// src/components/MarsPhotoGallery.js
import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';
import PhotoCard from './PhotoCard';
import '../styles/PhotoGallery.css';

const MarsPhotoGallery = () => {
  const [photos, setPhotos] = useState([]);
  const [loading, setLoading] = useState(true); // Add loading state
  const [error, setError] = useState(null); // Add error state
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPhotos = async () => {
      setLoading(true); // Set loading to true before fetching
      setError(null); // Clear any previous errors

      const searchParams = new URLSearchParams(location.search);
      const params = {
        roverName: searchParams.get('roverName'),
        sol: searchParams.get('sol'),
        earth_date: searchParams.get('earthDate'),
        camera: searchParams.get('camera'),
        page: searchParams.get('page'),
      };

      try {
        const response = await axios.get(`/mars-photos/${params.roverName}`, { params });
        setPhotos(response.data.photos || []);
      } catch (error) {
        console.error('Error fetching photos:', error);
        setError('An error occurred while fetching photos. Please try again later.');
      } finally {
        setLoading(false); // Set loading to false after fetching, regardless of success or failure
      }
    };

    fetchPhotos();
  }, [location.search]);

  const handleGoBack = () => {
    navigate('/');
  };

  if (loading) {
    return <p>Loading photos...</p>; // Display loading message
  }

  if (error) {
    return <p className="error">{error}</p>; // Display error message
  }

  return (
    <div>
      <button onClick={handleGoBack}>Go Back</button>
      <h2>Mars Rover Photos</h2>

      {photos.length > 0 ? (
        <div className="photo-gallery">
          {photos.map((photo) => (
            <PhotoCard key={photo.id} photo={photo} />
          ))}
        </div>
      ) : (
        <p>No photos found for your search criteria. Please try different parameters.</p>
      )}
    </div>
  );
};

export default MarsPhotoGallery;