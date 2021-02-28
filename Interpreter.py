# open input
fin = open('./input.txt', 'r')

# read lines
lines = fin.read().splitlines()

# close input
fin.close()

# open output
fout = open('./output.txt', 'w')

def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

def process_command(command, args):
    global index, varlist
    # comment
    if command == '#':
        index += 1
    # print
    elif command == 'print':
        if len(args) > 1:
            if args[0] == 'var':
                try:
                    varidx = int(args[1])
                    fout.write(str(varlist[varidx]) + '\n')
                except:
                    fout.write('! Invalid var !\n')
                return
        fout.write(' '.join(args) + '\n')
    # skip next line
    elif command == 'skip':
        index += 2
    # goto line
    elif command == 'goto':
        try:
            line = int(args[0])
            index = line - 2
        except:
            fout.write('! Invalid goto !')
    # for loop
    elif command == 'for':
        try:
            count = int(args[0])
            for i in range(count):
                process_command(args[1], args[2:])
        except:
            fout.write('! Invalid for loop !\n')
    # variable
    elif command == 'var':
        try:
            varidx = int(args[0])
            if len(args) > 2:
                if args[1] == 'var':
                    var2idx = int(args[2])
                    varlist[varidx] = varlist[var2idx]
                    return
            if args[1] == '+':
                varlist[varidx] += 1
                return
            elif args[1] == '-':
                varlist[varidx] -= 1
                return
            # int var
            if is_int(args[1]):
                varlist[varidx] = int(args[1])
            # string var
            else:
                varlist[varidx] = ''.join(args[1:])
        except:
            fout.write('! Invalid var !\n')
    # variable list
    elif command == 'varlist':
        try:
            count = int(args[0])
            while len(varlist) < count:
                varlist.append(None)
        except:
            fout.write('! Invalid varlist !\n')
    # unrecognized command
    else:
        fout.write('! Command ' + command + ' not recognized !\n')

varlist = []
index = 0
while index < len(lines):
    words = lines[index].split()
    if len(words) < 1: continue
    command = words[0]
    process_command(command, words[1:])
    index += 1

# close output
fout.close()
