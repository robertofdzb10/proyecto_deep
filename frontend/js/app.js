// app.js

// Añade un mensaje al contenedor del chat
function addMessage(sender, text) {
  const chatBody = document.getElementById('chatBody');
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message');
  messageDiv.classList.add(sender === 'user' ? 'user-message' : 'agent-message');
  messageDiv.textContent = text;
  chatBody.appendChild(messageDiv);

  // Desplaza el scroll hasta el final para ver el último mensaje
  chatBody.scrollTop = chatBody.scrollHeight;
}

// Envía el mensaje a la API y maneja la respuesta
async function sendMessage() {
  const userInputElem = document.getElementById('userInput');
  const userInput = userInputElem.value.trim();
  
  if (!userInput) return;

  // Añadir el mensaje del usuario al chat
  addMessage('user', userInput);

  // Limpiar el input
  userInputElem.value = '';

  try {
    // Realiza la solicitud POST a la API de FastAPI
    const response = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_input: userInput })
    });

    if (!response.ok) {
      throw new Error('Error en la respuesta del servidor');
    }

    const data = await response.json();
    // Añade el mensaje del agente al chat
    addMessage('agent', data.prediction);

  } catch (error) {
    addMessage('agent', `Error: ${error.message}`);
  }
}
