import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Optional: If you have global styles
import App from './App'; // Import the main App component

// Render the React App component
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
