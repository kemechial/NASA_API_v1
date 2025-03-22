// src/components/RoverForm.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RoverForm = () => {
  const [formData, setFormData] = useState({
    roverName: 'curiosity',
    sol: '',
    earthDate: '',
    camera: 'all',
    page: 1,
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const queryParams = new URLSearchParams(formData).toString();
    navigate(`/gallery?${queryParams}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Rover:
        <select name="roverName" value={formData.roverName} onChange={handleChange}>
          <option value="curiosity">Curiosity</option>
          <option value="opportunity">Opportunity</option>
          <option value="spirit">Spirit</option>
        </select>
      </label>

      <label>
        Sol:
        <input
          type="number"
          name="sol"
          value={formData.sol}
          onChange={handleChange}
          placeholder="Enter sol"
        />
      </label>

      <label>
        Earth Date:
        <input
          type="date"
          name="earthDate"
          value={formData.earthDate}
          onChange={handleChange}
        />
      </label>

      <label>
        Camera:
        <select name="camera" value={formData.camera} onChange={handleChange}>
          <option value="all">All</option>
          <option value="fhaz">FHAZ</option>
          <option value="rhaz">RHAZ</option>
          <option value="mast">MAST</option>
          <option value="chemcam">CHEMCAM</option>
          <option value="mahli">MAHLI</option>
          <option value="mardi">MARDI</option>
          <option value="navcam">NAVCAM</option>
          <option value="pancam">PANCAM</option>
          <option value="minites">MINITES</option>
        </select>
      </label>

      <label>
        Page:
        <select name="page" value={formData.page} onChange={handleChange}>
          {[...Array(25).keys()].map((n) => (
            <option key={n + 1} value={n + 1}>
              {n + 1}
            </option>
          ))}
        </select>
      </label>

      <button type="submit">Fetch Photos</button>
    </form>
  );
};

export default RoverForm;