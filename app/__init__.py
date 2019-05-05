from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/events.html")
def events():
    return render_template('events.html')

@app.route("/transportation.html")
def transportation():
    return render_template('transportation.html')

@app.route("/hotels.html")
def hotels():
    return render_template('hotels.html')

@app.route("/cuisine.html")
def cuisine():
    return render_template('cuisine.html')

@app.route("/faq.html")
def faq():
    return render_template('faq.html')

@app.route("/history.html")
def history():
    return render_template('history.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/pictures.html")
def pictures():
    return render_template('pictures.html')
