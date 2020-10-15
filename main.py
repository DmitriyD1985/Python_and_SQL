from creationScriptsSQL import tableHistory, tableOrders, tableContact, viewServices, services_stat
from serviceMethods import createTable, getTable, addClient, addOrdersString, addService, setDeleteClient, \
    restoreDeletedClient, dropView, dropTAble

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
