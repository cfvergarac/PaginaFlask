# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import  sqlite3

class TutorialPipeline(object):

    def __init__(self):
       self.create_conection()
       #self.delete_table()
       #self.create_table()
       
    def create_conection(self):
      self.conn = sqlite3.connect('productos.db')
      self.conn.text_factory = str
      self.curr = self.conn.cursor()
      
    def create_table(self):
      #self.curr.execute(""" DROP TABLE IF EXISTS productos  """)
      self.curr.execute("""create table  productos(
             nombre text,
             tienda  text, 
             categoria text,
             precio text,
             url    text
             )""")
             
    def delete_table(self):
       self.curr.execute(""" DELETE FROM productos  """)
       
       
    def update_table(self, item):
       self.curr.execute(""" UPDATE productos SET precio = ? WHERE nombre = ?  """,(
        item['precio'],
        item['nombre']
        ))   
       
       self.conn.commit()
    
    
    def process_item(self, item, spider):
        self.update_table(item)
        self.storeDB(item)
        return item

    def storeDB(self, item):
        self.curr.execute(""" INSERT INTO productos VALUES (?,?,?,?,?)  """,(
        item['nombre'],
        item['tienda'],       
        item['categoria'],
        item['precio'],
        item['url']
        ))
    
        self.conn.commit()
        
    
    
    
    
     