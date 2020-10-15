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