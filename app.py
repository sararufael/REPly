
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destination',methods=['POST'])
def repinformation():
    address = request.form['address']
    data = requests.get('https://www.googleapis.com/civicinfo/v2/representatives?address='+address+'&key=AIzaSyByalwgte_IJ-iClnTKSJVdWv7dxhIdLhU')
    reps_json = data.json()
    user_info = reps_json['normalizedInput']
# index order: US Senator, US Senator, US Representative, State Senator, State Representative
    officials_list = [reps_json['officials'][0],reps_json['officials'][2],reps_json['officials'][3],reps_json['officials'][4],reps_json['officials'][7],reps_json['officials'][8]]
    return render_template('destination.html', officials_list=officials_list)

@app.route('/representative')
def representative():
    return render_template('representative.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resources')
def resources():
    return render_template('blog.html')

@app.route('/issue')
def issue():
    return render_template('issue.html')


if __name__ == '__main__':
    app.run()
