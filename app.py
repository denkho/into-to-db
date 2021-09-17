from database import Database
from user import User


Database.initialise(database="youdatabasename", user="yourusername", password="yourpassword", host="localhost")

my_user = User('jude@jsmith.com', 'Jude', 'Smith', None)

my_user.save_to_db()

user_email = User.load_from_db_by_email("email@bk.ru")
print(user_email)



