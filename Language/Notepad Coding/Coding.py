class Code :
    def __init__(self, File):
        code = open(f"{File}.txt", "r")
        self.lines = code.read().splitlines()

    def Run(self) : # In class define -> self.(def name)()
        for index in range(len(self.lines)) :
            line = self.lines[index]
            line = line.replace("\\n", "\n")
            # string temp storing system
            strings = []
            str_index, str_tup = -1, [-1, -1]
            MoreString = True
            while MoreString :
                str_index = line.find("\"", str_index+1)
                if (str_index==-1) :
                    MoreString = False
                backslashcnt = 0
                if (str_index>0 and line[str_index-1]=="\\") :
                    backslashcnt = 1
                    while (str_index>backslashcnt and line[str_index-1-backslashcnt]=='\\') :
                        backslashcnt += 1
                    if (backslashcnt%2 == 1) :
                        continue
                if (str_tup[0]==-1) :
                    str_tup[0] = str_index
                elif (str_tup[1]==-1) :
                    str_tup[1] = str_index
                else :
                    strings.append(line[str_tup[0]+1:str_tup[1]])
                    str_tup = [-1, -1]
                    str_tup[0] = str_index
            for string in strings :
                line = line.replace(string, "%s", 1)
            line = line.replace(" ", "")
            self.lines[index] = [line, strings]
            self.ProgramedType(line, strings)

    def ProgramedType(self, line, strings) : # OutPut System Finish
        if (line[:5]=="print") :
            if (line[5]=="(" and line[len(line)-1]==")") :
                self.PrintFunction(line, strings)
        
        elif (line[:5]=="input") :
            if (line[5]=="(" and line[len(line)-1]==")") :
                self.InputFunction(line)

    def PrintFunction(self, line, strings) :
        endindex = -4
        endstring = ""
        comindex = -6
        commastring = " "
        commaindex = -1
        endIndex = -1
        if (line.find("comma=")+1) :
            comindex = line.find("comma=")
            commaindex = line.count("%s", 0, comindex+4)
            commastring = strings[commaindex]
        if (line.find("end=")+1) :
            endindex = line.find("end=")
            endIndex = line.count("%s", 0, endindex+4)
            endstring = strings[endIndex]
        for string in strings :
            if (commaindex!=-1 and strings.index(string)==commaindex) :
                continue
            if (endIndex!=-1 and strings.index(string)==endIndex) :
                continue
            print(string, end="")
            if (strings.index(string) != len(strings)-1-(endindex>-1)-(comindex>-1)) :
                print(commastring, end="")
        print(endstring, end="")

    def InputFunction(self, line) : # input(&(varname), (vartype))
        attributes = []
        stindex = line.find("(")
        for i in range(line.count(',')) :
            attributes.append(line[stindex+1:line.find(",")])
            stindex = line.find(",")
        attributes.append(line[stindex+1:line.find(")")])

        temp_var = {"name":"", "value":""}
        varType = ["int", "float", "string", "str"]
        varindex = -1

        for attri in attributes :
            if attri[0] == "&" :
                temp_var['name'] = attri[1:]
            elif attri in varType :
                varindex = varType.index(attri)
        
        inputed = input()

        if varindex==0 :
            inputed = int(inputed)
        elif varindex==1 :
            inputed = float(inputed)
        elif varindex==2 or varindex==3 :
            inputed = str(inputed)
        
        temp_var['value'] = inputed

        print(temp_var)