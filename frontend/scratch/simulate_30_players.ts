import { io, Socket } from 'socket.io-client';

async function runLoadSimulation(pinCode: string, playerCount: number = 30) {
  console.log(`🚀 Starting Load Simulation with ${playerCount} concurrent players for PIN: ${pinCode}`);
  
  const sockets: Socket[] = [];
  const SERVER_URL = 'http://localhost:5005';

  for (let i = 1; i <= playerCount; i++) {
    const nickname = `Student_${i.toString().padStart(2, '0')}`;
    const socket = io(SERVER_URL, { transports: ['websocket', 'polling'] });
    sockets.push(socket);

    socket.on('connect', () => {
      socket.emit('player:join-session', { code: pinCode, nickname });
    });

    socket.on('player:joined', ({ nickname }) => {
      console.log(`✅ [${nickname}] Joined session successfully.`);
    });

    socket.on('player:question-started', ({ questionIndex, durationSec }) => {
      // Simulate random response delay between 300ms and 2500ms
      const delay = Math.floor(300 + Math.random() * 2200);
      const randomChoice = Math.floor(Math.random() * 4);

      setTimeout(() => {
        socket.emit('player:submit-answer', { code: pinCode, optionIndex: randomChoice });
      }, delay);
    });

    socket.on('player:answer-received', ({ pointsEarned, totalScore }) => {
      // Answer acknowledged
    });

    socket.on('player:round-summary', ({ isCorrect, rank, score }) => {
      console.log(`📊 [${nickname}] Round Result: ${isCorrect ? 'Correct ✓' : 'Wrong ✕'} | Rank: #${rank} | Score: ${score}`);
    });

    // Stagger connection requests slightly (10ms) to simulate real network burst
    await new Promise(r => setTimeout(r, 10));
  }

  console.log(`✨ All ${playerCount} socket clients initialized and connected.`);
}

// Read PIN from command line arguments
const pin = process.argv[2] || '123456';
runLoadSimulation(pin, 30);
