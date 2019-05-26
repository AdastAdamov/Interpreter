def generatePOLIZ(lexem_list, variable_list, constant_list):
    priorityTable = {
        ";": 1,
        "=": 2,
        "(": 3,
        ")": 4,
        "+": 4,
        "-": 4,
        "*": 5,
        "/": 5
    }
    line, stack = [], []
    index = 0;
    while index < len(lexem_list):
        if lexem_list[index][1] in ["Var","Con"]:
            line.append(lexem_list[index])
        elif len(stack) == 0:
            stack.append(lexem_list[index])

        #elif lexem_list[index][1] == "(":


        elif lexem_list[index][1] == ";":
            while len(stack) != 0:
                line.append(stack.pop())

        elif priorityTable[lexem_list[index][1]] <= priorityTable[stack[-1][1]]:
            line.append(stack.pop())
            stack.append(lexem_list[index])

        elif priorityTable[lexem_list[index][1]] > priorityTable[stack[-1][1]]:
            stack.append(lexem_list[index])

        index += 1
    while len(stack) != 0:
        line.append(stack.pop())
    return line
