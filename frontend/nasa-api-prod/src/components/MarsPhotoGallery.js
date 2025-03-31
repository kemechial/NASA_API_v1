import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';
import PhotoCard from './PhotoCard';
import '../styles/PhotoGallery.css';

const MarsPhotoGallery = () => {
  const [photos, setPhotos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPhotos = async () => {
      setLoading(true);
      setError(null);

      const searchParams = new URLSearchParams(location.search);
      const params = {
        roverName: searchParams.get('roverName'),
        sol: searchParams.get('sol'),
        earth_date: searchParams.get('earthDate'),
        camera: searchParams.get('camera'),
        page: searchParams.get('page'),
      };

      try {
        const response = await axios.get(`/api/mars-photos/${params.roverName}`, { params });
        setPhotos(response.data.photos || []);
      } catch (error) {
        console.error('Error fetching photos:', error);
        setError('An error occurred while fetching photos. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchPhotos();
  }, [location.search]);

  const handleGoBack = () => {
    navigate('/');
  };

  if (loading) {
    return <p className="text-center">Loading photos...</p>;
  }

  if (error) {
    return <p className="text-danger text-center">{error}</p>;
  }

  return (
    <div className="container mt-4">
      <div className="d-flex flex-column align-items-center mb-4">
        <h1>Mars Rover Photo Fetcher</h1>
        <button className="btn btn-secondary mt-2" onClick={handleGoBack}>Go Back</button>
      </div>

      {photos.length > 0 ? (
        <div className="row">
          {photos.map((photo) => (
            <div key={photo.id} className="col-md-4 mb-4">
              <PhotoCard photo={photo} />
            </div>
          ))}
        </div>
      ) : (
        <p className="text-center">No photos found for your search criteria. Please try different parameters.</p>
      )}
    </div>
  );
};

export default MarsPhotoGallery;