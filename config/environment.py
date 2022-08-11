import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/plants_db')
secret = os.getenv('SECRET', 'friendswaffleswork')

# db_URI = os.getenv('DATABASE_URL', 'postgresql')"postgresql://localhost:5432/plants_db"
# secret = "friendswaffleswork"