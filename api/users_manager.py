import sqlite3

class UsersManager(object):

    @staticmethod
    def get_all_users():
        """
        This function responds to a request for /api/users/
        with the complete lists of people

        :return: sorted list of people
        """
        with sqlite3.connect("user.db") as con:
            con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
            cur = con.cursor()
            cur.execute("""SELECT * FROM users""")
            return cur.fetchall()

    @staticmethod
    def add_user(name, surname, age):
        with sqlite3.connect("user.db") as con:
            con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
            cur = con.cursor()
            cur.execute("""INSERT INTO users(name, surname, age) VALUES("%s",
            "%s", %s)""" % (name, surname, age))
            con.commit()

    @staticmethod
    def fetch_user(user_id):
        with sqlite3.connect("user.db") as con:
            con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
            cur = con.cursor()
            cur.execute("""SELECT * FROM users WHERE ID = %s""" % user_id)
            return cur.fetchone()

    @staticmethod
    def remove_user(user_id):
        with sqlite3.connect("user.db") as con:
            con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
            cur = con.cursor()
            cur.execute("""DELETE FROM users WHERE ID = %s""" % user_id)
            con.commit()

    @staticmethod
    def update_user(user_id, user_data):
        name = user_data.get("name")
        surname = user_data.get("surname")
        age = user_data.get("age")
        query = """UPDATE users SET """
        if name is not None:
            query += """name = "%s" """ % name

        if surname is not None:
            query += """surname = "%s" """ % surname

        if age is not None:
            query += """age = %s """ % age

        query += """ WHERE id = %s""" % user_id
        with sqlite3.connect("user.db") as con:
            con.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
            cur = con.cursor()
            print(query)
            cur.execute(query)
            con.commit()
