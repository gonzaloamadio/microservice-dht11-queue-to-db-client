import os
class Config(object):
    BK_URL = 'postgres://aznyoiqv:1DiWjnHFB_5_u9tgYkK6RC094q-drRmn@tuffi.db.elephantsql.com:5432/aznyoiqv'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', BK_URL)
