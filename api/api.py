from flask import render_template
from db.connector import connector, cursor
from http import HTTPAPI
import connexion

## Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
#app.add_api('swagger.yml')

def create_database(conn, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
            name varchar(20) NOT NULL, surname varchar(20) NOT NULL, age integer)""")
    conn.commit()

def get_users():
    """
    This function responds to a request for /api/users/
    with the complete lists of people

    :return: sorted list of people
    """
    return {}
    #cursor.execute("""SELECT name, surname, age FROM users""")
    #return cursor.fetchall()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return: the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    create_database(connector, cursor)
    api = HTTPAPI()
    api()
    #app.run(host='0.0.0.0', port=5000, debug=True)
