from serviceMethods import createTable, getTable, addClient, addOrdersString, addService, setDeleteClient, \
    restoreDeletedClient, dropView, dropTAble

tableHistory = """CREATE TABLE IF NOT EXISTS services_hist(
   id INTEGER primary key autoincrement,
   service_id INTEGER,
   title varchar(125),
   price REAL,
   start_dttm timestamp DEFAULT CURRENT_TIMESTAMP,
   end_dttm timestamp DEFAULT (datetime('2999-12-31 23:59:59'))
)"""

tableOrders = """CREATE TABLE IF NOT EXISTS orders(
   id INTEGER primary key autoincrement,
   service_id INTEGER,
   dttm timestamp DEFAULT CURRENT_TIMESTAMP,
   client_id INTEGER
)"""

tableContact = """CREATE TABLE IF NOT EXISTS contact_groups(
   id INTEGER primary key autoincrement,
   name varchar(125),
   lastname varchar(125) ,
   deleted_flg INTEGER DEFAULT NULL
)"""

viewServices = """
    CREATE VIEW IF NOT EXISTS services
    AS
    SELECT
        title,
        price,
        lastname,
        name
    from
    (
       SELECT
        distinct(title),
        price,
        orders.service_id,
        orders.client_id
    from services_hist
    LEFT JOIN orders on services_hist.service_id = orders.service_id
    where services_hist.end_dttm = datetime('2999-12-31 23:59:59')
    ) as clientService
    LEFT JOIN contact_groups on contact_groups.id = clientService.client_id

"""

services_stat = """
    CREATE VIEW IF NOT EXISTS servicesstat
    AS
    SELECT
        services_hist.title, count(distinct(orders.id)) from services_hist left JOIN orders ON orders.service_id = services_hist.service_id
        group by services_hist.title
"""

dropTAble('services_hist')
dropTAble('orders')
dropTAble('contact_groups')

# Creating three table
print('Creating three table')
createTable(tableHistory)
createTable(tableOrders)
createTable(tableContact)

# Input date in table Service_hist
print('Input date in table Service_hist')
print(addService("Sevice1", "1.11"))
print(addService("Sevice2", "2.22"))
print(addService("Sevice3", "3.33"))

# Input date in table client_group
print('Input date in table client_group')
print(addClient('Client1', 'Clientov'))
print(addClient('Client2', 'Ivanov'))
print(addClient('Client3', 'Petrov'))

# Add orders
print('Add orders')
print(addOrdersString(1, 1))
print(addOrdersString(2, 1))
print(addOrdersString(1, 3))

# Print all tables
print('Print all tables')
print("services_hist")
getTable("services_hist")
print("orders")
getTable("orders")
print("contact_groups")
getTable("contact_groups")

print("Add service with exist name but another price")
print(addService("Sevice1", "4.44"))
print("services_hist")
getTable("services_hist")

print("Delete client with id 1")
print(setDeleteClient(1))
print("contact_groups")
getTable("contact_groups")
print("Restore client with id 1")
restoreDeletedClient(1)
print("contact_groups")
getTable("contact_groups")

print("Create view services")
dropView('services')
createTable(viewServices)
getTable("services")

print("Create view servicesstat")
dropView('servicesstat')
createTable(services_stat)
getTable("servicesstat")
