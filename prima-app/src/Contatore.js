import React, {  useState } from 'react'

const Contatore = () => {

    const [count, setCount] = useState(0);
    const increment = () => {

        //  setTimeout(()=>{
        setCount((oldCount) => {
          if (oldCount < 4) {
            return oldCount + 1;
          } else {
            return oldCount;
          }
        });
        //},2000)
      };
      return (
        <>
          <div>{count}</div>
          <div>
            <button onClick={() => setCount(count - 1)}>Decrementa</button>&nbsp;
            <button onClick={increment}>Incrementa</button>
          </div>
        </>
      );
}

export default Contatore