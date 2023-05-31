import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function NamePage() {
  const [name, setName] = useState('');
  const navigate = useNavigate();

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleNameSubmit = (event) => {
    event.preventDefault();
    // 이름이 제출되면 주사위 페이지로 이동합니다.
    navigate('/dice');
  };

  return (
    <div>
      <h1>이름을 입력하세요</h1>
      <form onSubmit={handleNameSubmit}>
        <input type="text" value={name} onChange={handleNameChange} />
        <input type="submit" value="제출" />
      </form>
    </div>
  );
}

export default NamePage;
