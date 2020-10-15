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
    CREATE VIEW services 
    AS 
    SELECT
    title,
    client_name,
    client_lastname,
    price,
    FROM
    services_hist
    INNER JOIN orders ON orders.service_id = services_hist.service_id
    INNER JOIN contact_groups ON contact_groups.id = orders.client_id
    where contact_groups.deleted_flg = 0 and services_hist.end_dttm is null
"""

services_stat = """
    CREATE VIEW services 
    AS 
    SELECT
    title,
    price,
    count(orders.id)
    FROM
    services_hist
    INNER JOIN orders ON orders.service_id = services_hist.service_id
    ROUP BY orders.id
"""