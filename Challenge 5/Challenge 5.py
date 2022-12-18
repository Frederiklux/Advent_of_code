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
    moved_crates_quant = int(x[5:7].strip())
    from_stack = int(x[x.find('from')+5])
    to_stack = int(x[x.find('to')+3])
    moved_crates = all_stacks[int(from_stack)-1][len(all_stacks[from_stack-1])-moved_crates_quant:][::-1]
    all_stacks[int(from_stack)-1] = all_stacks[int(from_stack)-1][0:len(all_stacks[from_stack-1])-moved_crates_quant]
    all_stacks[to_stack-1] = all_stacks[to_stack-1]+moved_crates

for i in range(len(crane_commands)):
    crate_move(crane_commands[i])

def crate_move_9001(x):
    moved_crates_quant = int(x[5:7].strip())
    from_stack = int(x[x.find('from')+5])
    to_stack = int(x[x.find('to')+3])
    moved_crates = all_stacks[int(from_stack)-1][len(all_stacks[from_stack-1])-moved_crates_quant:]
    all_stacks[int(from_stack)-1] = all_stacks[int(from_stack)-1][0:len(all_stacks[from_stack-1])-moved_crates_quant]
    all_stacks[to_stack-1] = all_stacks[to_stack-1]+moved_crates


for i in range(len(crane_commands)):
    crate_move_9001(crane_commands[i])

answer1 = PSNRGBTFT
answer2 = BNTZFPMMW
