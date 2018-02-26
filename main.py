from datetime import datetime


def calculateAge():
    while True:
        try:
            dob = input('Input your date of birth(dd/mm/yyyy): ')
            currentDate = datetime.now()
            dobParsed = datetime.strptime(dob, '%d/%m/%Y')
            age = currentDate.year - dobParsed.year
            if (currentDate.month, currentDate.day) < (dobParsed.month, dobParsed.day):
                age -= 1
            assert age > 0
        except ValueError:
            print('Please input a valid date of birth!')
        except AssertionError:
            print('Unless you are a time traveller, I doubt you were born on ' + dob + '.')
        except:
            print('Unexpected error! Please try again.')
    return age


name = input('Input your name: ')

print(calculateAge())
