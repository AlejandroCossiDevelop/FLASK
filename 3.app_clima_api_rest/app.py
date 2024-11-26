from flask import Flask, render_template, request  # Importar las librerías necesarias
import requests  # Importar la librería requests para realizar peticiones a la API

app = Flask(__name__)  # Crear una instancia de la aplicación Flask

# API Key proporcionada por OpenWeatherMap
API_KEY = 'cc4552b5d77473ae40bc4cc76bbc1fd9'

@app.route('/', methods=['GET', 'POST'])  # Ruta principal que acepta métodos GET y POST
def index():
    weather_data = []  # Lista para almacenar los datos del clima
    if request.method == 'POST':  # Verificar si el formulario fue enviado
        ciudad = request.form['ciudad']  # Obtener el valor ingresado en el campo 'ciudad'
        city_list = [city.strip() for city in ciudad.split(',')]  # Separar las ciudades por comas

        for city in city_list:  # Iterar sobre cada ciudad ingresada
            # Construir la URL de la API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
            response = requests.get(url)  # Realizar la solicitud a la API

            if response.status_code == 200:  # Si la respuesta es exitosa
                data = response.json()  # Convertir la respuesta en formato JSON
                weather = {  # Extraer los datos relevantes
                    'city': data['name'],  # Nombre de la ciudad
                    'temperature': data['main']['temp'],  # Temperatura actual
                    'description': data['weather'][0]['description'],  # Descripción del clima
                    'feels_like': data['main']['feels_like'],  # Sensación térmica
                    'temp_min': data['main']['temp_min'],  # Temperatura mínima
                    'temp_max': data['main']['temp_max'],  # Temperatura máxima
                    'icon': data['weather'][0]['icon']  # Icono del clima
                }
                weather_data.append(weather)  # Agregar los datos a la lista
            else:
                # En caso de error, agregar un mensaje indicando que no se pudo obtener el clima
                weather_data.append({'city': city, 'error': 'No se pudo obtener el clima.'})

    return render_template('index.html', weather_data=weather_data)  # Renderizar la plantilla HTML

if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo de depuración
