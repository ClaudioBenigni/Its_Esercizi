import React from 'react';
import './App.css';
import Saluto from './Saluto.jsx';
import CardUtente from './CardUtente.jsx';
import MenuRistorante from './MenuRistorante.jsx'; // passo 3

function App() {
  return (
    <>
      <Saluto />
      <CardUtente nome="Claudio" email="claudio.benigni06@gmail.com" />
      <MenuRistorante /> {/* passo 3: menu dinamico */}
    </>
  );
}

export default App;
