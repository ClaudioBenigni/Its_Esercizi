import { useState } from "react";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [nome, setNome] = useState("");
  const [cognome, setCognome] = useState("");

  return (
    <div>
      <form>
        <div>
          <label>Email</label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button className="btn btn-success">Login</button>
      </form>

      <hr />

      <div className="container">
        <form className="row g-3">
          <div className="col-md-6">
            <label htmlFor="nome">Nome</label>
            <input
              type="text"
              id="nome"
              className="form-control"
              required
              value={nome}
              onChange={(event) => setNome(event.target.value)}
            />
          </div>
          <div className="col-md-6">
            <label htmlFor="cognome">Cognome</label>
            <input
              type="text"
              id="cognome"
              required
              value={cognome}
              onChange={(event) => setCognome(event.target.value)}
            />
          </div>

          <button className="btn btn-success">Login</button>
        </form>
      </div>

      <p>Email: {email}</p>
      <p>Password: {password}</p>
      <p>Nome: {nome}</p>
      <p>Cognome: {cognome}</p>
    </div>
  );
};

export default LoginForm;


