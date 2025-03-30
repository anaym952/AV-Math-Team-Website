from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html')



@app.route("/team")
def team():
    return render_template('team.html')
    


@app.route("/achievements")
def achievements():
    return render_template('achievements.html')



@app.route("/events")
def events():
    return render_template('events.html')



if __name__ == "__main__":
    app.run(debug=True)