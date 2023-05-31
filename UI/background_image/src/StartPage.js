import React from 'react';
import { useNavigate } from 'react-router-dom';

function StartPage() {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    // 모험 시작 버튼을 클릭하면 이름 입력 페이지로 이동합니다.
    navigate('/name');
  };

  return (
    <div>
      <h1>모험을 시작하세요!</h1>
      <button onClick={handleButtonClick}>모험 시작</button>
    </div>
  );
}

export default StartPage;
