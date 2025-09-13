import { useState } from 'react';
import bgImg from './assets/bg-yoolee.png';
import './App.css';

export default function App() {
  // 처음 접속 시 이름 입력 (임시 로그인 같은 느낌)
  const [userName] = useState(() => prompt('이름을 입력하세요') || '익명');

  // 메시지 상태
  const [messages, setMessages] = useState([
    { user: '은미', text: '나 지금 가는 중이야' },
    { user: '엄마', text: '저녁 뭐 먹을래?' },
  ]);
  const [input, setInput] = useState('');

  // 메시지 전송 함수
  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, { user: userName, text: input }]);
    setInput('');
  };

  return (
    <div className='app-container' style={{ backgroundImage: `url(${bgImg})` }}>
      {/* 채팅 박스 */}
      <div className='chat-box'>
        <h2>YOOLEE FAMILY CHAT</h2>

        <div className='messages'>
          {messages.map((m, idx) => (
            <p
              key={idx}
              className={m.user === '은미' ? 'my-message' : 'other-message'}
            >
              <b>{m.user}:</b> {m.text}
            </p>
          ))}
        </div>

        <form
          className='input-row'
          onSubmit={(e) => {
            e.preventDefault();
            sendMessage();
          }}
        >
          <input
            type='text'
            placeholder='메시지를 입력하세요...'
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button type='submit'>전송</button>
        </form>
      </div>
    </div>
  );
}
