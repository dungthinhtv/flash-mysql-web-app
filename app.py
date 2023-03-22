from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Sala town',
    'salary': '2000$'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Sala town',
    'salary': '2000$'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Sala town',
    'salary': '2000$'
  },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(debug=True)
