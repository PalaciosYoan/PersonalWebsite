from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/roommate-compatibility')
def portfolio_details():
    return render_template('roommate-compatibility.html')

@app.route('/pipeline-simulator')
def pipeline_simulator():
    return render_template('pipeline-simulator.html')

@app.route('/super-mario-bros-troll')
def super_mario():
    return render_template('super-mario-troll-level.html')

@app.route('/personal-website')
def personal_website():
    return render_template('personal-website.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)