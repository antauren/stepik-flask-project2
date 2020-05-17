from flask import Flask

app = Flask(__name__)


@app.route('/')
def render_index():
    return 'здесь будет главная'


@app.route('/goals/<goal>/')
def render_goal(goal):
    return 'здесь будет цель {}'.format(goal)


@app.route('/profiles/<profile_id>/')
def render_profile(profile_id):
    return 'здесь будет преподаватель <id учителя> {}'.format(profile_id)


@app.route('/request/')
def render_request():
    return 'здесь будет заявка на подбор'


@app.route('/request_done/')
def render_request_done():
    return 'заявка на подбор отправлена'


@app.route('/booking/<profile_id>/<day>/<time>/')
def render_booking(profile_id, day, time):
    return 'здесь будет форма бронирования <id учителя>'.format(profile_id, day, time)


@app.route('/booking_done/')
def render_booking_done():
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run()
