from flask import Flask, render_template, jsonify
# from database import load_jobs_from_db, load_job_from_db, add_application_to_db

import os

APP_NAME = os.getenv('APP_NAME')

app = Flask(__name__)

@app.context_processor
def inject_app_name():
    return dict(app_name=APP_NAME)

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

def find(arr , id):
    for x in arr:
        if x["id"] == id:
            return x


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):  
  job = find(JOBS , int(id))
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', 
                         job=job)

  

if __name__ == '__main__':
  app.run(debug=True)
