from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#configirations
from main_app import app, db

#models
from main_app.models import Message


#setting up migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)




if __name__ == "__main__":
    manager.run()