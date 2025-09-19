import { useState, useEffect } from 'react';
import bgImg from './assets/bg-yoolee.png';
import './App.css';
import { initializeApp } from 'firebase/app';
import {
  getFirestore,
  collection,
  addDoc,
  onSnapshot,
  query,
  orderBy,
  serverTimestamp,
  getDocs,
  Timestamp,
} from 'firebase/firestore';

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const db = getFirestore(app);

export default function App() {
  const [userName, setUserName] = useState('');
  useEffect(() => {
    if (!userName) {
      setUserName(prompt('이름을 알려주세요') || null);
    }
    const q = query(collection(db, 'messages'), orderBy('Timestamp', 'asc'));

    getDocs(q).then((snapshot) => {
      const oldMessages = snapshot.docs.map((doc) => doc.data());
      setMessages(oldMessages);
    });

    const unsubscribe = onSnapshot(q, (snapshot) => {
      const msgs = snapshot.docs.map((doc) => doc.data());
      setMessages(msgs);
    });

    return () => unsubscribe(); // 컴포넌트 언마운트 시 구독 해제
  }, []);

  // 메시지 상태
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  // 메시지 전송 함수
  const sendMessage = async () => {
    if (!input.trim()) return;
    setMessages([...messages, { user: userName, text: input }]);

    await addDoc(collection(db, 'messages'), {
      user: userName,
      text: input,
      Timestamp: serverTimestamp(),
    });
    console.log(messages);

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
