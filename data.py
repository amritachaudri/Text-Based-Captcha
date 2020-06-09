import sqlite3 
conn = sqlite3.connect('example.db')
c = conn.cursor() 
#c.execute('''CREATE TABLE cdata (name text, Mobileno text, age real)''')
#c.execute("INSERT INTO cdata VALUES ( 'A','0987654321',19)")
#c.execute("INSERT INTO cdata VALUES ( 'B','9999955555',20)")
#c.execute("INSERT INTO cdata VALUES ( 'C','9999955555',21)")
#c.execute("INSERT INTO cdata VALUES ( 'D','5555577777',21)")
#c.execute("INSERT INTO cdata VALUES ( 'E','4444433333',22)")
d=c.execute("SELECT * FROM cdata")
print(d.fetchall())
conn.commit() 
  
