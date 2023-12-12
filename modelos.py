from flask_sqlalchemy import SQLAlchemy

# Crear objeto SQLAlchemy
db = SQLAlchemy()

### MODELOS ###

# nullable=False: no puede ser nulo
# nullable=True: puede ser nulo

# Crear modelo de la tabla Casas
class Heroe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apodo = db.Column(db.String(30), nullable=True)
    edad = db.Column(db.Integer, nullable=False)
    detalles = db.Column(db.String(500), nullable=False)
    foto = db.Column(db.String(30), nullable=True)

