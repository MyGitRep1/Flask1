from urllib import request

import app as app
from werkzeug.exceptions import BadRequest


@app.route("/power/")
def power_value():
    x = request.args.get("x") or ""
    y = request.args.get("y") or ""
    if not (x.isdigit() and y.isdigit()):
        app.logger.info("invalid values for power: x=%r and y=%r", x, y)
        raise BadRequest("please pass integers in `x` and `y` query params")
    x = int(x)
    y = int(y)
    result = x ** y
    app.logger.debug("%s ** %s = %s", x, y, result)
    return str(result)


# GET (no values passed) http://127.0.0.1:5000/power/
#  < HTTP/1.0 400 BAD REQUEST
#  - Bad Request
#    please pass integers in `x` and `y` query params
#  [log]: INFO in app: invalid values for power: x='' and y=''

# GET (pass valid data) http://127.0.0.1:5000/power/?x=7&y=3
# < HTTP/1.0 200 OK
# - 343
# [log]: DEBUG in app: 7 ** 3 = 343