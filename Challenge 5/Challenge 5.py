f = open('input.txt', 'r')

content = f.read()

with open('input.txt', 'r') as fp:
    max_lines = len(fp.readlines())

all_stacks = []
for j in range(9):
    curr_stack = ''
    for i in range(8):
        curr_stack = curr_stack + content.splitlines()[i][1+(j)*4].strip()
    all_stacks.append(curr_stack[::-1])

crane_commands = []
for i in range(10,max_lines):
    crane_commands.append(content.splitlines()[i])

def crate_move(x):
    moved_crates = x[5:7].strip()
    from_stack = x[x.find('from')+5]
    to_stack = x[x.find('to')+3]
    print(moved_crates, from_stack, to_stack)

crate_move(crane_commands[25])
# Få loadet de 9 stacks i lister, hvor du starter fra bunden.

# Lav en funktion, der flytter kasser som en kran efter kommandoer

# Kør alle kommandoer igennem din kran-funktion

# gg wp