import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [pingResponse, setPingResponse] = useState(null);

  useEffect(() => {
    fetchPing();
  }, []);

  const fetchPing = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/ping/');
      setPingResponse(response.data.message);
    } catch (error) {
      console.error('Error fetching ping:', error);
    }
  };

  return (
    <div className="App">
      <h1>Ping-Pong App</h1>
      {pingResponse !== null ? (
        <p>Response: {pingResponse}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;