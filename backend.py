import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY, date text, earning integer, exercise text, study text, diet text, python text)")
    conn.commit()
    conn.close()

def insert(date, earning, exercise, study, diet, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL, ?,?,?,?,?,?)",(date, earning, exercise, study, diet, python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?",(id, ))
    conn.commit()
    conn.close()

def search(date = '', earning = '', exercise='', study='', diet='', python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earning=? OR exercise=? OR study=? OR diet=? OR python=?", (date,earning,exercise,study,diet,python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#insert('15/09/2022', 200, 'did not exercise', 'have studied', 'diet not taken','did python')
#print(view())
connect()