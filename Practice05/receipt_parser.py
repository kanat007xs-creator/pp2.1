import re
import json

with open("Practice05/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1
prices = re.findall(r'\d+\s?x\s([\d\s,]+)', text)
prices = [p.replace(" ", "") for p in prices]

# 2
products = re.findall(r'\d+\.\n(.+)', text)

# 3
total_match = re.search(r'ИТОГО:\s*([\d\s,]+)', text)
total = total_match.group(1).replace(" ", "") if total_match else None

# 4
datetime_match = re.search(r'Время:\s*([\d\.]+\s[\d:]+)', text)
datetime = datetime_match.group(1) if datetime_match else None

# 5
payment_match = re.search(r'(Банковская карта|Наличные)', text)
payment = payment_match.group(1) if payment_match else None

# 
result = {
    "products": products,
    "prices": prices,
    "total_amount": total,
    "datetime": datetime,
    "payment_method": payment
}


with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

# 1
task1 = re.findall(r'ab*', text)
print("1:", task1)


# 2
task2 = re.findall(r'ab{2,3}', text)
print("2:", task2)


# 3
task3 = re.findall(r'[a-z]+_[a-z]+', text)
print("3:", task3)


# 4
task4 = re.findall(r'[A-Z][a-z]+', text)
print("4:", task4)


# 5
task5 = re.findall(r'a.*?b', text)
print("5:", task5)


# 6
task6 = re.sub(r'[ ,.]', ':', text)
print("6:", task6[:200])  


# 7
snake_words = re.findall(r'[a-z]+_[a-z_]+', text)

camel_words = []
for word in snake_words:
    parts = word.split('_')
    camel = parts[0] + ''.join(p.capitalize() for p in parts[1:])
    camel_words.append(camel)

print("7:", camel_words)


# ү
example = "HelloWorldPythonTest"
task8 = re.split(r'(?=[A-Z])', example)
print("8:", task8)


# 9. 
task9 = re.sub(r'([A-Z])', r' \1', example).strip()
print("9:", task9)


# 10. 
camel = "helloWorldPythonTest"
task10 = re.sub(r'([A-Z])', r'_\1', camel).lower()
print("10:", task10)