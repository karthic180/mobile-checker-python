from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Mobile network coverage data
mobile_data = {
    "Saudi Arabia": {
        "STC": "95%",
        "Mobily": "90%",
        "Zain": "85%",
    },
    "UAE": {
        "Etisalat": "98%",
        "Du": "95%",
    },
    "France": {
        "Orange": "90%",
        "SFR": "85%",
        "Bouygues Telecom": "80%",
        "Free Mobile": "75%",
    },
    "Germany": {
        "Deutsche Telekom": "90%",
        "Vodafone": "85%",
        "O2": "80%",
    },
    "Switzerland": {
        "Swisscom": "98%",
        "Sunrise": "92%",
        "Salt": "85%",
    },
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coverage')
def coverage():
    country = request.args.get('country')
    provider = request.args.get('provider')

    if country and provider:
        country = country.capitalize()
        if country in mobile_data and provider in mobile_data[country]:
            return jsonify({
                'country': country,
                'provider': provider,
                'coverage': mobile_data[country][provider]
            })
        return jsonify({'error': 'Coverage data not found'}), 404

    return jsonify({'error': 'Missing parameters'}), 400

if __name__ == '__main__':
    app.run(debug=True)