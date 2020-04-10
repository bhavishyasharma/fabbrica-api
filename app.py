from flask import Flask
from flask_graphql import GraphQLView
from flask_mongoengine import MongoEngine

from database import init_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'catalyst',
    
}
app.debug = True
db = MongoEngine()

if __name__ == '__main__':
    db.init_app(app)
    from schema import schema
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql',
        schema=schema, graphiql=True))
        
    init_db()
    app.run()