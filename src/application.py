from flask import Flask, Response, request
from datetime import datetime
import json
from reservation_resource import ReservationResource
from flask_cors import CORS
from datetime import datetime

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.route("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...

    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/api/reservations/", methods=["GET"])
def get_all_reservation():
    result = ReservationResource.get_all_reservation()
    print(result)
    if result:
        rsp = Response(json.dumps(result, default = str), status=200, content_type="application.json") # set default = str, otherwise result not json serializable
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/reservations/<phone>", methods=["GET"])
def get_reservation_by_phone(phone):
    result = ReservationResource.get_reservation_by_phone(phone)
    print(result)
    if result:
        rsp = Response(json.dumps(result, default = str), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/reservations/<phone>/<table_id>", methods=["PUT"])
def reserve_table_by_phone(phone, table_id):
    print(request.method)
    print(phone, table_id)
    current = datetime.now()

    result = ReservationResource.create_reservation(phone, table_id, current)
    print(result)
    if result:
        rsp = Response("Success on inserting for {}".format(phone), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/reservations/<phone>/<table_id>/delete", methods=["DELETE"])
def delete_table_by_phone(phone, table_id):

    result = ReservationResource.delete_reservation(phone, table_id)
    print(result)
    if result:
        rsp = Response("Success on deleting for {}".format(phone), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5011)

