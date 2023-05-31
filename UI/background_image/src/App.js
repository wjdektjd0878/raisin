// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StartPage from './StartPage';
import NamePage from './NamePage';
import DicePage from './DicePage';
import StoryPage from './StoryPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<StartPage />} />
        <Route path="/name" element={<NamePage />} />
        <Route path="/dice" element={<DicePage />} />
        <Route path="/story" element={<StoryPage />} />
      </Routes>
    </Router>
  );
}

export default App;
