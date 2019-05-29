def run(executableLine, lexem_list, variable_list, constant_list):
    operators = [";","=","(",")","+","-","*","/","print", "goto"]
    stack = []
    output = ""

    def getValue(lexem):
        if not isinstance(lexem, list):
            return lexem
        if lexem[1]=='Var':
            if variable_list[lexem[2]][1] == "":
                raise Exception(str(lexem[0]) + " : Variable was not initialized.")
            return variable_list[lexem[2]][1]
        elif lexem[1]=='Con':
            return constant_list[lexem[2]]
        else:
            raise Exception("Not a number.")

    index = 0
    while index < len(executableLine):
        if executableLine[index][1] == "Var" and executableLine[index+1][1] == ":":
            index += 1
        elif executableLine[index][1] not in operators:
            stack.append(executableLine[index])
        elif executableLine[index][1] == "*":
            stack.append(getValue(stack.pop()) * getValue(stack.pop()))
        elif executableLine[index][1] == "/":
            stack.append(getValue(stack.pop(-2)) / getValue(stack.pop()))
        elif executableLine[index][1] == "+":
            stack.append(getValue(stack.pop()) + getValue(stack.pop()))
        elif executableLine[index][1] == "-":
            stack.append(getValue(stack.pop(-2)) - getValue(stack.pop()))
        elif executableLine[index][1] == "=":
            variable_list[stack.pop()[2]][1] = getValue(stack.pop())
        elif executableLine[index][1] == "print":
            output += str(getValue(stack.pop())) + "\n"
        elif executableLine[index][1] == "goto":
            target = executableLine[index+1][1]
            index = 0
            while executableLine[index][1] != target or executableLine[index+1][1] != ":":
                index += 1
            index += 1
        index += 1

    return output