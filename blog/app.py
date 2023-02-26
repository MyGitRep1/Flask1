from flask import Flask, request

app = Flask(__name__)


@app.route("/status/", methods=["GET", "POST"])
def custom_status_code():
    if request.method == "GET":
        return """\
        To get response with custom status code
        send request using POST method
        and pass `code` in JSON body / FormData
        """
    print("raw bytes data:", request.data)
    if request.form and "code" in request.form:
       return "code from form", request.form["code"]
    if request.json and "code" in request.json:
        return "code from json", request.json["code"]
    return "", 204


# GET
# > curl --request GET --url http://127.0.0.1:5000/status/
# - To get response with custom status code
#  send request using POST method
#  and pass `code` in JSON body / FormData

# POST (empty body)
# > curl --request POST --url http://127.0.0.1:5000/status/
# < HTTP/1.0 204 NO CONTENT

# POST (multipart/form-data)
#  > curl --request POST --url http://127.0.0.1:5000/status/ \
#    --header 'Content-Type: multipart/form-data' \
#    --form code=202
#  < HTTP/1.0 202
#  - code from form

# POST (json)
#  > curl --request POST --url http://127.0.0.1:5000/status/ \
#    --header 'Content-Type: application/json' \
#    --data '{"code": 205}'
#  < HTTP/1.0 205 RESET CONTENT
#  - code from json