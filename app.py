from flask import Flask
from flask import render_template
from datetime import date

app_instance = Flask(__name__)

@app_instance.route('/')
def index():
    return render_template('index.html', title = 'Home', year=get_year())

@app_instance.route('/about')
def about():
    return render_template('about.html', title='About')

@app_instance.route('/data')
def data():
    return render_template('data.html', title='Data source')

def get_year():
    current_year = date.today().year
    return current_year


if __name__ == '__main__':
    app_instance.run(debug=True)