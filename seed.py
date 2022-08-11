# Differences: Our seed file knows about Flask, and SQLAlchemy
# Our previous project the seed file did not know about Express
from app import app, db
from models.plant_data import plants_list, comments_list
from models.user_data import user_list 

# This basically ensures app and db are ready for use, and it
# provides 'scope' were I can access the app/db

with app.app_context():
  # try/catch in python is try/except
    try:
        print('Oh, hello!')
        db.drop_all() # Removing everything from the db
        db.create_all() # This will create the TABLES in the db

        print("Seeding your data!")

        db.session.add_all(user_list) # Seeding my users
        db.session.commit()

        db.session.add_all(plants_list) # Add a list of things to the db
        db.session.commit() # Add, commit. Like Git.


        # # * This has to come after making the characters (above) because you need the characters to comment on.
        db.session.add_all(comments_list)
        db.session.commit()

        print("😘")

    except Exception as e:
        print(e)