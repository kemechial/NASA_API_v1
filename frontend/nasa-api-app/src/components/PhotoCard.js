// src/components/PhotoCard.js
import React from 'react';

const PhotoCard = ({ photo }) => {
  return (
    <div className="photo-card">
      <img src={photo.img_src} alt={`Mars Rover ${photo.rover.name}`} width="200" />
      <div className="photo-details">
        <p><strong>Camera:</strong> {photo.camera.full_name}</p>
        <p><strong>Earth Date:</strong> {photo.earth_date}</p>
        <p><strong>Sol:</strong> {photo.sol}</p>
      </div>
    </div>
  );
};

export default PhotoCard;