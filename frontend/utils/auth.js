// utils/auth.js - Authentication utility functions

// Get token from localStorage
export const getToken = () => {
  return typeof window !== 'undefined' ? localStorage.getItem('token') : null;
};

// Set token in localStorage
export const setToken = (token) => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('token', token);
  }
};

// Remove token from localStorage
export const removeToken = () => {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('token');
  }
};

// Check if user is authenticated
export const isAuthenticated = () => {
  const token = getToken();
  // In a real app, you would also verify the token is valid
  return !!token;
};