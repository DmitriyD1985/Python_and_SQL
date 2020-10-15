from sqlite3 import DatabaseError
from dbConnection import makeConnection


def addService(title, price):
    connection = makeConnection()
    cursor = connection.cursor()
    if cursor.execute("""Select title from services_hist where title = ?;""", (title,)).fetchone() is None:
        try:
            max_number_service_id = cursor.execute\
                ("""Select service_id from services_hist ORDER BY service_id DESC limit 1""").fetchone()
            if max_number_service_id is None:
                cursor.execute("""INSERT INTO services_hist (service_id, title, price) VALUES(?, ?, ?)""",
                               (1, title, price))
                connection.commit()
            else:
                cursor.execute("""INSERT INTO services_hist (service_id, title, price) VALUES	(?, ?, ?)""",
                               (max_number_service_id[0]+1, title, price))
                connection.commit()
                return "service inserted"
        except DatabaseError as exc:
            print('failed INSERT 41', exc)
        finally:
            connection.close()
    else:
        try:
            cursor.execute("""UPDATE services_hist SET end_dttm = CURRENT_TIMESTAMP  WHERE title = ?""", (title,))
            max_number_service_id = cursor.execute\
                ("""Select service_id from services_hist where title = ?;""", (title,)).fetchone()[0]
            new_service_id = max_number_service_id
            cursor.execute("""INSERT INTO services_hist (service_id, title, price) VALUES (?, ?, ?);""",
                           (new_service_id, title, price))
            connection.commit()
            return "updated"
        except DatabaseError as exc:
            print('failed UPDATE', exc)
        finally:
            connection.close()


def addClient(name, lastname):
    connection = makeConnection()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO contact_groups (name, lastname) VALUES(?, ?);""",
                                           (name, lastname))
        return "user added"
    except DatabaseError as exc:
        print('Adding client is failed', exc)
    finally:
        connection.commit()
        connection.close()


def addOrdersString(service_id, client_id):
    connection = makeConnection()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO orders (service_id, client_id) VALUES	(?, ?);""",
                                           (service_id, client_id))
        return "order added"
    except DatabaseError as exc:
        print('Adding order is failed', exc)
    finally:
        connection.commit()
        connection.close()


def setDeleteClient(id):
    connection = makeConnection()
    cursor = connection.cursor()
    try:
        cursor.execute("""UPDATE contact_groups SET deleted_flg = 1  WHERE id = ?""", (id,))
        return f"User with id - {id} mark as deleted"
    except DatabaseError as exc:
        print('Deleting user is failed', exc)
    finally:
        connection.commit()
        connection.close()


def restoreDeletedClient(id):
    connection = makeConnection()
    cursor = connection.cursor()
    try:
        cursor.execute("""UPDATE contact_groups SET deleted_flg = NULL  WHERE id = ?""", (id,))
        return f"User with id - {id} restored"
    except DatabaseError as exc:
        print('Restoring user is failed', exc)
    finally:
        connection.commit()
        connection.close()


def getTable(name):
    connection = makeConnection()
    cursor = connection.cursor()
    try:
        datatable = cursor.execute(f"SELECT * FROM {name}").fetchall()
        for row in datatable:
            print(row)
    except DatabaseError as exc:
        print('Getting table is failed', exc)
    finally:
        connection.commit()
        connection.close()


def createTable(script):
    connection = makeConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(script)
        return "Table created"
    except DatabaseError as exc:
        print('Table create is failed', exc)
    finally:
        connection.commit()
        connection.close()


def dropView(name):
    connection = makeConnection()
    cursor = connection.cursor()
    cursor.execute(f"DROP VIEW IF EXISTS {name};")


def dropTAble(name):
    connection = makeConnection()
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {name};")