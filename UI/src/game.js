// 모험 시작 버튼 클릭 이벤트 핸들러
document.getElementById('startButton').addEventListener('click', function() {
    // 이름 입력 화면으로 이동
    showNameInput();
  });
  
  // 이름 입력 화면 표시 함수
  function showNameInput() {
    // 이름 입력 폼과 제출 버튼 표시
    document.getElementById('nameInputContainer').style.display = 'block';
  
    // 제출 버튼 클릭 이벤트 핸들러
    document.getElementById('submitButton').addEventListener('click', function() {
      // 입력한 이름 가져오기
      var playerName = document.getElementById('nameInput').value;
  
      // 이름이 비어있지 않은 경우에만 처리
      if (playerName.trim() !== '') {
        // 이름 입력 화면 감추기
        document.getElementById('nameInputContainer').style.display = 'none';
  
        // 포인트 제공 함수 호출
        providePoints(playerName);
      }
    });
  }
  
  // 포인트 제공 함수
  function providePoints(playerName) {
    // TODO: 포인트를 제공하는 로직 작성
  
    // 주사위 UI 표시
    document.getElementById('dice').style.display = 'block';
  
    // 주사위 클릭 이벤트 핸들러
    document.getElementById('dice').addEventListener('click', function() {
      // 주사위 값을 랜덤하게 생성
      var diceValue = Math.floor(Math.random() * 10) + 1;
  
      // 주사위 UI 감추기
      document.getElementById('dice').style.display = 'none';
  
      // 스토리 표시 함수 호출
      showStory(playerName, diceValue);
    });
  }
  
  // 스토리 표시 함수
  function showStory(playerName, diceValue) {
    // TODO: 스토리와 선택지 표시하는 로직 작성
  
    // 예시: 스토리와 선택지를 HTML에 동적으로 추가
    var storyContainer = document.getElementById('storyContainer');
    storyContainer.innerHTML = `
      <div>안녕하세요, ${playerName}님! 주사위를 던져서 포인트를 받았습니다.</div>
      <div>주사위 값: ${diceValue}</div>
      <div>이제 스토리와 선택지를 표시해주세요.</div>
      <!-- 선택지 버튼 등을 HTML로 추가 -->
    `;
  }
  