import sqlite3


conn=sqlite3.connect('lecture_videos.db')
c=conn.cursor()

'''c.execute("""CREATE TABLE lecture_videos(
    grade integer
    course text
    link text
    done text         
)""")
'''

conn.commit()
conn.close()
