import sqlite3

ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts