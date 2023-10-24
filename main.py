import requests
from flask import Flask, render_template

database = 'http://api-hkiot.kazuyosan.my.id:8081/database/history/HKCCTV_DH001/guest_count/get_all'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    response = requests.get(database)
    data = response.json()
    return render_template('history.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)