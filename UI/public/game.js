// JavaScript (game.js)

document.getElementById('startButton').addEventListener('click', function() {
  fetch('http://localhost:5000/getRandomValue') // 백엔드 API 요청
    .then(response => response.json()) // 응답을 JSON 형태로 변환
    .then(data => {
      var randomValue = data.randomValue; // 응답에서 랜덤한 값 가져오기
      console.log(randomValue)
      showStory(randomValue); // 가져온 값을 사용하여 스토리를 표시하는 함수 호출
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

function showStory(value) {
  var storyContainer = document.getElementById('storyContainer');
  storyContainer.innerHTML = `
    <div>모험이 시작되었습니다!</div>
    <div>랜덤한 값: ${value}</div>
    <div>스토리 내용...</div>
  `;
  // 이어지는 스토리와 선택지 등을 HTML로 추가하여 보여줍니다.
}
