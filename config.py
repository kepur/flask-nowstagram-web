import os
DEBUG=True
SECRET_KEY=os.urandom(24)
DEBUG=True
DB_USERNAME='root'
DB_PASSWORD="Aa123.com"
DB_HOST="202.182.110.99"
DB_PORT="31789"
DB_NAME="flask-nowstagram"
# PERMANENT_SESSION_LIFETIME=
DB_URI="mysql+pymysql://%s:%s@%s:%s/%s"%(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI=DB_URI
ALLOW_EXT=set(['png','jpg','jpeg','bmp','gif'])
UPLOAD_DIR=''
RUN_HOST='0.0.0.0'
RUN_PORT=8080
UP_DIR=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
FC_DIR=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/users/")