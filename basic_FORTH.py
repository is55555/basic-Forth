from __future__ import print_function

MAXINT = (2 ** 32) - 1


def forth_interpreter(input_string, trace = False):
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
        elif TOP.isdigit():
            n = int(TOP)
            if 0 <= n <= MAXINT:
                results.append(n)
            else:
                return -1
        elif TOP == "+":
            if len(results) < 2:
                return -1
            sum_ = results[-1] + results[-2]
            if sum_ > MAXINT:
                return -1
            else:
                results.pop()
                results.pop()
                results.append(sum_)
        elif TOP == "-":
            if len(results) < 2:
                return -1
            diff = results[-1] - results[-2]
            if diff < 0:
                return -1
            else:
                results.pop()
                results.pop()
                results.append(diff)
        elif TOP == "*":
            if len(results) < 2:
                return -1
            prod_ = results[-1] * results[-2]
            if prod_ > MAXINT:
                return -1
            else:
                results.pop()
                results.pop()
                results.append(prod_)
        elif TOP == "/":  # integer division
            if len(results) < 2:
                return -1
            int_div_ = results[-1] // results[-2]
            if int_div_ > MAXINT:
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

