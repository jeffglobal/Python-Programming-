file = open('example.txt', 'w')     # Creates file if it doesn't exist

file.write('Line 1')
file.close()

# 'w' method is NOT an append method, it overwrites current file from index 0

file = open('example.txt', 'w')
file.write('Line 1\n')      # Necessary, or it continues on same line
file.write('Line 2')
file.close()

l = ['line 1', 'line 2', 'line 3']

file = open('example.txt', 'w')
for item in l:
    file.write(item + '\n')

file.close()

l = ['line 4', 'line 5', 'line 6']

file = open('example.txt', 'a')     # append method
for item in l:
    file.write(item + '\n')

file.close()