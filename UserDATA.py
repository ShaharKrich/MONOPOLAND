import sqlite3


class Users:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

    def __init__(self, tablename="users", userId="userId", password="password", username="username", email="email"):
        self.__tablename = tablename
        self.__userId = userId
        self.__password = password
        self.__username = username
        self.__email = email
        conn = sqlite3.connect('MONO.db')
        print("Opened database successfully")

        query_str = f"CREATE TABLE IF NOT EXISTS {tablename} ({self.__userId} INTEGER PRIMARY KEY AUTOINCREMENT , " \
                    f"{self.__password} TEXT    NOT NULL , " \
                    f"{self.__username} TEXT    NOT NULL, " \
                    f"{self.__email} TEXT NOT NULL UNIQUE);"

        # conn.execute("Create table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def insert_user(self, username, password, email):
        """Gets a new user's data and adds it to the database."""

        conn = sqlite3.connect('MONO.db')
        insert_query = f"INSERT INTO {self.__tablename} ({self.__username},{self.__password},{self.__email}) VALUES ('{username}','{password}','{email}'); "
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def select_user_by_id(self, userId):
        conn = sqlite3.connect('MONO.db')
        print("Opened database successfully")
        str1 = "select * from users;"

        """strsql = "SELECT userId, username, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(userId)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("userId = ", row[0])
            print("username = ", row[1])
            print("password = ", row[2])

        print("Operation done successfully")
        conn.close()

    def delete_user_by_id(self, userId):
        """Gets user's id and deletes the user from the database.
        *NOTE: If the user id is not in the database, the function does nothing."""

        conn = sqlite3.connect('MONO.db')
        delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__userId} = {userId};"
        print(delete_query)
        conn.execute(delete_query)
        conn.commit()
        conn.close()
        print("user deleted successfully")

    def update_users_password_by_id(self, userId, password=None):
        """Gets user's id and new password. The function updates the user's password.
        *NOTE: If the user id is not in the database, or if the password is None, the function does nothing."""

        if password is not None:
            conn = sqlite3.connect('MONO.db')
            delete_query = f"UPDATE {self.__tablename} SET {self.__password} = ? WHERE {self.__userId} = ?;"
            print(delete_query)
            conn.execute(delete_query, (password, userId))
            conn.commit()
            conn.close()
            print("password updated successfully")
        else:
            print("password did not changed. password must not be None.")

class Players:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

    def __init__(self, tablename="Players", character="character", money = "money", properties="properties", doubles="doubles"):
        self.__tablename = tablename
        self.__character = character
        self.__money = money
        self.__properties = properties
        self.__doubles = doubles
        conn = sqlite3.connect('PLAYERS.db')
        print("Opened database successfully")

        query_str = f"CREATE TABLE IF NOT EXISTS {tablename} ({self.__userId} INTEGER PRIMARY KEY AUTOINCREMENT , " \
                    f"{self.__password} TEXT    NOT NULL , " \
                    f"{self.__username} TEXT    NOT NULL, " \
                    f"{self.__email} TEXT NOT NULL UNIQUE);"

        # conn.execute("Create table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def add_money(self, username, password, email):
        """Gets a new user's data and adds it to the database."""

        conn = sqlite3.connect('PLAYERS.db')
        insert_query = f"INSERT INTO {self.__tablename} ({self.__username},{self.__password},{self.__email}) VALUES ('{username}','{password}','{email}'); "
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def select_user_by_id(self, userId):
        conn = sqlite3.connect('PLAYERS.db')
        print("Opened database successfully")
        str1 = "select * from users;"

        """strsql = "SELECT userId, username, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(userId)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("userId = ", row[0])
            print("username = ", row[1])
            print("password = ", row[2])

        print("Operation done successfully")
        conn.close()

    def delete_user_by_id(self, userId):
        """Gets user's id and deletes the user from the database.
        *NOTE: If the user id is not in the database, the function does nothing."""

        conn = sqlite3.connect('PLAYERS.db')
        delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__userId} = {userId};"
        print(delete_query)
        conn.execute(delete_query)
        conn.commit()
        conn.close()
        print("user deleted successfully")

    def update_users_password_by_id(self, userId, password=None):
        """Gets user's id and new password. The function updates the user's password.
        *NOTE: If the user id is not in the database, or if the password is None, the function does nothing."""

        if password is not None:
            conn = sqlite3.connect('PLAYERS.db')
            delete_query = f"UPDATE {self.__tablename} SET {self.__password} = ? WHERE {self.__userId} = ?;"
            print(delete_query)
            conn.execute(delete_query, (password, userId))
            conn.commit()
            conn.close()
            print("password updated successfully")
        else:
            print("password did not changed. password must not be None.")


def main():
    u = Users()

    # insert 3 users
    u.insert_user('user1', 'pass1', 'emailfsdfsdf1y78')
    u.insert_user('user2', 'pass2', 'emailadfhs2')
    u.insert_user('user3', 'pass3', 'emailsfzfgsfg3')

    # delete the user whose id is 2
    u.delete_user_by_id(2)

    # update the password of the user whose id is 1
    u.update_users_password_by_id(1, 'newpass1')
    u.select_user_by_id(3)


if __name__ == '__main__':
    main()
