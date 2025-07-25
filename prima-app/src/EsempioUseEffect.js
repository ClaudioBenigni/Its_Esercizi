import React,{useEffect, useState} from 'react'

const EsempioUseEffect = () => {
    const [count, setCount] = useState(0);
    const [count2, setCount2] = useState(0);



    useEffect(() => {
        console.log("Ho chiamato useffect")
        if(count<1){
            document.title = "Nessun titolo"
        }else{
            document.title = "Ho trovato qualcosa"
        }
    },[count,count2]);
    // console.log("Ho chiamato useffect")
    console.log("Sono fuori dallo useEffect")
  return (
    <>
    <div>EsempioUseEffect count 1: {count}</div>
    <div>EsempioUseEffect count 2: {count2}</div>
    <button onClick={() => setCount(count + 1)}> Incrementa </button>;
    <button onClick={() => setCount2(count2 + 1)}> Incrementa </button>;
    </>
  );
};

export default EsempioUseEffect






