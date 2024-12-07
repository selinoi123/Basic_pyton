#START 1
for i in range(12, 24 + 1):
    print(i)
#END

#START 2
for i in range(7, 31 + 1):
    if i % 2 != 0:
        print(i)
#END

#START 3
for i in range(10, -20 - 1, -1):
    if i % 2 == 0:
        print(i)
#END

#START 4
for i in range(1, 45 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
#END

#START 5
def sum_list(arr) -> int:
    count = 0
    for num in arr:
        count += num

    return count

print(sum_list([1, 2, 3, 4, 5]))
#END

#START 6
def remove_from_students(student, remove):
    for a in student:
        if remove in a  :
            return a.pop(remove)
        else:
            return None

def print_students(student):
    for x in student:
        for key, value in x.items():
            print(f"{key}: {value}")

def sort_by_age(student):
    return sorted(student, key=lambda x: x['age'], reverse=True)

students = [
    {"id": 1, "first name": "Selin", "last name": "Introligator", "age": 19, "country": "Israel", "city": "Ashdod"},
    {"id": 2, "first name": "John", "last name": "Doe", "age": 12, "country": "USA", "city": "New York"},
    {"id": 3, "first name": "Jane", "last name": "Smith", "age": 16, "country": "Canada", "city": "Toronto"}
]

print(remove_from_students(students, "city"))
print(print_students(students))
print(sort_by_age(students))
#END

#START 7
def print_cats(pets):
    for cat in pets:
        if cat['animal_type'] == 'cat':
            return cat

def print_animal_names(pets, animal_type):
    for name in pets:
        if name['animal_type'] == animal_type:
            return name['names']


def add_name_to_all(pets, name):
    for pet in pets:
        if name not in pet['names']:
            pet['names'].append(name)
    return pets

our_pets = [
    {"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
    { "animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}
]

print(print_cats(our_pets))
print(print_animal_names(our_pets, "cat"))
print(add_name_to_all(our_pets, "luffy"))
#END

#START 8
def print_student_data(student):
    for key, value in student.items(): # 1
        print(f"{key}: {value}")

def add_hobby(student, hobby):
    if hobby not in student['hobbies']: # 2
        student['hobbies'].append(hobby)
    return student

def delete_hobby(student, hobby):
    if hobby in student['hobbies']: # 4
        student['hobbies'].remove(hobby)
    return student

student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}

print(print_student_data(student))
print("-------------------------------")
print(add_hobby(student, "basketball"))
print("-------------------------------")
print(print_student_data(student)) # 3
print("-------------------------------")
print(delete_hobby(student, "games"))
print("-------------------------------")
print(print_student_data(student)) # 5
print("-------------------------------")
student['family_name'] = 'Doe' # 6
print(student)
#END

#START 9
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')

matrix =[[1, 2],[3, 4],[5, 6]]
print(print_matrix(matrix))
#END

#START 10
def zero_count(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j == 0:
                count += 1
    return count

matrix = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]
print(zero_count(matrix))
#END

#START 11
def find_duplicates(arr):
    duplicates:list[int] = []

    for num in arr:
        count = arr.count(num)
        if count > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates

print(find_duplicates([4, 2, 34, 4, 1, 12, 1, 4]))
#END

#START 12
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
print(reverse_array(arr))
#END

#START 13
def add_arrays(arr1, arr2):
    new_arr: list[int] = []

    for i in range(len(arr1)):
        new_arr.append(arr1[i] + arr2[i])

    return new_arr

print(add_arrays([4, 6, 7], [8, 1, 9]))
#END

#START 14
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Java"))
#END

#START 15
counter: int = 1
while counter < 100:
    print(counter)
    counter *= 2

#END

#START 16
counter: int = 900000
while counter > 50:
    print(counter)
    counter //= 2
#END

#START 17
def find_duplicates(arr):
    duplicates = []
    new_array = []

    i = 0
    while i < len(arr):
        value = arr[i]
        if value not in duplicates and arr.count(value) > 1:
            new_array.append(value)
        duplicates.append(value)
        i += 1
    return new_array
#END

#START 18
def names(arr):
    i = 0
    new_array: list[str] = []
    while i < len(arr):
        if arr[i] not in new_array:
            new_array.append(arr[i])

        i += 1
    return new_array

arr = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(names(arr))
#END

#START 19
def names(arr):
    i = 0
    new_array: list[str] = []
    while i < len(arr):
        if arr[i] not in new_array and arr[i] != 'Pete':
            new_array.append(arr[i])

        i += 1
    return new_array

arr = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(names(arr))
#END

#START 20
def find_consecutive_index(arr):
    index = 0
    while index < len(arr) - 1:
        if arr[index] != arr[index + 1]:
            index += 1
        else:
            return index + 1
    return -1

# Test cases
print(find_consecutive_index([True, False, False, True, True, False]))
print(find_consecutive_index([True, False, True, False, True, True]))
print(find_consecutive_index([True, False, True, False, True, False]))
#END

#START 21
while True:
    full_name: str = str(input("Enter your first name and last name: "))
    if len(full_name.split()) != 2:
        print("Invalid input. Please enter a first and last name.")
    else:
        break

while True:
    try:
        age: int = int(input("Enter your age: "))
        if age < 1 or age > 130:
            print("Age must be between 1 and 130.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

while True:
    email = input("Enter your email: ")
    if '@' not in email:
        print("Invalid email. Please enter a valid email address.")
    else:
        break

print("User Details:")
print(f"Full Name: {full_name}")
print(f"Age: {age}")
print(f"Email: {email}")

#END
