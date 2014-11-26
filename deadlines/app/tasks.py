from deadlines.app import app


@app.route('/api/tasks/', methods=['GET'])
def list_tasks():
    pass
