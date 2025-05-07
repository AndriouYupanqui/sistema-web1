from models import Producto
from flask import Flask, render_template
###########################
import sqlite3
conexion = sqlite3.connect("copysystems.db",
                           check_same_thread=False)
########################
app = Flask(__name__)

@app.route("/")
def home():
    productos = Producto.get_all(conexion)

    return render_template("index.html", data = {
        "prods": productos
    })

@app.route("/contacto")
def contacto():
    return render_template("contacto.html", data={

    })


@app.route("/iniciose")
def iniciose():
    
        
    return render_template("iniciose.html", data={

    })

@app.route("/detalle")
def detalle():
    
        
    return render_template("detalle.html", data={

    })





if __name__ == "__main__":
    app.run(debug = True)