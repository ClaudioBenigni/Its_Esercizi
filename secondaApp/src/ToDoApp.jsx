import React from 'react'
import ToDoForm from './ToDoForm'
import ToDoList from './ToDoList'
import { useState, useEffect } from 'react'
import { createTask, fetchTasks, deleteTaskService, toggleTaskService } from './api'



const API_URL = "http://localhost:3000/tasks"

const ToDoApp = () => {
    const [tasks, setTasks] = useState([])
    const getTasks = async () => {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error("Errore fetch :(")
            const data = await fetchTasks()

            setTasks(data)
        } catch (err) {
            console.log(err)
        }
    };

    const addTask=async (text) =>{
        await createTask(text);
    //await fetch(API_URL, {
     // method: "POST",
     // headers: { "Content-Type": "application/json" },
     // body:JSON.stringify({text,completed:false})
    //});
        getTasks();
  }
    const deleteTask = async (id) => {
        //await fetch(API_URL + "/" + id, { method: "DELETE" });
        await deleteTaskService(id);
        getTasks();
    }

    const toggleTask = async (id, completed) => {
        await toggleTaskService(id, completed);
        getTasks();
    }

    useEffect(() => {
        getTasks()
    }, [])
    return (
        <div>ToDoApp
            <ToDoForm onAddTask={addTask}></ToDoForm>
            <ToDoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask}></ToDoList>
        </div>
    )
}

export default ToDoApp