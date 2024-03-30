from flask import Flask, jsonify, render_template, jsonify

app = Flask(__name__)

INTERESTS = [{
    "id": 1,
    "Job Role": "AI Engineer",
    "Company": "Google"
}, {
    "id": 2,
    "Job Role": "Data Scientist",
    "Company": "Amazon"
}, {
    "id": 3,
    "Job Role": "ML Engineer",
    "Company": "Microsoft"
}, {
    "id": 4,
    "Job Role": "Data Analyst",
    "Company": "Microsoft"
}, {
    "id": 5,
    "Job Role": "Data Engineer",
    "Company": "IBM"
}, {
    "id": 6,
    "Job Role": "Data Scientist",
    "Company": "Facebook"
}]


@app.route("/")
def hw():
  return render_template('homebs.html', ints=INTERESTS)


@app.route("/api/ints")
def list_ints():
  return jsonify(INTERESTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
