from flask import Flask, render_template
from data import teachers, goals, days_of_week

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/goals/<goal>/')
def render_goal(goal):
    return render_template('goal.html')


@app.route('/profiles/<int:profile_id>/')
def render_profile(profile_id):
    return render_template('profile.html', profile=teachers[profile_id], goals=goals, days_of_week=days_of_week)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/')
def render_request_done():
    return render_template('request_done.html')


@app.route('/booking/<int:profile_id>/<day>/<time>/')
def render_booking(profile_id, day, time):
    return render_template('booking.html', profile=teachers[profile_id], day=day, time=time, days_of_week=days_of_week)


@app.route('/booking_done/')
def render_booking_done():
    return render_template('booking_done.html')


if __name__ == '__main__':
    app.run(debug=True)
