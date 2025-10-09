import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCrud from './user-crud-analyst/UserCrud'
import ToDoApp from './ToDoApp'
import MainComponent from './useContext/MainComponent'

function App() {

  return (
    <>
    <MainComponent></MainComponent>
    <ToDoApp></ToDoApp>
    </>
  )
}

export default App
