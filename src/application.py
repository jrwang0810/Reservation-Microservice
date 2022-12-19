from flask import Flask, Response, request
from datetime import datetime
import json
import requests
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
        rsp = Response(json.dumps(result, indent=4, sort_keys=True, default=str), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/reservations/<email>", methods=["GET"])
def get_reservation_by_email(email):
    result = ReservationResource.get_reservation_by_email(email)
    print(result)
    if result:
        rsp = Response(json.dumps(result, indent=4, sort_keys=True, default=str), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/reservations/<email>/<table_id>", methods=["PUT"])
def reserve_table_by_email(email, table_id):
    print(request.method)
    print(email, table_id)
    current = datetime.now()
    year = current.year
    month = current.month
    day = current.day
    # current = "2022-01-05"
    # year = 2022
    # month = 1
    # day = 5
    token = "477ad380984d434598e1a0c5f3c998b1"
    response = requests.get(
        "https://holidays.abstractapi.com/v1/?api_key={}&country=US&year={}&month={}&day={}".format(token,year,month,day))
    print(response.status_code)
    print(response.content)
    data = json.loads(response.content)
    if not data:
        result = ReservationResource.create_reservation(email, table_id, current)
        print(result)
        if result:
            rsp = Response("Success on inserting for {}".format(email), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    else:
        rsp = Response("Public Holiday: {}".format(data[0]["name"]), status=404, content_type="text/plain")
    return rsp

@app.route("/api/reservations/<email>/<table_id>/delete", methods=["DELETE"])
def delete_table_by_email(email, table_id):

    result = ReservationResource.delete_reservation(email, table_id)
    print(result)
    if result:
        rsp = Response("Success on deleting for {}".format(email), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/reservations/delete", methods=["DELETE"])
def delete_all_table():

    result = ReservationResource.delete_all_reservation()
    print(result)
    if not result:
        rsp = Response("Success on deleting for all", content_type="application.json")
    else:
        rsp = Response("some error occurs", status=404, content_type="text/plain")
    return rsp

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5011)

