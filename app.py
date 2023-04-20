from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Anaylst',
    'location': 'Mumbai',
    'salary': '1 crores'
  },
  {
    'id': 2,
    'title': 'Data Anaylst',
    'location': 'Mumbai',
    'salary': '1 crores'
  },
  {
    'id': 3,
    'title': 'Data Anaylst',
    'location': 'Mumbai',
    'salary': '1 crores'
  },
  {
    'id': 4,
    'title': 'Data Anaylst',
    'location': 'Powai',
    'salary': '1 crores'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="NSB")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
