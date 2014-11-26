from flask.ext.sqlalchemy import SQLAlchemy

from deadlines.app import app


db = SQLAlchemy(app)


class Schedule(db.Model):

    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)


class Task(db.Model):

    __tablename__ = 'schedules'

    # This translates to a package that would be installed and some
    # entrypoint defined in the package.
    # For example, a setup.py of a packages with tasks might be:
    #
    #  setup(...
    #      entry_points={
    #          'deadlines.tasks': [
    #              'snapshot = pangaea.etls.postgres.tasks:Snapshot',
    #              'sorted_chunk = pangaea.etls.postgres.tasks:SortedChunk',
    #              'dated_chunk = pangaea.etls.postgres.tasks:DatedChunk',
    #           ]
    #      }
    #  )
    #
    # Deadlines server can see if the package,
    # "pangaea.etls>=3.4,<4.0" for example, has been installed and
    # install it when necessary in order to run it.

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    package = db.Column(db.String)
    namespace = db.Column(db.String)
    installed = db.Column(db.Boolean, default=False)
