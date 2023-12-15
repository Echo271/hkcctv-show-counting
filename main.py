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

@app.route('/summary')
def summary():
    params = request.args.get('date')
    response = requests.get(dated_data+'08_12_2023')
    data = response.json()
    
    jam = []
    masuk = []
    keluar = []
    total_masuk = 0
    total_keluar = 0
    
    for item in data:
        if item.isdigit():
            jam.append(item)
            masuk.append(data[item]['in'])
            keluar.append(data[item]['out'])
        else:
            total_masuk = data[item]['in']
            total_keluar = data[item]['out']

    return render_template('summary.html', masuk=masuk, keluar=keluar, total_masuk=total_masuk, total_keluar=total_keluar)

if __name__ == "__main__":
    app.run(debug=True)