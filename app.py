from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Heroe
import os
from werkzeug.utils import secure_filename



# Instancia de la clase Flask de la biblioteca Flask.
app = Flask(__name__)

# Configuramos la base de datos 
    # URL de conexión a la base de datos que SQLAlchemy utilizará para conectarse a la base de datos. 
    # En este caso, se está utilizando una base de datos SQLite,
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    # desactiva el seguimiento de modificaciones por SQLAlchemy. Cuando se establece en False, 
    # le está diciendo a SQLAlchemy que no realice un seguimiento automático de los cambios en los objetos de la DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuramos la carpeta de subida de archivos
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# función llamada allowed_file que toma un parámetro filename, que es el nombre del archivo que se desea comprobar.
def allowed_file(filename):
    # se utiliza para extraer la extensión del archivo y convertirla en minúsculas. Luego, se verifica 
    # si esta extensión está en el conjunto de extensiones permitidas. Si es así, la función devuelve True,
    #  lo que significa que el archivo tiene una extensión permitida; de lo contrario, devuelve False.
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Inicializamos la base de datos
db.init_app(app)

### RUTAS ###

# Ruta principal - Ver heroes
@app.route('/')
def index():

    # Traemos todos los heroes de la base de datos
    heroes = Heroe.query.all() 

    # Renderizamos la plantilla index.html y le pasamos la lista de heroes
    return render_template('index.html', heroes=heroes)

# Ruta Create - Crear
@app.route('/crear', methods=['POST'])
def crear():
    if request.method =='POST':
            
        # Obtener los datos de mi formulario
        nombre = request.form.get('nombre')
        apodo = request.form.get('apodo')
        edad = request.form.get('edad')
        detalles = request.form.get('detalles')

        # Trabajar con la imagen
        file = request.files['foto']

        # Esta línea verifica si se ha enviado un archivo ('file' no es nulo) y si el nombre del archivo es 
        # permitido según la función allowed_file que debe haber sido definida previamente. 
        # Esto se hace para asegurarse de que el archivo que se ha enviado sea válido y seguro.
        if file and allowed_file(file.filename):

            # Esta línea asegura que el nombre del archivo sea seguro, es decir, que no contenga caracteres
            filename = secure_filename(file.filename)

            # Aquí se crea la ruta completa donde se guardará el archivo. Se utiliza la configuración previamente
            #  definida UPLOAD_FOLDER (la carpeta de subida de archivos) y se combina con el nombre de archivo 
            # seguro utilizando os.path.join. Esto establece la ubicación donde se guardará el archivo en el sistema 
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Esta línea guarda físicamente el archivo en la ubicación especificada por file_path. 
            # En otras palabras, está almacenando el archivo en la carpeta de subida de archivos que has configurado.
            file.save(file_path)

            # Aquí, se crea una URL que apunta al archivo recién cargado. La variable foto_url contiene 
            # la URL relativa al archivo de imagen que se ha cargado.
            foto_url = '/static/' + filename  # Save the relative path
        else:
            foto_url = None

        # print(filename)

        # Creamos el objeto de tipo heroe
        heroe = Heroe(nombre=nombre, apodo=apodo, edad=edad, detalles=detalles, foto=foto_url)

        # Agregamos el objeto a la db
        db.session.add(heroe)

        # Guardamos los cambios
        db.session.commit()

        return redirect(url_for('index'))







### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)