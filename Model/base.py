from flask import Flask
from peewee import *

app = Flask(__name__)
db = MySQLDatabase('junction_hackathon_2023', host="localhost", port=3306, user='root', passwd='629220')


@app.before_request
def _db_connect():
    db.connect()


# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


class BaseModel(Model):
    class Meta:
        database = db
