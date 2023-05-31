import React, { useEffect, useState } from 'react';

function StoryPage() {
  const [story, setStory] = useState(null);
  const [choice, setChoice] = useState(null);

  useEffect(() => {
    // 서버에 GET 요청을 보내 스토리 데이터를 가져옵니다.
    fetch('http://localhost:5000/story')
      .then(response => response.json())
      .then(data => {
        // 받아온 데이터를 state에 저장합니다.
        setStory(data.main);
        setChoice(data.choice);
      })
      .catch(error => console.error('Error:', error));
  }, []);

  // 아직 데이터가 로드되지 않았다면 로딩 메시지를 표시합니다.
  if (!story || !choice) {
    return <div>Loading...</div>;
  }

  // 데이터가 로드되었다면 스토리와 선택지를 표시합니다.
  return (
    <div>
      <h1>{story}</h1>
      <p>{choice}</p>
    </div>
  );
}

export default StoryPage;
