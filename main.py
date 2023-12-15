import requests
from flask import Flask, render_template, request

database = 'http://api-hkiot.kazuyosan.my.id:8081/database/history/HKCCTV_DH001/guest_count/get_all'
dated_data = 'http://api-hkiot.kazuyosan.my.id:8081/database/history/HKCCTV_DH001/guest_count/'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    response = requests.get(database)
    data = response.json()
    return render_template('history.html', data=data)

@app.route('/summary/<date>')
def summary(date):
    response = requests.get(dated_data+date)
    data = response.json()

    return render_template('summary.html', data=data, tanggal=date)

if __name__ == "__main__":
    app.run(debug=True)