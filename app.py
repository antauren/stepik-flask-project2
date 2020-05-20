from flask import Flask, render_template, request
from data import teachers, goals, days_of_week

from handler import update_booking_data

app = Flask(__name__)
app.secret_key = 'REPLACE_ME'


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


@app.route('/booking_done/', methods=['GET', 'POST'])
def render_booking_done():
    name = request.form.get('clientName')
    phone = request.form.get('clientPhone')
    day = request.form.get('clientWeekday')
    time = request.form.get('clientTime')
    profile_id = request.form.get('clientTeacher')

    if request.method != "POST":
        return 'Error'

    data = {'name': name,
            'profile_id': profile_id,
            'phone': phone,
            'day': day,
            'time': time
            }
    update_booking_data(data)

    return render_template('booking_done.html', name=name, phone=phone, day=days_of_week[day], time=time)


if __name__ == '__main__':
    app.run(debug=True)
