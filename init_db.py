from modelos import db, Heroe
from flask import Flask 

# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Crear tablas en la base de datos
with app.app_context():
    db.create_all()

# Cargamos los datos en la base de datos
with app.app_context():

    ### cargar Casas ###
    heroe_1 = Heroe(nombre='Iron Man', apodo='Genio, multimillonario, playboy, filántropo', edad=35, detalles='Líder de los Vengadores, fundador de Stark Industries', foto='/static/iron_man.png')
    heroe_2 = Heroe(nombre='Thor', apodo='Dios del Trueno', edad=1500, detalles='Príncipe de Asgard, miembro de los Vengadores', foto='/static/thor.png')

    ### Agregar a la base de datos ###
    db.session.add(heroe_1)
    db.session.add(heroe_2)

    # Guardar cambios
    db.session.commit()
