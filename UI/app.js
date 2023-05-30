import React, { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // 여기서 name, email을 처리하실 수 있습니다.
    console.log(name, email);
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
        <input type="submit" value="제출" />
      </form>
    </div>
  );
}

export default App;
