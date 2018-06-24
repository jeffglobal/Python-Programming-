def age_func(age):              # This 'age' is a LOCAL variable
    new_age = float(age) + 50
    return new_age


age = input('Enter your age: ')     # This 'age' is a GLOBAL variable
print(age_func(age))                # Probably bad form because ambiguously
                                    # defined 2 variables

