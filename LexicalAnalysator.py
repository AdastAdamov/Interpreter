def analyze(code):
    index, line = 0, 1
    lexem_list, variable_list, constant_list = [], [], []
    lexem = ""
    keywords = ["print", "input", "repeat", "until", "goto", "if"]
    operators = ["+","-","*","/","(",")",":","=",";","{","}","<",">"]
    whitespaces = [" ","\t"]
    while index < len(code):
        if code[index].isdigit():
            while code[index].isdigit():
                lexem += code[index]
                index += 1
            if int(lexem) not in constant_list:
                constant_list.append(int(lexem))
            lexem_list.append([line, "Con", constant_list.index(int(lexem))])
            lexem = ""
            if code[index].isalpha():
                raise Exception(str(line) + ":Variable name cannot begin with number")
            continue
        if code[index].isalpha():
            while code[index].isalpha() or code[index].isdigit():
                lexem += code[index]
                index += 1
            if lexem in keywords:
                lexem_list.append([line, lexem, "-"])
            else:
                if [lexem,""] not in variable_list:
                    variable_list.append([lexem, ""])
                lexem_list.append([line, "Var", variable_list.index([lexem, ""])])
            lexem = ""
            continue
        if code[index] in operators:
            lexem_list.append([line, code[index], "-"])
            index += 1
            continue
        if code[index] in whitespaces:
            index += 1
            continue
        if code[index] == "\n":
            line += 1
            index += 1
            continue
        raise Exception(str(line) + ":Unknown symbol")


    return lexem_list, variable_list, constant_list

