import json

some_dict = {
    986325: ('Liam', 43),
    475368: ('Noah', 35),
    958634: ('Lydia', 23),
    456278: ('James', 28),
    443215: ('Sam', 14),
    186327: ('Olivia', 31)
}

with open('example.json', 'w') as file:
    json.dump(some_dict, file)
