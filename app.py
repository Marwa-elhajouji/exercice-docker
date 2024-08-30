import os
from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST', 'db')
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER','root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASSWORD','password')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DB','flaskdb')
mysql = MySQL()
mysql.init_app(app)
@app.route('/')
def index():
 cur = mysql.get_db().cursor()
 cur.execute("SHOW TABLES")
 result = cur.fetchall()
 return str(result)
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)