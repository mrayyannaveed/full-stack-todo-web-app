// hooks/useTasks.js - Custom hook for managing tasks

import { useState, useEffect } from 'react';

// This is a temporary hook that uses mock data
// In the future, it will connect to the API
export const useTasks = (token) => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Simulate API call
    const fetchTasks = async () => {
      try {
        setLoading(true);
        // In a real app, this would be an API call:
        // const data = await taskService.getAllTasks(token);
        // setTasks(data);
        
        // For now, just initialize with empty array
        // In a real app, this would fetch user-specific tasks
        setTimeout(() => {
          setTasks([]);
          setLoading(false);
        }, 500);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    if (token) {
      fetchTasks();
    } else {
      // If no token, clear tasks
      setTasks([]);
      setLoading(false);
    }
  }, [token]);

  const addTask = async (taskData) => {
    try {
      // In a real app, this would be an API call:
      // const newTask = await taskService.createTask(taskData, token);
      const newTask = {
        id: Date.now(),
        ...taskData,
        status: 'pending'
      };
      
      setTasks(prev => [...prev, newTask]);
      return newTask;
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  const updateTask = async (id, taskData) => {
    try {
      // In a real app, this would be an API call:
      // const updatedTask = await taskService.updateTask(id, taskData, token);
      setTasks(prev => prev.map(task => 
        task.id === id ? { ...task, ...taskData } : task
      ));
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  const deleteTask = async (id) => {
    try {
      // In a real app, this would be an API call:
      // await taskService.deleteTask(id, token);
      setTasks(prev => prev.filter(task => task.id !== id));
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  const toggleTaskStatus = async (id) => {
    try {
      // In a real app, this would be an API call:
      // const updatedTask = await taskService.toggleTaskStatus(id, token);
      setTasks(prev => prev.map(task => 
        task.id === id 
          ? { ...task, status: task.status === 'pending' ? 'completed' : 'pending' } 
          : task
      ));
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  return {
    tasks,
    loading,
    error,
    addTask,
    updateTask,
    deleteTask,
    toggleTaskStatus
  };
};