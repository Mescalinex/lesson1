'''
first_name = 'Mikhail'
last_name = 'Mashchenko'
print(f'{first_name } {last_name}')
'''
'''
a = [3, 5, 7, 9, 10.5]
print(a)
a.append('Python')
#print(len(a))

print(a[0])
print(a[5])
print(a[1:5])

a.remove('Python')
print(a)
'''

a = {
    "city": "Москва",
    "temperature": 20
}

a["temperature"] = a["temperature"] - 5

print(a)
print(a.get("country", "Россия"))

a['date'] = '27.05.2019'
print(a)