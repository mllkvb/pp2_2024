import psycopg2 as ps

sql = """
INSERT INTO phonebook VALUES(DEFAULT, %s, %s);
"""

conn = ps.connect(host='localhost',
                  dbname='postgres',
                  user='postgres',
                  password='1892',
                  port='1892'
                  )

cur = conn.cursor()

banned = []
while True:
    print("Want to enter a person's data? yes/no")
    mode = input()
    if mode == "no":
        break
    person = input().split()
    if len(person) > 2:
        banned.append(person)
        continue
    if not person[1].isdigit():
        banned.append(person)
        continue
    cur.execute(sql, (person[0], person[1]))

conn.commit()

cur.close()
conn.close()