# All constants are indexed from 0
TERM = 0
RULE = 1

# Terminals
T_LPAR = 0
T_RPAR = 1
T_A = 2
T_PLUS = 3
T_END = 4
T_INVALID = 5

# Non-Terminals
N_S = 0
N_F = 1

# Parse table
table = [[ 1, -1, 0, -1, -1, -1],
         [-1, -1, 2, -1, -1, -1]]

RULES = [[(RULE, N_F)],
         [(TERM, T_LPAR), (RULE, N_S), (TERM, T_PLUS), (RULE, N_F), (TERM, T_RPAR)],
         [(TERM, T_A)]]

stack = [(TERM, T_END), (RULE, N_S)]

def lexical_analysis(inputstring):
    print("Lexical analysis")
    tokens = []
    for c in inputstring:
        if c   == "+": tokens.append(T_PLUS)
        elif c == "(": tokens.append(T_LPAR)
        elif c == ")": tokens.append(T_RPAR)
        elif c == "a": tokens.append(T_A)
        else: tokens.append(T_INVALID)
    tokens.append(T_END)
    print(tokens)
    return tokens

def syntactic_analysis(tokens):
    print("Syntactic analysis")
    position = 0
    while len(stack) > 0:
        (stype, svalue) = stack.pop()
        token = tokens[position]
        if stype == TERM:
            if svalue == token:
                position += 1
                print("pop", svalue)
                if token == T_END:
                    print("input accepted")
            else:
                print("bad term on input:", token)
                break
        elif stype == RULE:
            print("svalue", svalue, "token", token)
            rule = table[svalue][token]
            print("rule", rule)
            for r in reversed(RULES[rule]):
                stack.append(r)
        print("stack", stack)

inputstring = "(a+a)"
syntactic_analysis(lexical_analysis(inputstring))
