from flask import Flask
from flask import render_template
import  sqlite3
from flask import request


app = Flask(__name__, static_url_path='/static')

    

@app.route('/')
def hello_world(name=None):

    conn = sqlite3.connect('database/productos.db')
    curr = conn.cursor()
    curr.execute("SELECT nombre, precio, tienda, url  FROM productos")
    test = curr.fetchall()
    
    return render_template('principal.html', name=name, test=test)
    conn.close()
    
    
    
@app.route('/tabla' , methods=["POST"])
def tabla(name=None):

     if request.method == 'POST':
     
        producto = request.form['producto']
     
        conn = sqlite3.connect('database/productos.db')
        curr = conn.cursor()
        curr.execute('SELECT nombre, precio, tienda, url  FROM productos WHERE nombre LIKE ? ', ('%'+producto+'%',))
        test = curr.fetchall()
        
       
        return render_template('principal.html', name=name, test=test)
        conn.close()