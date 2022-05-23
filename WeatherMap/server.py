# Import the requests library to be able to SEND requests to servers/API’s.
import requests
# From the flask library, import only the Flask, jsonify and request classes.
# The jsonify class can be used to format your response data into json.
# The request class (not the same as the requests library you imported above) is used to RECEIVE requests from clients.
from flask import Flask, jsonify, request
# From the flask_cors library, import the CORS and cross_origin classes.
# These classes are used to prevent CORS errors.
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")  # Run this method when receiving any POST request
@cross_origin(origin='*')  # Allow requests from any domain
def myMainFunction():
    lat = str(request.args.get("lat"))
    lng = str(request.args.get("lng"))

    url = "https://api.tomorrow.io/v4/timelines"

    querystring = {
        "location": f'{lat}, {lng}',
        "fields": ["temperature", "cloudCover", "windDirection", "windSpeed"],
        "units": "metric",
        "timesteps": "1h",
        "timezone": "Africa/Johannesburg",
        "apikey": "WFW3S3VthhbfWs9p3PlrFRYdl1P7gRQS"}

    response = requests.request("GET", url, params=querystring)
    results = response.json()['data']['timelines'][0]['intervals'][0:12]
    data = jsonify(results)
    return data


if __name__ == "__main__":
    app.run()
