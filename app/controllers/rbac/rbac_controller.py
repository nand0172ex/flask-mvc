from flask import Blueprint, request, jsonify
from app import db
from app.models.rbac.role import Role

rbac_bp = Blueprint('rbac', __name__)

@rbac_bp.route('/roles', methods=['POST'])
def create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    return jsonify({"message": "Role created successfully!"}), 201
