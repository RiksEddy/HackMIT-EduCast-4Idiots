from flask import Flask,request
import sqlite3

app = Flask(__name__)


def db_connection():
    conn=None
    try:
        conn=sqlite3.connect("lecture_videos.sqlite")
    except sqlite3.error as e :
        print(e)
    return conn



@app.route('/')
def home():
    return 'Home'



if __name__ == '__main__':
    app.run(debug=True)



