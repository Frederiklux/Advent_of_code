f = open('Challenge 6\input.txt', 'r')

content = f.read()

print(content)



count = []
for i in range(len(content)-4):
    if ((content[i] == content[i+1]) | (content[i] == content[i+2]) | (content[i] == content[i+3]) | (content[i] == content[i+4]) | 
        (content[i+1] == content[i+2]) | (content[i+1] == content[i+3]) | (content[i+1] == content[i+4]) |
        (content[i+2] == content[i+3]) | (content[i+2] == content[i+4]) | 
        (content[i+3] == content[i+4])) == True:
        pass
    else: 
        count.append(i) 
print(count[0]+4)