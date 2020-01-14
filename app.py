from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

#database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
#  dbuser=os.environ['DBUSER'],
#  dbpass=os.environ['DBPASS'],
#  dbhost=os.environ['DBHOST'],
#  dbname=os.environ['DBNAME']
#)

database_uri = 'postgresql+psycopg2://aznyoiqv:1DiWjnHFB_5_u9tgYkK6RC094q-drRmn@tuffi.db.elephantsql.com:5432/aznyoiqv'

app = Flask(__name__)

app.config.update(
  SQLALCHEMY_DATABASE_URI=database_uri,
  SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

#initialize the database connection
db = SQLAlchemy(app)

@app.route('/')
def view_registered_weathers():
  from models import Weather
  weathers = Weather.query.all()
  return render_template('weather.html', weathers=weathers)

if __name__ == '__main__':
  app.run()
