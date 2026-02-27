import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + " " + "-" * 8 + " " + "-" * 6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))





#1
import json

data = '{"name": "Kanat", "age": 18}'

result = json.loads(data)

print(result)
print(result["name"])
#2
import json

person = {
    "name": "Kanat",
    "age": 18
}

json_string = json.dumps(person)

print(json_string)
#3
{
  "city": "Almaty",
  "population": 2000000
}
import json

with open("example.json", "r") as file:
    data = json.load(file)

print(data["city"])
#4
import json

data = '''
{
    "students": [
        {"name": "Aruzhan", "grade": 90},
        {"name": "Dias", "grade": 85}
    ]
}
'''

result = json.loads(data)

for student in result["students"]:
    print(student["name"], student["grade"])
#5
import json

data = '''
{
    "products": [
        {"name": "Phone", "price": 500},
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 25}
    ]
}
'''

result = json.loads(data)

for product in result["products"]:
    if product["price"] > 100:
        print(product["name"])
#6
import json

data = {
    "users": [
        {"name": "Kanat", "active": True}
    ]
}

data["users"].append({"name": "Aliya", "active": False})

with open("users.json", "w") as file:
    json.dump(data, file, indent=4)
#7
import json

data = '''
{
    "orders": [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 250},
        {"id": 3, "amount": 150}
    ]
}
'''

result = json.loads(data)

total = 0
for order in result["orders"]:
    total += order["amount"]

print("Total:", total)
#8
import json

data = '''
{
    "company": {
        "departments": [
            {
                "name": "IT",
                "employees": [
                    {"name": "Kanat", "salary": 1000},
                    {"name": "Aruzhan", "salary": 1200}
                ]
            },
            {
                "name": "HR",
                "employees": [
                    {"name": "Dias", "salary": 900}
                ]
            }
        ]
    }
}
'''

result = json.loads(data)

for dept in result["company"]["departments"]:
    print("Department:", dept["name"])
    for emp in dept["employees"]:
        print(" ", emp["name"], emp["salary"])
    
#9
import json
date={
    "name": "alice" ,
    "age" : "25" ,
    "city" : "ny"
}
json_string=json.dumps(date)
print(json_string)
#output
{"name":"alice","age":"25","city":"ny"}

#10
with open("date.json","r") as file:
    data=json.
        

