from datetime import datetime

def inputDOB():
    while True:
        dob = input('Input your date of birth(dd/mm/yyyy): ')
        validDOB = validateDOB(dob)
        if validDOB:
            break
    return validDOB

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

def calculateAge(validDOB):
    currentDate = datetime.now()
    age = currentDate.year - validDOB.year
    if (currentDate.month, currentDate.day) < (validDOB.month, validDOB.day):
        age -= 1
    return age

def inputName():
    while True:
        name = input('Input your name: ')
        validName = validateName(name)
        if validName:
            break
    return validName

def validateName(name):
    if name.isalpha():
        return name
    else:
        print('Please input letters only!')
        return False

def generatePassword(sequence1,sequence2,passwordLength=6):
    #convert sequence to binary

    binarySequence = ''
    binarySequence2 =''
    for char in sequence1:
        binarySequence += (format(ord(char), 'b'))
    for char in sequence2:
        binarySequence2 += (format(ord(char), 'b'))

    #calculate the maximum possible size of bits
    #based on the binarySequence and passwordLength
    itemSize = len(binarySequence) // passwordLength
    newBinarySequence = []
    counter = 0
    while not len(newBinarySequence) == passwordLength:
        andBinary = int(binarySequence[counter:counter + itemSize],2) | int(binarySequence2,2)
        newBinarySequence.append(andBinary)
        counter+=itemSize
    return newBinarySequence


# name = inputName()
# dob = inputDOB()
# age = calculateAge(dob)
name = 'Richard'
dob = 19870822
age = 34
print('Hi! ' + name)
print('You are ' + str(age) + ' years old')

fullInfo = str(dob)+str(age)
password = generatePassword(fullInfo,name)
print(password)
#password = ''.join(format(for each in fullInfo,'b'))

