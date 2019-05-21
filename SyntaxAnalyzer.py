def analyze(lexem_list, variable_list, constant_list):
    operators = ['+', '-', '*', '/', '<', '>']

    def expression(start, end):
        if end - start == 0:
            raise Exception(str(lexem_list[start-1][0]) + ": Invalid expression.")
        index = start
        if lexem_list[index][1] == 'Var' or lexem_list[index][1] == 'Con':
            index += 1
            if index == end:
                return
            else:
                if lexem_list[index][1] in operators:
                    index += 1
                    expression(index, end)
                    return

        if end - start < 2:
            raise Exception(str(lexem_list[start - 1][0]) + ": Invalid expression.")
        if lexem_list[index][1] == '-' and (lexem_list[index+1][1] == 'Var' or lexem_list[index+1][1] == 'Con'):
            index += 2
            if index == end:
                return
            else:
                if lexem_list[index][1] in operators:
                    index += 1
                    expression(index, end)
                    return

        if lexem_list[start][1] == '(':
            index = start + 1
            counter = 1
            while index < end and counter != 0:
                if lexem_list[index][1] == '(': counter += 1
                elif lexem_list[index][1] == ')': counter -= 1

                if counter != 0: index += 1
            if index == end:
                raise Exception(str(lexem_list[index - 1][0]) + " : ')' operator is missing.")
            else:
                expression(start + 1, index)
                index += 1
                if index == end:
                    return
                else:
                    if lexem_list[index][1] in operators:
                        index += 1
                        expression(index, end)
                        return
        raise Exception(str(lexem_list[index][0]) + " : Illegal expression.")

    def statement(start, end):

        #Variable initialization
        if lexem_list[start][1] == 'Var':
            if lexem_list[start+1][1] == '=':
                expression(start+2, end)
            else:
                raise Exception(str(lexem_list[start][0]) + " : Variable declaration: [VARIABLE_NAME] [=] [VALUE] or [EXPRESSION]")

        #Print function
        elif lexem_list[start][1] == 'print':
            index = start + 1
            expression(index, end)

        #Goto keyword
        elif end - start == 2 and lexem_list[start][1] == 'goto' and lexem_list[start+1][1] == 'Var':
            pass

        else:
            raise Exception(                str(lexem_list[start][0]) + " : Illegal statement")


    def analyze_block(start, end):
        while start < end:
            #Goto label
            if end - start > 1 and lexem_list[start][1] == 'Var' and lexem_list[start+1][1] == ':':
                start = start + 2
                continue

            # Repeat keyword processing
            elif lexem_list[start][1] == 'repeat':
                index = start = start + 1
                if lexem_list[start][1] != '{':
                    raise Exception(str(lexem_list[index - 1][0]) + " : '{' operator is missing.")

                index = start = index + 1
                counter = 1
                while index < end and counter != 0:
                    if lexem_list[index][1] == '{': counter += 1
                    elif lexem_list[index][1] == '}': counter -= 1

                    if counter != 0: index += 1

                if index == end:
                    raise Exception(str(lexem_list[index - 1][0]) + " : '}' operator is missing.")

                analyze_block(start, index)
                index += 1
                if lexem_list[index][1] != 'until':
                    raise Exception(str(lexem_list[index - 1][0]) + " : 'until' keyword is missing after 'repeat'.")
                start = index = index + 1
                while lexem_list[index][1] != ';':
                    index += 1
                    if index == end:
                        raise Exception(str(lexem_list[index - 1][0]) + " : ';' operator is missing.")
                expression(start, index)
                start = index + 1

            #If keyword processing
            elif lexem_list[start][1] == 'if':
                index = start = start + 1
                while lexem_list[index][1] != '{':
                    index += 1
                    if index == end:
                        raise Exception(str(lexem_list[index - 1][0]) + " : '{' operator is missing.")
                expression(start, index)
                start = index = index + 1
                counter = 1
                while index < end and counter != 0:
                    if lexem_list[index][1] == '{': counter += 1
                    elif lexem_list[index][1] == '}': counter -= 1

                    if counter != 0: index += 1

                if index == end:
                    raise Exception(str(lexem_list[index - 1][0]) + " : '}' operator is missing.")

                analyze_block(start, index)
                start = index + 1

            else:
                index = start
                while lexem_list[index][1] != ';':
                    index += 1
                    if index == end:
                        raise Exception(str(lexem_list[index - 1][0]) + " : ';' operator is missing.")
                statement(start, index)
                start = index + 1

    analyze_block(0, len(lexem_list))
