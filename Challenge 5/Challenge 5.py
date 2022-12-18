f = open('input.txt', 'r')

content = f.read()

all_stacks = []
for j in range(9):
    curr_stack = ''
    for i in range(8):
        curr_stack = curr_stack + content.splitlines()[i][1+(j)*4].strip()
    all_stacks.append(curr_stack)

# Få loadet de 9 stacks i lister, hvor du starter fra bunden.

# Lav en funktion, der flytter kasser som en kran efter kommandoer

# Kør alle kommandoer igennem din kran-funktion

# gg wp