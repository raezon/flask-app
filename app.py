from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    # Vulnérabilité XSS : Insertion de données non filtrées dans la réponse JSON
    user_input = request.args.get('user_input', '')
    return jsonify({'message': f'Hello, {user_input}!'})  # XSS possible si l'input n'est pas filtré

@app.route('/api/info')
def info():
    # Erreur intentionnelle : fuite d'informations sur la version de l'application
    return jsonify({'application': 'Simple Python Flask App', 'version': '1.0'})

@app.route('/api/data')
def data():
    # Mauvaise pratique : Paramètre non validé pour une requête de données (injection SQL simulée)
    query = request.args.get('query', '')  # Pas de validation sur la donnée
    data = [1, 2, 3, 4, 5]
    return jsonify({'data': data, 'query': query})  # Potentielle vulnérabilité d'injection SQL si utilisé dans une base de données

@app.route('/api/secret')
def secret():
    # Mauvaise pratique : Données sensibles exposées sans authentification
    return jsonify({'secret': 'This is a secret message! Access is not restricted.'})

# Activation de l'affichage des erreurs (mauvaise pratique)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error', 'message': str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070, debug=True)  # 'debug=True' expose des détails sur les erreurs
