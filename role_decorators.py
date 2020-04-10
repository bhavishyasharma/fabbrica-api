from functools import wraps
from flask import jsonify
from flask_jwt_extended import ( verify_jwt_in_request, get_jwt_claims )
from flask_jwt_extended.exceptions import NoAuthorizationError

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        print("Hahahaha")
        if 'admin' not in claims['roles']:
            print("Blaha Blah")
            raise NoAuthorizationError("Permission Denied!")
        else:
            return fn(*args, **kwargs)
    return wrapper