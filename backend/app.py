from venv import logger
from flask import Flask, jsonify, request
import requests, os
import logging
from dotenv import load_dotenv
from flask_cors import CORS
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


NASA_API_BASE_URL= "https://api.nasa.gov/mars-photos/api/v1"

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

NASA_API_KEY = os.environ.get("NASA_API_KEY")
if not NASA_API_KEY:
    raise ValueError("NASA_API_KEY environment variable not set.")

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

def fetch_data(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        return {"error": str(e)}

@app.route("/apod", methods=["GET"])
def get_apod():
    params = {"api_key": NASA_API_KEY}
    rover_name = request.args.get('rover', 'curiosity')
    data = fetch_data("https://api.nasa.gov/planetary/apod", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route('/api/mars-photos/<rover_name>', methods=['GET'])
def get_mars_photos(rover_name):
    logger.info(f"Incoming request URL: {request.url}")
    print(rover_name)
    earth_date = request.args.get('earth_date', None)
    camera = request.args.get('camera', "all")
    page = request.args.get('page', 1, type=int)  # Query parameter for page
    sol = request.args.get('sol', None)

    params = {
        'api_key': NASA_API_KEY
    }

    if earth_date:
        params['earth_date'] = earth_date
        
    elif sol:
        params['sol'] = sol
        
    elif camera:
        params['camera'] = camera

    params['page'] = page # Always include the page parameter
    #for debugging
    full_url = requests.Request('GET', f"{NASA_API_BASE_URL}/rovers/{rover_name}/photos", params=params).prepare().url

    # Print the full request URL
    logger.info(f"NASA API Request URL: {full_url}")
    print(f"NASA API Request URL: {full_url}")

    try:
        response = requests.get(f"{NASA_API_BASE_URL}/rovers/{rover_name}/photos", params=params)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route("/neos", methods=["GET"])
def get_neos():
    params = {"api_key": NASA_API_KEY, "start_date": "2022-01-01", "end_date": "2022-01-07"}
    data = fetch_data("https://api.nasa.gov/neo/rest/v1/feed", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/earth-observations", methods=["GET"])
def get_earth_observations():
    params = {"api_key": NASA_API_KEY, "lon": -74.006, "lat": 40.7128, "date": "2022-01-01"}
    data = fetch_data("https://api.nasa.gov/earth/asset", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/epic", methods=["GET"])
def get_epic():
    params = {"api_key": NASA_API_KEY}
    data = fetch_data("https://api.nasa.gov/EPIC/api/natural", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/exoplanets", methods=["GET"])
def get_exoplanets():
    query = "select * from ps where pl_name like '%Kepler%'"
    try:
        response = requests.get(f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}")
        response.raise_for_status()
        return jsonify(response.json())
    except RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/space-weather", methods=["GET"])
def get_space_weather():
    params = {"api_key": NASA_API_KEY, "start_date": "2022-01-01", "end_date": "2022-01-07"}
    data = fetch_data("https://api.nasa.gov/DONKI/notifications", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/iss-location", methods=["GET"])
def get_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        return jsonify(response.json())
    except RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/asteroids", methods=["GET"])
def get_asteroids():
    params = {"api_key": NASA_API_KEY}
    data = fetch_data("https://api.nasa.gov/neo/rest/v1/neo/browse", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/comets", methods=["GET"])
def get_comets():
    params = {"api_key": NASA_API_KEY}
    data = fetch_data("https://api.nasa.gov/neo/rest/v1/comet", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/solar-system", methods=["GET"])
def get_solar_system():
    params = {"api_key": NASA_API_KEY}
    data = fetch_data("https://api.nasa.gov/planetary/solar-system", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/climate-data", methods=["GET"])
def get_climate_data():
    params = {"api_key": NASA_API_KEY, "lon": -74.006, "lat": 40.7128, "date": "2022-01-01"}
    data = fetch_data("https://api.nasa.gov/earth/earthdata/climate", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/natural-events", methods=["GET"])
def get_natural_events():
    params = {"api_key": NASA_API_KEY, "start_date": "2022-01-01", "end_date": "2022-01-07"}
    data = fetch_data("https://api.nasa.gov/earth/earthdata/natural-event-tracker", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/satellite-data", methods=["GET"])
def get_satellite_data():
    params = {"api_key": NASA_API_KEY, "lon": -74.006, "lat": 40.7128, "date": "2022-01-01"}
    data = fetch_data("https://api.nasa.gov/earth/earthdata/satellite", params)
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data)

# Global error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Global error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Example of handling a custom exception
class APIKeyError(Exception):
    pass

@app.errorhandler(APIKeyError)
def handle_api_key_error(error):
    return jsonify({"error": "Invalid or missing API key"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3030, debug=True)
    
    