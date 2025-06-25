'use client';

import { useState, useEffect, FormEvent } from 'react';
import axios from 'axios';

interface Todo {
  id: string;
  task: string;
  completed: boolean;
}

const API_URL = 'http://localhost:8000/api/todos';

export default function Home() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [newTask, setNewTask] = useState('');

  // 1. Fetch todos
  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const response = await axios.get(API_URL);
        setTodos(response.data);
      } catch (error) {
        console.error('Error fetching todos:', error);
      }
    };
    fetchTodos();
  }, []);

  // 2. Add task
  const handleAddTask = async (e: FormEvent) => {
    e.preventDefault();
    if (!newTask.trim()) return;

    try {
      const response = await axios.post(API_URL, { task: newTask });
      setTodos([...todos, response.data]);
      setNewTask('');
    } catch (error) {
      console.error('Error adding task:', error);
    }
  };

  // 3. Toggle complete
  const handleToggleComplete = async (id: string) => {
    try {
      const response = await axios.patch(`${API_URL}/${id}`);
      setTodos(todos.map(todo => (todo.id === id ? response.data : todo)));
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };


  // 4. Edit task
  const handleEdit = async (id: string, oldText: string) => {
    const newText = prompt("Edit your task:", oldText);
    if (newText) {
      try {
        await axios.put(`${API_URL}/${id}`, { task: newText });
        setTodos(todos.map(todo => (todo.id === id ? { ...todo, task: newText } : todo)));
      } catch (error) {
        console.error('Error editing task:', error);
      }
    }
  };

  // 5. Delete task
  const handleDeleteTask = async (id: string) => {
    try {
      await axios.delete(`${API_URL}/${id}`);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  // 6. Clear completed
  const clearCompleted = async () => {
    try {
      await axios.delete(`${API_URL}/completed`);
      setTodos(todos.filter(todo => !todo.completed));
    } catch (error) {
      console.error('Error clearing completed tasks:', error);
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white p-8">
      <div className="w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-lg">
        <h1 className="text-3xl font-bold mb-6 text-center text-cyan-400">
          Full-Stack To-Do List
        </h1>

        <form onSubmit={handleAddTask} className="flex gap-2 mb-6">
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="Add a new task..."
            className="flex-grow p-2 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />
          <button
            type="submit"
            className="bg-cyan-600 hover:bg-cyan-700 text-white font-bold py-2 px-4 rounded transition-colors"
          >
            Add
          </button>
        </form>

        <ul className="space-y-3">
          {todos.map((todo) => (
            <li
              key={todo.id}
              className="flex items-center justify-between p-3 bg-gray-700 rounded-md"
            >
              <span
                onClick={() => handleToggleComplete(todo.id)}
                className={`cursor-pointer ${todo.completed ? 'line-through text-gray-500' : ''}`}
              >
                {todo.task}
              </span>
              <div className="flex gap-2">
                <button
                  onClick={() => handleEdit(todo.id, todo.task)}
                  className="bg-yellow-600 hover:bg-yellow-700 text-white text-xs font-bold py-1 px-2 rounded-full transition-colors"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDeleteTask(todo.id)}
                  className="bg-red-600 hover:bg-red-700 text-white text-xs font-bold py-1 px-2 rounded-full transition-colors"
                >
                  ✕
                </button>
              </div>
            </li>
          ))}
        </ul>

        <button
          onClick={clearCompleted}
          className="mt-4 bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded transition-colors w-full"
        >
          Clear Completed
        </button>
      </div>
    </main>
  );
}
