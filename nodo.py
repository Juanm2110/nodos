import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/comunicacion')
def comunicacion():
    try:
        # Llamada a nodo2 usando su nombre en la red de Docker
        response = requests.get('http://nodo2:8080')
        return jsonify({'respuesta': response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error al intentar comunicarse con nodo2: {str(e)}'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
