from __future__ import print_function

MAXINT = (2 ** 32) - 1
MININT = MAXINT * -1


def is_valid_number(n):
    try:
        n = int(n)
    except ValueError:
        return False
    return MININT <= n <= MAXINT


def forth_interpreter(input_string, trace=False):
    input_list = input_string.split()
    input_list = input_list[::-1]

    results = []
    while input_list:
        if trace:
            print("INPUT tape:", input_list)
            print("OUTPUT tape:", results)
        TOP = input_list.pop()
        if TOP == "POP":
            if results:
                results.pop()
            else:
                return -1
        elif TOP == "DUP":
            if results:
                results.append(results[-1])
        elif is_valid_number(TOP):
            n = int(TOP)
            results.append(n)
        elif TOP == "+":
            if len(results) < 2:
                return -1
            sum_ = results[-1] + results[-2]
            if not is_valid_number(sum_):
                return -1
            else:
                results.pop()
                results.pop()
                results.append(sum_)
        elif TOP == "-":
            if len(results) < 2:
                return -1
            diff_ = results[-1] - results[-2]
            if not is_valid_number(diff_):
                return -1
            else:
                results.pop()
                results.pop()
                results.append(diff_)
        elif TOP == "*":
            if len(results) < 2:
                return -1
            prod_ = results[-1] * results[-2]
            if not is_valid_number(prod_):
                return -1
            else:
                results.pop()
                results.pop()
                results.append(prod_)
        elif TOP == "/":  # integer division
            if len(results) < 2:
                return -1
            int_div_ = results[-1] // results[-2]
            if not is_valid_number(int_div_):
                return -1
            else:
                results.pop()
                results.pop()
                results.append(int_div_)

    if trace:
        print("INPUT tape:", input_list)
        print("OUTPUT tape:", results)

    if not results:
        return -1
    else:
        return results[-1]

if __name__ == "__main__":
    print(forth_interpreter("5 6 + -"), "== -1 (error)")  # error
    print(forth_interpreter("3 DUP 5 - -"), "== -1 (error)")  # error
    print(forth_interpreter('18 DUP 4 POP 5 DUP + DUP + - +'), "== 20")  # 20

    print(forth_interpreter('18 DUP 4 POP 5 DUP + DUP + - +', trace=True), "== 20")  # 20

