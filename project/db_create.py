# project/db_create.py

from views import db
from models import Task, User
from datetime import date

#create the database and the db table
# initialize the database schema
db.create_all()

# insert data
# db.session.add(Task('Finish the tutorial', date(2016,12,31), 10, 1))
# db.session.add(Task('Finish Real python', date(2017,1,1), 10, 1))
# db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, 1))
# db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, 1))

#commit the changes
db.session.commit()
