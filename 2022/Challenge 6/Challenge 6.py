f = open('input.txt', 'r')

content = f.read()

for i in range(len(content)-14):
    if len(set(content[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(content)-14):
    if len(set(content[i:i+14])) == 14:
        print(i+14)
        break
