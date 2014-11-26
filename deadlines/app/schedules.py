from flask import jsonify

from deadlines import models
from deadlines.app import app


@app.route('/api/schedules/', methods=['GET'])
def list_schedules():
    schedules = models.Schedule.query.all()
    return jsonify(schedules)
