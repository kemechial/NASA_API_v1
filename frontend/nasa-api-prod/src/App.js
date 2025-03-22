import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Correct import
import RoverForm from './components/RoverForm';
import MarsPhotoGallery from './components/MarsPhotoGallery';

function App() {
  return (
    <Router> {/* BrowserRouter wrapping the entire app */}
      <div className="App">
        <h1>Mars Rover Photo Fetcher</h1>
        <Routes>
          <Route path="/" element={<RoverForm />} />
          <Route path="/gallery" element={<MarsPhotoGallery />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;