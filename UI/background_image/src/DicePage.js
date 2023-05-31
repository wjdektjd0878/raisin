import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function DicePage() {
  const [points, setPoints] = useState(0);
  const navigate = useNavigate();

  const rollDice = () => {
    const newPoints = Math.floor(Math.random() * 10) + 1;
    setPoints(newPoints);
    navigate('/story');
  };

  return (
    <div>
      <h1>주사위를 굴려보세요</h1>
      <button onClick={rollDice}>주사위 굴리기</button>
      <p>{points}</p>
    </div>
  );
}

export default DicePage;
