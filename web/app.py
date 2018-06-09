from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

# Init flask object
app = Flask(__name__)

# Config flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flasksqluser:flasksqlpw@sqldb/flasksqldb'
app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskmongodb',
    'host': 'mongo',
    'port': 27017
}

# Init extensions
sqldb = SQLAlchemy(app)
mongo = MongoEngine(app)
redis = Redis(host='redis', port=6379)

# Define sql model
class SQLUser(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    username = sqldb.Column(sqldb.String(80), unique=True, nullable=False)

# Define mongo document
class MongoUser(mongo.Document):
    username = mongo.StringField(required=True)

# Runs before first request to '/'
@app.before_first_request
def set_up():
    # Do sql op
    sqldb.drop_all()
    sqldb.create_all()
    admin = SQLUser(username="sql_user")
    sqldb.session.add(admin)
    sqldb.session.commit()

    # Init mongo
    MongoUser.objects().delete()
    MongoUser(username="mongo_user").save()

    # Write to redis
    redis.set('foo', 'bar')

@app.route('/')
def hello_user():
    sql_user = SQLUser.query.first()
    mongo_user = MongoUser.objects.first()
    return 'SQL User: {0} Mongo User: {1} Redis: {2}'.format(sql_user.username, mongo_user.username, redis.get('foo'))

if __name__ == "__main__":
    # Only for debugging while developing
    app.run('0.0.0.0', 5000, debug=True)