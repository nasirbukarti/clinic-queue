from flask import Flask, render_template, request, redirect, url_for
from models import Patient

app = Flask(__name__)

queue = []
served_count = 0

@app.route('/')
def index():
    return render_template('index.html', queue=queue, count=served_count)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            patient = Patient(name)
            queue.append(patient)
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/serve')
def serve_patient():
    global served_count
    if queue:
        queue.pop(0)  # FIFO
        served_count += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)