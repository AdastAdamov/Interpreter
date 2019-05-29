def run(executableLineOriginal, lexem_list, variable_list, constant_list):
    operators = [";","=","(",")","+","-","*","/"]
    executableLine = executableLineOriginal[:]

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
        if executableLine[index][1] not in operators:
            pass
        elif executableLine[index][1] == "*":
            executableLine[index] = getValue(executableLine[index-2]) * getValue(executableLine[index-1])
            del executableLine[index-1]
            del executableLine[index-2]
            index -= 2
        elif executableLine[index][1] == "/":
            executableLine[index] = getValue(executableLine[index-2]) / getValue(executableLine[index-1])
            del executableLine[index-1]
            del executableLine[index-2]
            index -= 2
        elif executableLine[index][1] == "+":
            executableLine[index] = getValue(executableLine[index-2]) + getValue(executableLine[index-1])
            del executableLine[index-1]
            del executableLine[index-2]
            index -= 2
        elif executableLine[index][1] == "-":
            executableLine[index] = getValue(executableLine[index-2]) - getValue(executableLine[index-1])
            del executableLine[index-1]
            del executableLine[index-2]
            index -= 2
        elif executableLine[index][1] == "=":
            variable_list[executableLine[index-2][2]][1] = getValue(executableLine[index-1])
            del executableLine[index]
            del executableLine[index-1]
            del executableLine[index-2]
            index -= 3
        index += 1

    return ""