import React, { useState } from 'react';

const CambiaNome = () => {
  const nomeOriginale = "Claudio";
  const [nome1, setNome1] = useState(nomeOriginale);

  const CambiaNome = () => {
    setNome1("Rune");
  };

  const ripristinaNome = () => {
    setNome1(nomeOriginale);
  };

  return (
    <div>
      <p>{nome1}</p>
      <button onClick={CambiaNome}>Cambia Nome</button>
      <button onClick={ripristinaNome}>Ripristina Nome</button>
    </div>
  );
};

export default CambiaNome;