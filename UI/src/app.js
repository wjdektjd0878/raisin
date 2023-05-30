import React, { useState } from "react";
import axios from 'axios';

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const user = {
      name: name,
      email: email,
      password: password
    };

    // axios를 사용하여 백엔드로 사용자 정보 전송
    try {
      const response = await axios.post('/api/login', user);
      console.log(response.data); // 응답 데이터 출력
    } catch (error) {
      console.error('Error:', error);
    }

    // form reset
    setName('');
    setEmail('');
    setPassword('');
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          이름:
          <input type="text" value={name} onChange={handleNameChange} />
        </label>
        <label>
          이메일:
          <input type="email" value={email} onChange={handleEmailChange} />
        </label>
        <label>
          비밀번호:
          <input type="password" value={password} onChange={handlePasswordChange} />
        </label>
        <input type="submit" value="제출" />
      </form>
    </div>
  );
}

export default App;
