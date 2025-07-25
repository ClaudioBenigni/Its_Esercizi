const Componente1 = (props) => {
    return (
      <>
      <div>Componente1 {props.children} </div>
      <Anagrafica></Anagrafica>
      <Messaggio></Messaggio>
      </>
    )
  }
  
  export default Componente1

  const Anagrafica=()=> {

    return (
        <div> Anagrafica </div>
    )

}

const Messaggio=()=> {

    return (
        <div> Messaggio </div>
    )

}