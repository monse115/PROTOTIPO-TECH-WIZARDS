from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/temas')
def temas():
    return render_template('temas.html')

@app.route('/juego')
def juego():
    return render_template('juego.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None  # Inicializa el mensaje de error como nulo

    if request.method == 'POST':
        matricula = request.form.get('id_login')
        password = request.form.get('contra')

        if matricula == '1319313107' and password == '123456':
            # Matrícula y contraseña válidas, redirige a la página de juegos
            return redirect(url_for('temas'))
        else:
            # Matrícula o contraseña incorrectas, establece el mensaje de error
            error_message = 'Matrícula o contraseña incorrectas'

    return render_template('login.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
