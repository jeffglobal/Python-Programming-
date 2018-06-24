file = open("test", 'r')
content = file.read()
print(content)

file.seek(0)
content=file.readlines()
print(content)

content_clean = [i.rstrip('\n') for i in content]
print(content_clean)

content_clean = ''
content_clean = [line.rstrip('\n') for line in content]     # More descriptive?
print(content_clean)                                        # I think so...

file.close()

# Variables still there, and/or reuseable variables...
