from flask import Flask, request, jsonify, render_template, redirect
import webbrowser

app = Flask(__name__)

# Updated broadband coverage data for 2026
broadband_data = {
    "Saudi Arabia": {
        "STC": "90%",
        "Mobily": "85%",
        "Zain": "80%",
    },
    "UAE": {
        "Etisalat": "92%",
        "Du": "85%",
    },
    "France": {
        "Orange": "85%",
        "SFR": "80%",
        "Bouygues Telecom": "78%",
        "Free Mobile": "70%",
    },
    "Germany": {
        "Deutsche Telekom": "88%",
        "Vodafone": "80%",
        "O2": "83%",
    },
    "Switzerland": {
        "Swisscom": "90%",
        "Sunrise": "85%",  # Updated data
        "Salt": "80%",
    },
}

# Provider coverage map URLs for 2026 (real-time link)
coverage_map_urls = {
    "STC": "https://www.stc.com.sa/coverage-map",
    "Mobily": "https://www.mobily.com.sa/coverage-map",
    "Zain": "https://www.sa.zain.com/en/coverage-map",
    "Etisalat": "https://www.etisalat.ae/en/coverage-maps.jsp",
    "Du": "https://www.du.ae/en/coverage",
    "Orange": "https://www.orange.fr/coverage",
    "SFR": "https://www.sfr.fr/couverture-mobile",
    "Bouygues Telecom": "https://www.bouyguestelecom.fr/coverage",
    "Free Mobile": "https://www.free.fr/coverage",
    "Deutsche Telekom": "https://www.telekom.de/coverage",
    "Vodafone": "https://www.vodafone.de/hilfe/ueberblick/netz-und-coverage.html",
    "O2": "https://www.o2online.de/tarife/o2-netz/abdeckung/",
    "Swisscom": "https://www.swisscom.ch/en/residential/mobile/coverage-map.html",
    "Sunrise": "https://www.sunrise.ch/en/residential/mobile/network-coverage.html",
    "Salt": "https://www.salt.ch/en/mobile-network/"
}

@app.route('/')
def index():
    # Render the index.html from the templates folder
    return render_template('index.html')

@app.route('/coverage', methods=['GET'])
def get_coverage():
    country = request.args.get('country')
    provider = request.args.get('provider')

    # Check if country and provider are provided
    if not country or not provider:
        return jsonify({"error": "Missing country or provider"}), 400

    # Capitalize country and provider to match the keys in the dictionary
    country = country.capitalize()
    provider = provider.capitalize()

    # Check if country exists in the broadband data
    country_data = broadband_data.get(country)

    if country_data:
        # Check if provider exists in the specified country
        coverage = country_data.get(provider)
        if coverage:
            coverage_map_url = coverage_map_urls.get(provider)
            message = f"Coverage for {provider} in {country}: {coverage}. Check the coverage map: {coverage_map_url}"

            # Auto-redirect the user to the coverage map
            return redirect(coverage_map_url)

    return jsonify({
        "error": "Data not found",
        "message": "This is a simulated data source, please refer to real-world APIs for live data."
    }), 404

# Auto-open the browser when the Flask app starts
def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    # Launch the browser automatically
    open_browser()
    app.run(debug=True)