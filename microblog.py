from app import app, db, cli
from app.models import User, Post


# for testing in the shell interpreter
# all imports and db will be available using >>$ flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}