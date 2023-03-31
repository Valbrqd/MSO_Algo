pile = []
dico_ope = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y,'#': lambda x: -x}

# phrase = str(input("Entrez une expression postfixée : "))
phrase = "53-34*+"

for i in phrase:
    if i not in dico_ope:
        pile.append(int(i))
    elif i == '#':
        pile.append(dico_ope[i](pile.pop()))
    else:
        x = pile.pop()
        y = pile.pop()            
        pile.append(dico_ope[i](y, x))



