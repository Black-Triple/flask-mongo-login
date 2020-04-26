from flask_script import Manager
from server import app
import createDBSchema

manager = Manager(app)


@manager.command
def create_db():
    createDBSchema.create_mongodb_schema()


if __name__ == '__main__':
    manager.run()
