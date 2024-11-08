from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)

# Ruta para calculos aritmeticos
@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    if request.method == 'POST':
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2 if num2 != 0 else 'Infinito'
        return render_template('index.html', total_suma=suma,
                               total_resta=resta,
                               total_multiplicacion=multiplicacion,
                               total_division=division)
    return render_template('index.html')

# Ruta para calculos de longitudes
@app.route('/longitudes', methods=['GET', 'POST'])
def longitudes():
    if request.method == 'POST':
        metros = float(request.form.get('metros'))
        km = metros / 1000
        cm = metros * 100
        pulgadas = metros * 39.3701
        pies = metros * 3.28084
        return render_template('longitudes.html', 
                               metros=metros,
                               total_km=km,
                               total_cm=cm,
                               total_pulgadas=pulgadas,
                               total_pies=pies)
    return render_template('longitudes.html')

# Ruta para calculos de divisas
@app.route('/divisas', methods=['GET', 'POST'])
def divisas():
    tasas_conversion = {
        'USD': 1.0,          # Dolar Americano (Base)
        'EUR': 0.85,         # Euro
        'JPY': 110.0,        # Yen Japones
        'GBP': 0.75,         # Libra Esterlina
        'MXN': 20.0,         # Peso Mexicano
        'COP': 4390.0        # Peso Colombiano
    }

    if request.method == 'POST':
        cantidad = float(request.form.get('cantidad'))
        moneda_origen = request.form.get('moneda_origen')
        moneda_destino = request.form.get('moneda_destino')
        cantidad_en_usd = cantidad / tasas_conversion[moneda_origen]
        cantidad_convertida = cantidad_en_usd * tasas_conversion[moneda_destino]

        return render_template('divisas.html',
                               cantidad=cantidad,
                               moneda_origen=moneda_origen,
                               moneda_destino=moneda_destino,
                               cantidad_convertida=cantidad_convertida,
                               tasas_conversion=tasas_conversion)

    return render_template('divisas.html', tasas_conversion=tasas_conversion)

# Nueva ruta para calculo de fechas
@app.route('/fechas', methods=['GET', 'POST'])
def fechas():
    if request.method == 'POST':
        # Recibimos las fechas desde el formulario
        fecha_inicio_str = request.form.get('fecha_inicio')
        fecha_fin_str = request.form.get('fecha_fin')

        # Convertimos las fechas de string a objeto datetime
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')

        # Calculamos la diferencia en dias
        diferencia_dias = (fecha_fin - fecha_inicio).days

        return render_template('fechas.html',
                               fecha_inicio=fecha_inicio_str,
                               fecha_fin=fecha_fin_str,
                               diferencia_dias=diferencia_dias)
    return render_template('fechas.html')

if __name__ == '__main__':
    app.run(debug=True)
