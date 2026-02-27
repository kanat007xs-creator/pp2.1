import json

with open("instrac.json","r") as f:
    instrac=json.load(f)
with open("students.json","r") as f:
    students=json.load(f)
result = []

for t in instrac:
    t_kurs = t["kurs"]
    
    sov= []
    
    for student in students:
        if student["kurs"] == t_kurs:
            sov.append(student["name"])
    
    if sov:
        result.append({
            "teacher": t["name"],
            "course": t_kurs,
            "students": sov
        })

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

