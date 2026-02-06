a={'kanat':98,'askar':80,'aibyn ':92,'beka':69,'ali':86,'alina':77,'mina':71}
for key,value in a.items():
    if value>=95 and value<=100:
        print(key,"gpa:4.0")
    elif value>=90 and value<=94:
        print(key,"gpa:3.67")
    elif value>=85 and value<=89:
        print(key,"gpa:3.33")
    elif value>=80 and value<=84:
        print(key,"gpa:3.0")
    elif value>=75 and value<=79:
        print(key,"gpa:2.67")
    elif value>=70 and value<=74:
        print(key,"gpa:2.33")
    else:
        print(key,"no stepuha")