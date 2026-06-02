from flask import Flask, request, jsonify, make_response
from datetime import datetime
import sys
import os

# Add the parent directory to the path to import mobile_numerology
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mobile_numerology.consultation import NumerologyConsultation

app = Flask(__name__)

# ── CORS: handle preflight and inject headers on every response ──────────────
@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response()
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Numerology Backend API', 'status': 'running'})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.route('/api/numerology/consultation', methods=['POST', 'OPTIONS'])
def generate_consultation():
    try:
        data = request.get_json()

        if not data or not data.get('name') or not data.get('dob') or not data.get('mobile'):
            return jsonify({'error': 'Missing required fields: name, dob, mobile'}), 400

        dob_str = data['dob']
        if isinstance(dob_str, str) and '-' in dob_str:
            date_obj = datetime.strptime(dob_str, '%Y-%m-%d')
            dob_str = date_obj.strftime('%d/%m/%Y')

        consultation = NumerologyConsultation(
            name=data['name'],
            dob=dob_str,
            mobile_number=data['mobile'],
            challenges=data.get('challenges', '')
        )

        results = consultation.generate_consultation_report()

        api_response = {
            'client_info': results['client_info'],
            'moolank': results['moolank'],
            'bhagyank': results['bhagyank'],
            'classification': results['classification'],
            'pair_analysis': results['pair_analysis'],
            'final_result': results['final_result'],
            'interpretation': results['interpretation'],
            'remedies': results['remedies']
        }

        return jsonify(api_response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting ASB Numerology Backend API...")
    print("API will be available at: http://localhost:5001")
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule}")
    app.run(debug=False, host='0.0.0.0', port=5001, use_reloader=False)
