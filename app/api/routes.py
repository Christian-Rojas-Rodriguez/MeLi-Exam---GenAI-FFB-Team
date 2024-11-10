from flask import Blueprint, request, jsonify
from app.services.mutant_service import check_mutant, get_stats

api_bp = Blueprint('api', __name__)

@api_bp.route('gcloud app deploy', methods=['POST'])
def mutant_check():
    data = request.get_json()
    dna = data.get("dna", [])
    if check_mutant(dna):
        return jsonify({"message": "Mutant detected"}), 200
    else:
        return jsonify({"message": "Not a mutant"}), 403

@api_bp.route('/stats', methods=['GET'])
def stats():
    stats_data = get_stats()
    return jsonify(stats_data)
