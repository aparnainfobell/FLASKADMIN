from flask import jsonify
from flask import Flask, request
import psycopg2

# from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_user():
    dbase = psycopg2.connect(
        host='localhost',
        dbname='server_management',
        user='postgres',
        password='tomandjerry',
        port=5432
    )
    dbase.autocommit = True
    cursor = dbase.cursor()

    conn = None
    #cursor = None
    try:
        _json = request.json
        User_ID = _json['name']
        Email_ID = _json['email']
        Password = _json['pwd']
        ROle = _json['role']
        Team_ID = _json['teamid']
        # validate the received values
        if User_ID and Email_ID and Password and ROle and Team_ID and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(Password)
            # save edits

            # conn = dbase.connect()
            # cursor = conn.cursor()

            cursor = dbase.cursor()

            sql = "INSERT INTO USER_TABLE(User_ID, Email_ID, Password, ROle, Team_ID) VALUES(%s, %s, %s, %s, %s)"
            data = (User_ID, Email_ID, _hashed_password, ROle, Team_ID)

            cursor.execute(sql, data)
            dbase.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return 'not found'
    except Exception as e:
        print(e)
    # finally:
    #     cursor.close()
        # conn.close()


# @app.route('/users')
# def users():
#     conn = None
#     cursor = None
#     try:
#         conn = mycursor.connect()
#         cursor = conn.cursor(psycopg2.cursors.DictCursor)
#         cursor.execute("SELECT User_ID, Email_ID, Password, ROle, Team_ID pwd FROM USER_TABLE")
#         rows = cursor.fetchall()
#         resp = jsonify(rows)
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
#
#
# @app.route('/user/<int:id>')
# def user(id):
#     conn = None
#     cursor = None
#     try:
#         conn = mycursor.connect()
#         cursor = conn.cursor(psycopg2.cursors.DictCursor)
#         cursor.execute(
#             "SELECT User_ID, Email_ID, Password, ROle, Team_ID pwd FROM USER_TABLE WHERE User_ID=%s",
#             id)
#         row = cursor.fetchone()
#         resp = jsonify(row)
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
#
#
# @app.route('/update', methods=['PUT'])
# def update_user():
#     conn = None
#     cursor = None
#     try:
#         _json = request.json
#         User_ID = _json['name']
#         Email_ID = _json['email']
#         Password = _json['pwd']
#         ROle = _json['role']
#         Team_ID = _json['teamid']
#         # validate the received values
#         if User_ID and Email_ID and Password and ROle and Team_ID and request.method == 'PUT':
#             # do not save password as a plain text
#             _hashed_password = generate_password_hash(Password)
#             # save edits
#             sql = "UPDATE USER_TABLE SET User_ID=%s, Email_ID=%s, Password=%s, ROle=%s,Team_ID=%s WHERE User_ID=%s"
#             data = (User_ID, Email_ID, _hashed_password, ROle, Team_ID)
#             conn = mycursor.connect()
#             cursor = conn.cursor()
#             cursor.execute(sql, data)
#             conn.commit()
#             resp = jsonify('User updated successfully!')
#             resp.status_code = 200
#             return resp
#         else:
#             return not_found()
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()
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