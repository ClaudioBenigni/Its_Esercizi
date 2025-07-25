import React, { useState } from 'react';
import './App.css';
import Clock from './Clock';
import Componente1 from './Componente1';
import { anagrafica } from './data/dati';
import Contatore from './Contatore';
import EsempioUseEffect from './EsempioUseEffect';
import CleanUp from './CleanUp';
import CambiaNome from './CambiaNome';
import LoginForm from './LoginForm';


function App() {

  let nome = "Claudio"

  const [nome1, setNome1] = useState(nome);



  const cambiaNome = () => {
    console.log(nome);
    nome = "Mario";
    setNome1(nome);
    console.log(nome);
  };
  const [persone, setPersone] = useState(anagrafica);
  const elimina = (id) => {
    const newAnag = persone.filter((p)=>{
      return p.id !== id
    })
    setPersone(newAnag)
  };

  const [persona,setPersona]=useState ({
    id:"1",
    nome:"Rob",
    cognome:"Del",
    età:48
  })


  const compleanno=()=>{
    let anni=persona.età+1;

    setPersona({
      ...persona,
      età:anni
    })
  }

  return (
    <>
    <div className="App">
      <LoginForm></LoginForm>
      <CambiaNome></CambiaNome>
      <CleanUp></CleanUp>
      <EsempioUseEffect> </EsempioUseEffect>
      <Contatore></Contatore>
      <h1> {nome1} </h1>
      <button onClick={cambiaNome} className="btn btn-primary"> Cambia Nome</button>
      <br></br>
      <br></br>
      <div>{persona.nome}</div>
      <div>{persona.cognome}</div>
      <div>{persona.età}</div>
      <button onClick={compleanno} className="btn btn-primary"> Compleanno </button>

      {persone.map((p) => {
          return (
            <div key={p.id}>
              <span>
                {p.nome} {p.cognome}
              </span>
              &nbsp;&nbsp; 
              <button className="btn btn-primary"
                onClick={() => {
                  elimina(p.id);
                }}
              >
                Elimina
              </button>
            </div>
          );
        })}
      <h1></h1>
      <Clock timezone="0" country="Italy"> </Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="7" country="Japan"></Clock>
      
      
      {/* <h1>Primo Elemento {nome} </h1>
      <Componente1> Claudio </Componente1>
      <Componente1/>
      <h2>
        {
          new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString()

        }
      </h2>
      <h2>
      <Clock timezone="0" country="Italy"> </Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="7" country="Japan"></Clock>
    
      </h2>
          <h2>{getDate(new Date())}</h2>
    </div>
    <footer>

    </footer> */}
    </div>
    </>
  );
}

export default App;