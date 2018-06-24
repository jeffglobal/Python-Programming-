# print(1)
# int(9)
# int (9)
# print(2)
# print (3)

# a = 1
# b = "2"
# c = 3
# print(int(2.4))
# print(a + int(b))
# print(str(a) + b)
# print(c)

def divide(a,b):
    try:
        return a/b
    #except:                     # Excepting all errors this way
    except ZeroDivisionError:
        return 'Zero division is undefined'

print(divide(1,0))