from flask import Flask
from flask import jsonify
import requests
import datetime as dt


app = Flask(__name__)


@app.route('/urlaggregator', methods=['GET'])

def urlaggregator():
    url1 = "http://www.apnapaisa.com/personal-loan/interest-rates"
    url2 = "https://www.paisabazaar.com/personal-loan/"
    url3 =  "https://indialends.com/personal-loan"
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    json_data = {"url1": response1.text, "url2": response2.text, "url3": response3.text, "processedTime": f"{dt.datetime.now().date()}"}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True)


