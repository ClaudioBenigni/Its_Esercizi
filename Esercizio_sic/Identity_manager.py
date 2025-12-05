from flask import Flask, request, jsonify, make_response
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)

# Database fittizio degli utenti
users_db = {
    "admin": "password123",
    "user1": "123456"
}

# Database delle sessioni attive
sessions_db = {}

class IdentityManager:
    @staticmethod
    def authenticate(username, password):
        """Verifica le credenziali dell'utente"""
        return users_db.get(username) == password
    
    @staticmethod
    def create_session(username):
        """Crea una nuova sessione"""
        session_id = secrets.token_urlsafe(32)
        expiry = datetime.now() + timedelta(hours=1)
        
        sessions_db[session_id] = {
            "username": username,
            "expiry": expiry,
            "created_at": datetime.now()
        }
        
        return session_id
    
    @staticmethod
    def validate_session(session_id):
        """Verifica se una sessione è valida"""
        if session_id not in sessions_db:
            return False
        
        session = sessions_db[session_id]
        if datetime.now() > session["expiry"]:
            del sessions_db[session_id]  # Sessione scaduta
            return False
        
        return True
    
    @staticmethod
    def get_username(session_id):
        """Ottiene l'username da una sessione valida"""
        if IdentityManager.validate_session(session_id):
            return sessions_db[session_id]["username"]
        return None

# Routes dell'Identity Manager
@app.route("/api/login", methods=["POST"])
def login():
    """Endpoint per il login"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username e password richiesti"}), 400
    
    if IdentityManager.authenticate(username, password):
        session_id = IdentityManager.create_session(username)
        response = jsonify({
            "success": True,
            "message": "Login effettuato",
            "username": username,
            "session_id": session_id
        })
        
        # Imposta il cookie di sessione
        response.set_cookie(
            "session_id", 
            session_id,
            httponly=True,
            secure=False,  # True in produzione con HTTPS
            samesite='Lax',
            max_age=3600  # 1 ora
        )
        
        return response
    else:
        return jsonify({"error": "Credenziali non valide"}), 401

@app.route("/api/validate", methods=["GET"])
def validate_session():
    """Endpoint per validare una sessione"""
    session_id = request.cookies.get("session_id") or request.args.get("session_id")
    
    if not session_id:
        return jsonify({"valid": False, "error": "Session ID non fornito"}), 400
    
    if IdentityManager.validate_session(session_id):
        username = IdentityManager.get_username(session_id)
        return jsonify({
            "valid": True,
            "username": username,
            "session_id": session_id
        })
    else:
        return jsonify({"valid": False, "error": "Sessione non valida o scaduta"}), 401

@app.route("/api/logout", methods=["POST"])
def logout():
    """Endpoint per il logout"""
    session_id = request.cookies.get("session_id")
    
    if session_id and session_id in sessions_db:
        del sessions_db[session_id]
    
    response = jsonify({"success": True, "message": "Logout effettuato"})
    response.set_cookie("session_id", "", expires=0)
    return response

@app.route("/api/users", methods=["GET"])
def list_users():
    """Endpoint per listare gli utenti (solo per testing)"""
    return jsonify({"users": list(users_db.keys())})

if __name__ == "__main__":
    print("Identity Manager avviato su http://localhost:10000")
    app.run(host="0.0.0.0", port=10000, debug=True)