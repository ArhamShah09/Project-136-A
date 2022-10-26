from flask import Flask, jsonify, request

from data import data

app = Flask(__name__)
@app.route("/sundata")

def planet_data() :
    name = request.args.get("name")
    sun_info = next(item for item in data if item["name"] == name)
    return jsonify({
        "data" : sun_info,
        "message" : "success"
    }), 200

if __name__ == "__main__":
    app.run()