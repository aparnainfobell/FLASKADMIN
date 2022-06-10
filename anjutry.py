import psycopg2
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash

dbase = psycopg2.connect(
    host='localhost',
    dbname='server_management',
    user='postgres',
    password='tomandjerry',
    port=5432
)
app = Flask(__name__)
mycursor = dbase.cursor()


@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    User_ID = _json['User_ID']
    print(User_ID, "USERR")
    Email_ID = _json['Email_ID']
    Password = _json['Password']
    ROle = _json['ROle']
    Team_ID = _json['Team_ID']
    _hashed_password = generate_password_hash(Password)

    if User_ID and Email_ID and Password and ROle and Team_ID and request.method == 'POST':
        sql = "INSERT INTO USER_TABLE(User_ID, Email_ID, Password, ROle, Team_ID) VALUES(%s, %s, %s, %s, %s)"
        data = (User_ID, Email_ID, _hashed_password, ROle, Team_ID)
        mycursor.execute(sql, data)
        dbase.commit()
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return "not found"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
