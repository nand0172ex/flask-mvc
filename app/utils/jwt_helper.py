from flask_jwt_extended import jwt_required, get_jwt_identity

def admin_required(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        # Logic to check admin role
        return fn(*args, **kwargs)
    return wrapper
