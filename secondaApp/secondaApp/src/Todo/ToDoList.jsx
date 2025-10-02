import React from 'react'
import ToDoItem from './ToDoItem'

const ToDoList = (props) => {
    console.log("Props", props)
  return (
    <ul className="list-group">
    {
        props.tasks.map((task) => {
            return <ToDoItem 
            key={task.id} 
            task={task}
            onDeleteTask ={props.onDeleteTask}
            onToggleTask={props.onToggleTask}>
            </ToDoItem>;
        })
        }
    </ul>
  )
}

export default ToDoList