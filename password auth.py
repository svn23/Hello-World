"""This Code is for testing purposes
Working Model >
    First of all % username % password will be stored in the dictionary
    Then It will ask for the username and password for the login
    Then it will check the username and password for the authentication
    At last it will show you the desired Output"""
employees = {}

max_length = 5

while len(employees) < max_length:
    u = input("Enter employee's name: ")
    p = input("Enter employee's Password: ")

    employees[u] = p


# 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
print(employees)

print('Enter correct username and password combo to continue')
count=0
while count < 3:
    a = input ("Enter correct username to continue: ")
    b = input ("Enter correct password to continue: ")

    if b ==list(employees.values())[0] and a ==list(employees.keys())[0]:
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1