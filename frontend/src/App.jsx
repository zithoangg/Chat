//hi
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");
  const [username, setUsername] = useState("User1");

  useEffect(() => {
    const getMessages = async () => {
      try {
        const response = await axios.get("/api/get_messages");
        setMessages(response.data);
      } catch (error) {
        console.error("Error fetching messages:", error);
      }
    };

    getMessages();
  }, []);

  const handleSendMessage = async () => {
    if (!message.trim()) return;

    try {
      await axios.post("/api/send_message", { username, message });
      setMessages([...messages, { username, message }]);
      setMessage("");
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  return (
    <div className="App">
      <h1>Chat App</h1>
      <input
        type="text"
        placeholder="Enter your message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>Send</button>

      <h2>Messages</h2>
      <ul>
        {messages.map((msg, index) => (
          <li key={index}>
            <strong>{msg.username}: </strong>{msg.message}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
