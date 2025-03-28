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
    <div className="container mt-4">
      <h2 className="text-center mb-4">Search Mars Rover Photos</h2>
      <div className="d-flex justify-content-center">
        <form onSubmit={handleSubmit} className="row g-3 align-items-center">
          <div className="col-auto">
            <label>Rover:</label>
            <select name="roverName" value={formData.roverName} onChange={handleChange} className="form-control">
              <option value="curiosity">Curiosity</option>
              <option value="opportunity">Opportunity</option>
              <option value="spirit">Spirit</option>
            </select>
          </div>

          <div className="col-auto">
            <label>Sol:</label>
            <input
              type="number"
              name="sol"
              value={formData.sol}
              onChange={handleChange}
              placeholder="Enter sol"
              className="form-control"
            />
          </div>

          <div className="col-auto">
            <label>Earth Date:</label>
            <input
              type="date"
              name="earthDate"
              value={formData.earthDate}
              onChange={handleChange}
              className="form-control"
            />
          </div>

          <div className="col-auto">
            <label>Camera:</label>
            <select name="camera" value={formData.camera} onChange={handleChange} className="form-control">
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
          </div>

          <div className="col-auto">
            <label>Page:</label>
            <select name="page" value={formData.page} onChange={handleChange} className="form-control">
              {[...Array(25).keys()].map((n) => (
                <option key={n + 1} value={n + 1}>
                  {n + 1}
                </option>
              ))}
            </select>
          </div>

          <div className="col-auto">
            <button type="submit" className="btn btn-primary mt-3">Fetch Photos</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default RoverForm;