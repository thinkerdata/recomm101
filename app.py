from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def hello():
    user_id = request.args.get('user_id')
    return jsonify(status="OK", msg=["Apple", "Banana", "Cake"], user=user_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
