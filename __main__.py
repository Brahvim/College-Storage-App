import os

import magic
from flask import *

s_fsdir = "./files/"
s_app = Flask("Storage App")
s_magic = magic.Magic(mime=True)


@s_app.route("/", methods=["GET"])
def get_index():
    response = make_response("Hello! :D")
    # res.headers["Content-Type"] = "text/plain"
    return response


@s_app.route("/storage", methods=["GET", "PUT", "DELETE"])
def post_index():
    method = request.method
    speed = request.args["speed"]

    try:
        speed = int(speed)
    except ValueError:
        speed = 8192  # 8 KiB at once

    path = os.path.join(s_fsdir, request.args["path"])

    if method == "GET":

        if not os.path.exists(path):
            return "No such file", 404

        def generator():
            with open(path) as file:
                while chunk := file.read(speed):
                    yield chunk

        fname = os.path.basename(path)
        mimetype = s_magic.from_file(path) or "application/octet-stream"
        headers = {"Content-Disposition": f"attachment; filename={fname}"}
        return Response(generator(), mimetype=mimetype, headers=headers)

    elif method == "PUT":

        return make_response("")

    elif method == "DELETE":

        return make_response("")


s_app.run(debug=True)
