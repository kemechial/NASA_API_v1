from flask import Flask, jsonify
import requests, os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')  # Go up one directory
load_dotenv(dotenv_path=dotenv_path)

NASA_API_KEY = os.environ.get("NASA_API_KEY")
if not NASA_API_KEY:
    raise ValueError("NASA_API_KEY environment variable not set.")

app = Flask(__name__)


@app.route("/apod", methods=["GET"])
def get_apod():
    params = {"api_key": NASA_API_KEY}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    return jsonify(response.json())

@app.route("/mars-photos", methods=["GET"])
def get_mars_photos():
    params = {"api_key": NASA_API_KEY, "sol": 1000, "camera": "fhaz"}
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", params=params)
    return jsonify(response.json())

@app.route("/neos", methods=["GET"])
def get_neos():
    params = {"api_key": NASA_API_KEY, "start_date": "2022-01-01", "end_date": "2022-01-07"}
    response = requests.get("https://api.nasa.gov/neo/rest/v1/feed", params=params)
    return jsonify(response.json())

@app.route("/earth-observations", methods=["GET"])
def get_earth_observations():
    params = {"api_key": NASA_API_KEY, "lon": -74.006, "lat": 40.7128, "date": "2022-01-01"}
    response = requests.get("https://api.nasa.gov/earth/asset", params=params)
    return jsonify(response.json())

@app.route("/epic", methods=["GET"])
def get_epic():
    params = {"api_key": NASA_API_KEY}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural", params=params)
    return jsonify(response.json())

@app.route("/exoplanets", methods=["GET"])
def get_exoplanets():
    query = "select * from ps where pl_name like '%Kepler%'"
    response = requests.get(f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}")
    return jsonify(response.json())

@app.route("/space-weather", methods=["GET"])
def get_space_weather():
    params = {"api_key": NASA_API_KEY, "start_date": "2022-01-01", "end_date": "2022-01-07"}
    response = requests.get("https://api.nasa.gov/DONKI/notifications", params=params)
    return jsonify(response.json())

@app.route("/iss-location", methods=["GET"])
def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    return jsonify(response.json())

@app.route("/asteroids", methods=["GET"])
def get_asteroids():
    params = {"api_key": NASA_API_KEY}
    response = requests.get("https://api.nasa.gov/neo/rest/v1/neo/browse", params=params)
    return jsonify(response.json())

@app.route("/comets", methods=["GET"])
def get_comets():
    params = {"api_key": NASA_API_KEY}
    response = requests.get("https://api.nasa.gov/neo/rest/v1/comet", params=params)
    return jsonify(response.json())

@app.route("/solar-system", methods=["GET"])
def get_solar_system():
    params = {"api_key": NASA_API_KEY}
    response = requests.get("https://api.nasa.gov/planetary/solar-system", params=params)
    return jsonify(response.json())

@app.route("/climate-data", methods=["GET"])
def get_climate_data():
    params = {"api_key": NASA_API_KEY, "lon": -74.006, "lat": 40.7128, "date": "2022-01-01"}
    response = requests.get("https://api.nasa.gov/earth/earthdata/climate", params=params)
    return jsonify(response.json())

@app.route("/natural-events", methods=["GET"])
def get_natural_events():
    params = {"api_key": NASA_API_KEY, "start_date": "2022-01-01", "end_date": "2022-01-07"}
    response = requests.get("https://api.nasa.gov/earth/earthdata/natural-event-tracker", params=params)
    return jsonify(response.json())

@app.route("/satellite-data", methods=["GET"])
def get_satellite_data():
    params = {"api_key": NASA_API_KEY, "lon": -74.006, "lat": 40.7128, "date": "2022-01-01"}
    response = requests.get("https://api.nasa.gov/earth/earthdata/satellite", params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3030, debug=True)