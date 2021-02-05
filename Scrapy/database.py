import  sqlite3

conn = sqlite3.connect('productos.db')
curr = conn.cursor()


#curr.execute("""create table  productos(
#             nombre text,
#             tienda  text, 
#             categoria text,
#             precio text
#             )""")
 
curr.execute(""" INSERT INTO productos VALUES ('tele','mansion','teles','280.340')  """) 

 
conn.commit()
conn.close() 