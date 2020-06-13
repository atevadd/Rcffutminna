from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#configirations
from backend.config.config import app, db

#models
from backend.models.user import User


#setting up migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)




if __name__ == "__main__":
    manager.run()