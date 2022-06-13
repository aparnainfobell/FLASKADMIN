from flask import jsonify
from flask import Flask, request
import psycopg2
import uuid
import psycopg2.extras
from psycopg2.extras import RealDictCursor


# from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash

Team_ID = str(uuid.uuid1())
print(Team_ID,"TEAMMM")

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_user():
    # dbase = psycopg2.connect(
    #     host='localhost',
    #     dbname='server_management',
    #     user='postgres',
    #     password='tomandjerry',
    #     port=5432
    # )
    # dbase.autocommit = True
    # cursor = dbase.cursor()
    #
    # conn = None
    # cursor = None
    # try:
    _json = request.json
    # print(_json,"uuuu")
    User_ID = _json['User_ID']
    # print(User_ID,"USERR")
    Email_ID = _json['Email_ID']
    Password = _json['Password']
    ROle = _json['ROle']
    # Team_ID = _json['Team_ID']
    # validate the received values
    if User_ID and Email_ID and Password and ROle and Team_ID and request.method == 'POST':
        _hashed_password = generate_password_hash(Password)
        # save edits
        # conn = dbase.connect()
        # cursor = conn.cursor()
        # cursor = dbase.cursor()
        sql = "INSERT INTO USER_TABLE(User_ID, Email_ID, Password, ROle, Team_ID) VALUES(%s, %s, %s, %s, %s)"
        # print(sql,"sqll")
        data = (User_ID, Email_ID, _hashed_password, ROle, Team_ID)
        # print(data,"dataa")
        conn = psycopg2.connect(
            host='localhost',
            dbname='server_management',
            user='postgres',
            password='tomandjerry',
            port=5432
        )
        # print(conn,"conn")
        cursor = conn.cursor()
        # print(cursor,"currr")
        cursor.execute(sql, data)
        # print(cursor.execute(sql, data),"gggggg")
        conn.commit()
        # cursor.execute(sql, data)
        resp = jsonify('User added successfully!')
        # print(resp,"respp")
        resp.status_code = 200
        return resp

    else:
       return "not found"

    #         cursor.execute(sql, data)
    #         dbase.commit()
    #         resp = jsonify('User added successfully!')
    #         resp.status_code = 200
    #         return resp
    #     else:
    #         return 'not found'
    # except Exception as e:
    #     print(e)
    # finally:
    #     cursor.close()
        # conn.close()


@app.route('/users')
def users():
    # conn = None
    # cursor = None
    # try:
        conn =  psycopg2.connect(
            host='localhost',
            dbname='server_management',
            user='postgres',
            password='tomandjerry',
            port=5432
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        # print(cursor,"kkkk")
        cursor.execute("SELECT User_ID, Email_ID, Password, ROle, Team_ID pwd FROM USER_TABLE")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    # except Exception as e:
    #     print(e)
    # finally:
    #     cursor.close()
    #     conn.close()


@app.route('/user/<int:id>')
def user(id):
    # conn = None
    # cursor = None
    # try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='server_management',
            user='postgres',
            password='tomandjerry',
            port=5432
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print(cursor,"currrrs")
        # id=request.args.get(id=id)
    #
    # cursor.execute("SELECT user_id id, user_name name, user_email email,"
    #                " user_password pwd FROM tbl_user WHERE user_id=%s",
    #                id)

        cursor.execute(
            "SELECT User_ID User_ID, Email_ID Email_ID, Password Password, ROle ROle,"
            " Team_ID Team_ID  FROM USER_TABLE WHERE User_ID=%s",id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    # except Exception as e:
    #     print(e)
    # finally:
    #     cursor.close()
    #     conn.close()
#
#
@app.route('/update', methods=['PUT'])
def update_user():
    # conn = None
    # cursor = None
    # try:
        _json = request.json
        print(_json,"jsonn")
        User_ID = _json['name']
        Email_ID = _json['email']
        Password = _json['pwd']
        ROle = _json['role']
        Team_ID = _json['teamid']
        # validate the received values
        if User_ID and Email_ID and Password and ROle and Team_ID and request.method == 'PUT':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(Password)
            # save edits
            sql = "UPDATE USER_TABLE SET User_ID=%s, Email_ID=%s, Password=%s, ROle=%s,Team_ID=%s WHERE User_ID=%s"
            print(sql,"sqlll")
            data = (User_ID, Email_ID, _hashed_password, ROle, Team_ID)
            conn = psycopg2.connect(
            host='localhost',
            dbname='server_management',
            user='postgres',
            password='tomandjerry',
            port=5432
              )
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return ("Not found")
    # except Exception as e:
    #     print(e)
    # finally:
    #     cursor.close()
    #     conn.close()
#
#
# @app.route('/delete/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     conn = None
#     cursor = None
#     try:
#         conn = mycursor.connect()
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM USER_TABLE WHERE User_ID=%s", (id,))
#         conn.commit()
#         resp = jsonify('User deleted successfully!')
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
#
#
# @app.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'status': 404,
#         'message': 'Not Found: ' + request.url,
#     }
#     resp = jsonify(message)
#     resp.status_code = 404
#
#     return resp


if __name__ == "__main__":
    app.run()


