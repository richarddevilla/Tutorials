from datetime import datetime

def inputDOB():
    while True:
        dob = input('Input your date of birth(dd/mm/yyyy): ')
        if validateDOB(dob):break
    return validateDOB(dob)

def validateDOB(dob):
    try:
        dobParsed = datetime.strptime(dob, '%d/%m/%Y')
        assert dobParsed < datetime.now()
        return dobParsed
    except ValueError:
        print('Please input a valid date of birth!')
    except AssertionError:
        print('Unless you are a time traveller, I doubt you were born on ' + str(dobParsed) + '.')
    except:
        print('Unexpected error! Please try again.')
    return False

def calculateAge(dobParsed):
    currentDate = datetime.now()
    age = currentDate.year - dobParsed.year
    if (currentDate.month, currentDate.day) < (dobParsed.month, dobParsed.day):
        age -= 1
    return age

def inputName():
    while True:
        name = input('Input your name: ')
        if validateName(name):break
    return name

def validateName(name):
    if name.isalpha():
        return True
    else:
        print('Please input letters only!')
        return False

name = inputName()
dobParsed = inputDOB()
age = calculateAge(dobParsed)
print('Hi! ' + name)
print('You are ' + str(age) + ' years old')
