from flask import Flask, request, jsonify
from iris import IRIS_DATA_URL, load_data, group_sepal_length, describe
from sequence import elem, longest


app = Flask(__name__)
IRIS_DATA = None


@app.route("/sequence/elem", methods=["GET"])
def sequence_elem():
    try:
        return jsonify(elem(int(request.args["n"])))
    except Exception as ex:
        return jsonify(str(ex))


@app.route("/sequence/longest", methods=["GET"])
def sequence_longest():
    try:
        return jsonify(longest(int(request.args["n"])))
    except Exception as ex:
        return jsonify(str(ex))


@app.route("/iris/group/sepal_length", methods=["GET"])
def iris_group_sepal_length():
    try:
        df = group_sepal_length(IRIS_DATA, float(request.args["max"]))
        return df.to_json()
    except Exception as ex:
        return jsonify(str(ex))


@app.route("/iris/describe", methods=["GET"])
def iris_describe():
    try:
        df = describe(IRIS_DATA)
        return df.to_json()
    except Exception as ex:
        return jsonify(str(ex))


def start_service(cfg):
    global IRIS_DATA
    # set global DataFrame containing iris data
    IRIS_DATA = load_data(IRIS_DATA_URL)
    # start HTTP server
    app.run(**cfg)


if __name__ == "__main__":
    # http://127.0.0.1:8080/sequence/elem?n=13
    # http://127.0.0.1:8080/sequence/longest?n=13
    # http://127.0.0.1:8080/iris/group/sepal_length?max=5.8
    # http://127.0.0.1:8080/iris/describe

    start_service(
        {
            "host": "127.0.0.1",
            "port": "8080"
        }
    )
