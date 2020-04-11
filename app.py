from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

from database import init_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'fabbrica',
    
}
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400
jwt = JWTManager(app)
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    roles = []
    for role in user.roles:
        roles.append(role.name)
    return {"roles": roles}
app.debug = True
db = MongoEngine()
cors = CORS(app)

if __name__ == '__main__':
    db.init_app(app)
    from schema import schema
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql',
        schema=schema, graphiql=True))
        
    init_db()
    app.run()