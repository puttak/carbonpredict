#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from werkzeug.utils import secure_filename
import random
"""
This is an initial inplementtion of a REST based API and server for the CCaaS service.
As input the following json format with example values is expected. 
At least the "category-3" feature needs to have a value. Other 
features are optional. Also the ML used in prediction can be selected.
The default ML-model is "xyz".
{
    "brand": "b83",
    "category-1": "womenswear",
    "category-2": "footwear",
    "category-3": "socks",
    "colour": "bondi blue",
    "fabric_type": "K",
    "ftp_acrylic": "21.0",
    "ftp_cotton": "",
    "ftp_elastane": "",
    "ftp_linen": "",
    "ftp_other": "",
    "ftp_polyamide": "43.0",
    "ftp_polyester": "",
    "ftp_polypropylene": "24.0",
    "ftp_silk": "",
    "ftp_viscose": "",
    "ftp_wool": "11.0",
    "gender": "W",
    "label": "",
    "made_in": "VN",
    "season": "",
    "size": "M",
    "unspsc_code": "",
    "weight": "0.029",
    "ML-model": "", 
}

Example usage. 1. Run the server and the api. 2. Call it with curl using wsocks.json file with test input
$ python cpapi.py
$ curl -i -H "Content-Type: application/json" -X POST --data "@wsocks.json" http://localhost:5000/ccaas/api/v0.1/predict
"""

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'json'}

app = Flask(__name__)

@app.route('/ccaas/api/v0.1/predict', methods=['POST'])
def predict():
    if not request.json or not 'category-3' in request.json:
        abort(400)
    
    product = {
    "brand": request.json["brand"],
    "category-1": request.json["category-1"],
    "category-2": request.json["category-2"],
    "category-3": request.json["category-3"],
    "colour": request.json["colour"],
    "fabric_type": request.json["fabric_type"],
    "ftp_acrylic": request.json["ftp_acrylic"],
    "ftp_cotton": request.json["ftp_cotton"],
    "ftp_elastane": request.json["ftp_elastane"],
    "ftp_linen": request.json["ftp_linen"],
    "ftp_other": request.json["ftp_other"],
    "ftp_polyamide": request.json["ftp_polyamide"],
    "ftp_polyester": request.json["ftp_polyester"],
    "ftp_polypropylene": request.json["ftp_polypropylene"],
    "ftp_silk": request.json["ftp_silk"],
    "ftp_viscose": request.json["ftp_viscose"],
    "ftp_wool": request.json["ftp_wool"],
    "gender": request.json["gender"],
    "label": request.json["label"],
    "made_in": request.json["made_in"],
    "season": request.json["season"],
    "size": request.json["size"],
    "unspsc_code": request.json["unspsc_code"],
    "weight": request.json["weight"],
    "ML-model": request.json["ML-model"],  # delaut ML model is xyz
    }

    # load_model(product["ML-model"])
    # CO2E = do_prediction(product["category-3"])

    # This is just here to give a random response until real responses work
    co2e = random.randint(150,666)
    ci = round(co2e/10)
    mean = co2e - 2
    median = co2e - 4
    CO2E = {
        'CO2e': co2e,
        '95% confidence level': ci,
        'mean': mean,
        'median': median
        }
    
    return CO2E, 201


if __name__ == '__main__':
    app.run(debug=True)