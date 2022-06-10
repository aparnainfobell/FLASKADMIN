import psycopg2
import os
from flask import Flask,request

currentlocation = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


class Server_manage:
    def create_database(self):
        base = psycopg2.connect(
            host='localhost',
            database ='postgres',
            user='postgres',
            password='tomandjerry',
            port=5432
        )
        base.autocommit = True
        # creating database
        cursor = base.cursor()
        cursor.execute("DROP DATABASE IF EXISTS server_management")
        cursor.execute("CREATE DATABASE server_management")
        cursor.close()




s = Server_manage()
s.create_database()


# @myapp.route('/register',methods = ["GET","POST"])
# def registration():
#     if request.method == "POST":


# import pymysql
# from app import app
# from db import mysql
# from flask import jsonify
# from flask import flash, request
# # from werkzeug import generate_password_hash, check_password_hash
# from werkzeug.security import generate_password_hash, check_password_hash
#
#
# @app.route('/add', methods=['POST'])
# def adding():
#     try:
#         _json = request.json
#         _name = _json['name']
#         _email = _json['email']
#         _password = _json['pwd']
#         if _name and _email and _password and request.method == 'POST':
#             sql = "INSERT INTO SERVER_table(user_name, user_email, user_password) VALUES(%s, %s, %s)"
#             data = (_name, _email, _password,)
#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.execute(sql, data)
#             resp = jsonify('User added successfully!')
#             return resp
#         else:
#             return pass
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#
#
# @app.route('/users')
# def users():
#     conn = None
#     cursor = None
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT user_id id, user_name name, user_email email, user_password pwd FROM tbl_user")
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
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute(
#             "SELECT user_id id, user_name name, user_email email, user_password pwd FROM tbl_user WHERE user_id=%s", id)
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
#         _id = _json['id']
#         _name = _json['name']
#         _email = _json['email']
#         _password = _json['pwd']
#         # validate the received values
#         if _name and _email and _password and _id and request.method == 'PUT':
#             # do not save password as a plain text
#             _hashed_password = generate_password_hash(_password)
#             # save edits
#             sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
#             data = (_name, _email, _hashed_password, _id,)
#             conn = mysql.connect()
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
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
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