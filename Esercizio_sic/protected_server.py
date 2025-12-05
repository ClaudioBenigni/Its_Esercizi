from flask import Flask, make_response, redirect, request, session
from pathlib import Path
import requests

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Cambia in produzione!

STATIC_DIR = Path("static")
IDENTITY_MANAGER_URL = "http://localhost:10000"

# ---
# Helper: serve file HTML
# ---
def serve_html(filename: str):
    path = STATIC_DIR / filename
    if not path.exists():
        return make_response("<h1>404 - File non trovato</h1>", 404)

    html = path.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---
# Helper: verifica autenticazione
# ---
def is_authenticated():
    """Verifica se l'utente è autenticato con l'Identity Manager"""
    session_id = request.cookies.get("session_id")
    
    if not session_id:
        return False
    
    try:
        response = requests.get(
            f"{IDENTITY_MANAGER_URL}/api/validate",
            cookies={"session_id": session_id}
        )
        return response.status_code == 200 and response.json().get("valid", False)
    except requests.RequestException:
        return False

def get_username():
    """Ottiene l'username dall'Identity Manager"""
    session_id = request.cookies.get("session_id")
    
    if not session_id:
        return None
    
    try:
        response = requests.get(
            f"{IDENTITY_MANAGER_URL}/api/validate",
            cookies={"session_id": session_id}
        )
        if response.status_code == 200:
            return response.json().get("username")
    except requests.RequestException:
        pass
    
    return None

# ---
# Routes pubbliche
# ---
@app.route("/")
def root():
    return serve_html("home.html")

@app.route("/html/<page>")
def html_page(page):
    return serve_html(f"{page}.html")

@app.route("/go/<target>")
def go(target):
    return redirect(f"/html/{target}", code=302)

# ---
# Routes di autenticazione
# ---
@app.route("/login")
def login_page():
    """Pagina di login"""
    return serve_html("login.html")

@app.route("/protected")
def protected_page():
    """Pagina protetta - richiede autenticazione"""
    if not is_authenticated():
        return redirect("/login", code=302)
    
    username = get_username()
    html = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Area Protetta</h1>
        <p>Benvenuto, <strong>{username}</strong>!</p>
        <p>Questa è una pagina protetta che richiede il login.</p>
        <a href="/">Home</a> | 
        <a href="/logout">Logout</a>
    </body>
    </html>
    """
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

@app.route("/api/protected_login", methods=["POST"])
def protected_login():
    """Endpoint per il login sul server protetto"""
    username = request.form.get("username")
    password = request.form.get("password")
    
    try:
        # Invia le credenziali all'Identity Manager
        response = requests.post(
            f"{IDENTITY_MANAGER_URL}/api/login",
            json={"username": username, "password": password}
        )
        
        if response.status_code == 200:
            # Login riuscito, ottieni la risposta
            auth_data = response.json()
            session_id = auth_data["session_id"]
            
            # Reindirizza alla pagina protetta
            resp = redirect("/protected", code=302)
            resp.set_cookie(
                "session_id",
                session_id,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=3600
            )
            return resp
        else:
            # Login fallito
            return serve_html("login_error.html")
            
    except requests.RequestException:
        return serve_html("login_error.html")

@app.route("/logout")
def logout():
    """Logout da entrambi i server"""
    session_id = request.cookies.get("session_id")
    
    if session_id:
        try:
            requests.post(f"{IDENTITY_MANAGER_URL}/api/logout")
        except requests.RequestException:
            pass
    
    resp = redirect("/", code=302)
    resp.set_cookie("session_id", "", expires=0)
    return resp

# ---
# Routes per cookie (mantenute dalla versione originale)
# ---
@app.route("/setcookie")
def setcookie():
    resp = serve_html("home.html")
    resp.set_cookie("sessionid", "abc123", path="/")
    return resp

@app.route("/showcookie")
def showcookie():
    cookies = request.cookies
    html = "<h1>Cookie ricevuti</h1><pre>" 
    for k, v in cookies.items():
        html += f"{k} = {v}\n"
    html += "</pre><a href='/'>Torna alla home</a>"
    
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---
# Avvio server
# ---
if __name__ == "__main__":
    STATIC_DIR.mkdir(exist_ok=True)
    print("Server Protetto avviato su http://localhost:9000")
    app.run(host="0.0.0.0", port=9000, debug=True)