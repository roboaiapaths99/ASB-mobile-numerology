from flask import Flask, request, jsonify, make_response
from datetime import datetime
import sys
import os
import requests as http_requests
from functools import wraps
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the parent directory to the path to import mobile_numerology
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mobile_numerology.consultation import NumerologyConsultation

app = Flask(__name__)

# Load config from env
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "asb_store")
MERN_AUTH_BASE_URL = os.getenv("MERN_AUTH_BASE_URL", "https://api.asbcrystal.in")
ENABLE_CREDIT_SYSTEM = os.getenv("ENABLE_CREDIT_SYSTEM", "false").lower() == "true"

# Initialize MongoDB client
db_client = MongoClient(MONGODB_URI) if MONGODB_URI else None
db = db_client[DB_NAME] if db_client else None

def check_credits(user_id, cost=1):
    if db is None:
        return True
    try:
        user = db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return False
        # If user has a credits field, check it. Otherwise default to 10 credits for testing
        credits = user.get("credits", 10)
        return credits >= cost
    except Exception as e:
        print(f"Credit check error: {e}")
        return True # fail open during DB errors

def deduct_credits(user_id, cost=1):
    if db is None:
        return
    try:
        db.users.update_one({"_id": ObjectId(user_id)}, {"$inc": {"credits": -cost}})
    except Exception as e:
        print(f"Credit deduction error: {e}")

def verify_token_with_mern(token):
    """Validate token by calling the MERN auth service (api.asbcrystal.in).
    Returns (user_id, error_message). user_id is None on failure."""
    try:
        resp = http_requests.get(
            f"{MERN_AUTH_BASE_URL}/api/auth/me",
            headers={
                "Authorization": f"Bearer {token}",
                "X-Auth-Token": token,
            },
            timeout=8
        )
        data = resp.json()
        if resp.status_code == 200 and data.get("success"):
            user = data.get("user", {})
            user_id = str(user.get("_id") or user.get("id") or "")
            return user_id or "unknown", None
        return None, data.get("message", "Unauthorized")
    except Exception as e:
        return None, f"Auth service unreachable: {e}"

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Allow preflights
        if request.method == 'OPTIONS':
            return f(*args, **kwargs)

        token = None
        # 1. Authorization header
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        # 2. X-Auth-Token header
        if not token:
            token = request.headers.get("X-Auth-Token")

        security_bypass = os.getenv("SECURITY_BYPASS", "0") == "1"

        # No token at all
        if not token or token in ("null", "undefined"):
            if security_bypass:
                request.user_id = "000000000000000000000000"
                return f(*args, **kwargs)
            return jsonify({"error": "Unauthorized: Access token is missing"}), 401

        # Validate token via MERN auth service
        user_id, err = verify_token_with_mern(token)
        if not user_id:
            # If bypass is on, allow anyway (dev mode)
            if security_bypass:
                request.user_id = "000000000000000000000000"
                return f(*args, **kwargs)
            return jsonify({"error": f"Unauthorized: {err}"}), 401

        request.user_id = user_id

        # Check credits if credit system is enabled
        if ENABLE_CREDIT_SYSTEM:
            if not check_credits(request.user_id, cost=1):
                return jsonify({"error": "Insufficient credits. Please recharge your wallet."}), 402

        return f(*args, **kwargs)
    return decorated

# ── CORS: handle preflight and inject headers on every response ──────────────
@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response()
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Auth-Token'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Auth-Token'
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
@require_auth
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

        # Success, deduct credits if credit system enabled
        if ENABLE_CREDIT_SYSTEM:
            deduct_credits(request.user_id, cost=1)

        return jsonify(api_response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting ASB Numerology Backend API...")
    print("API will be available at: http://localhost:5002")
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule}")
    app.run(debug=False, host='0.0.0.0', port=5002, use_reloader=False)
