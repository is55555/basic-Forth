# Toy FORTH interpreter.
 
MAXINT: 2^32 - 1

By default, tracing is off (set to False).

    print(forth_interpreter('18 DUP 4 POP 5 DUP + DUP + - +', trace=True), "== 20")  # 20

Produces the following:

    INPUT tape: ['+', '-', '+', 'DUP', '+', 'DUP', '5', 'POP', '4', 'DUP', '18']
    OUTPUT tape: []
    INPUT tape: ['+', '-', '+', 'DUP', '+', 'DUP', '5', 'POP', '4', 'DUP']
    OUTPUT tape: [18]
    INPUT tape: ['+', '-', '+', 'DUP', '+', 'DUP', '5', 'POP', '4']
    OUTPUT tape: [18, 18]
    INPUT tape: ['+', '-', '+', 'DUP', '+', 'DUP', '5', 'POP']
    OUTPUT tape: [18, 18, 4]
    INPUT tape: ['+', '-', '+', 'DUP', '+', 'DUP', '5']
    OUTPUT tape: [18, 18]
    INPUT tape: ['+', '-', '+', 'DUP', '+', 'DUP']
    OUTPUT tape: [18, 18, 5]
    INPUT tape: ['+', '-', '+', 'DUP', '+']
    OUTPUT tape: [18, 18, 5, 5]
    INPUT tape: ['+', '-', '+', 'DUP']
    OUTPUT tape: [18, 18, 10]
    INPUT tape: ['+', '-', '+']
    OUTPUT tape: [18, 18, 10, 10]
    INPUT tape: ['+', '-']
    OUTPUT tape: [18, 18, 20]
    INPUT tape: ['+']
    OUTPUT tape: [18, 2]
    INPUT tape: []
    OUTPUT tape: [20]
    20 == 20
