import random

Scriptes, Executed, lists = [], [], []
varibles = {}

Scriptes.append(input())

for i in range(len(Scriptes)) :
    if (Scriptes[i][0:5]=="print") :
        # first_parentheses = Scriptes[i].find("(")
        # second_parentheses = Scriptes[i].find(")")
        first_doublequotationmark = Scriptes[i].find("\"")
        second_doublequotationmark = Scriptes[i].rfind("\"")
        print(Scriptes[i][first_doublequotationmark+1:second_doublequotationmark])
    
    elif (Scriptes[i][0:7]=="execute") :
        Scriptes[i] = Scriptes[i].replace(" ", "")
        opening_parentheses = Scriptes[i].find("(")
        closing_parentheses = Scriptes[i].find(")")
        Executed.append(Scriptes[i][opening_parentheses+1:closing_parentheses])
        print(Executed)
    
    elif (Scriptes[i][0:5]=="input") :
        first_doublequotationmark = Scriptes[i].find("\"")
        second_doublequotationmark = Scriptes[i].rfind("\"")
        a = input(Scriptes[i][first_doublequotationmark+1:second_doublequotationmark])
        print(a)

    elif (Scriptes[i][0:3]=="var") :
        space_bar = Scriptes[i].find(" ")
        Str_Script = Scriptes[i][space_bar+1:]
        if (Str_Script.find(" ")!=-1) :
            if (Str_Script[Str_Script.find("=")+1:].find("=")!=-1) :
                print("here?")
                var_name = Str_Script[:Str_Script.find(" ")]
            elif (Str_Script.find("=")>Str_Script.find(" ")) :
                print("or here?")
                var_name = Str_Script[:Str_Script.find(" ")]
            else :
                var_name = Str_Script[:Str_Script.find("=")]
        else :
            if (Str_Script[Str_Script.find("=")+1:].find("=")!=-1) :
                var_name = Str_Script
            else :
                var_name = Str_Script[:Str_Script.find("=")]
        var_value = 0
        if not(Scriptes[i].find("=")==-1) :
            if (Scriptes[i].find("\"")!=-1) :
                var_value = str(Scriptes[i][Scriptes[i].find("\"")+1:Scriptes[i].rfind("\"")])
            elif (Scriptes[i].find("\'")!=-1) :
                var_value = str(Scriptes[i][Scriptes[i].find("\'")+1:Scriptes[i].rfind("\'")])
            elif (Scriptes[i].find("true")!=-1) :
                var_value = True
            elif (Scriptes[i].find("false")!=-1) :
                var_value = False
            elif (Scriptes[i].find(".")!=-1) :
                Str_Script = Str_Script[Str_Script.find("=")+1:]
                if (Str_Script.find(" ")!=-1) :
                    Str_Script = Str_Script[Str_Script.rfind(" ")+1:]
                    var_value =float(Str_Script)
                else :
                    var_value = float(Str_Script[Str_Script[i].find("=")+1:])
            else :
                Str_Script = Str_Script[Str_Script.find("=")+1:]
                if (Str_Script.find(" ")!=-1) :
                    Str_Script = Str_Script[Str_Script.rfind(" ")+1:]
                    var_value = int(Str_Script)
                else :
                    var_value = int(Str_Script[Str_Script.find("=")+1:])
        varibles[var_name] = var_value
        print(varibles)

    elif (Scriptes[i][0:4]=="list") :
        space_bar = Scriptes[i].find(" ")
        Str_Script = Scriptes[i][space_bar+1:]
        if (Str_Script.find(" ")!=-1) :
            if (Str_Script[Str_Script.find("=")+1:].find("=")!=-1) :
                print("here?")
                var_name = Str_Script[:Str_Script.find(" ")]
            elif (Str_Script.find("=")>Str_Script.find(" ")) :
                print("or here?")
                var_name = Str_Script[:Str_Script.find(" ")]
            else :
                var_name = Str_Script[:Str_Script.find("=")]
        else :
            if (Str_Script[Str_Script.find("=")+1:].find("=")!=-1) :
                var_name = Str_Script
            else :
                var_name = Str_Script[:Str_Script.find("=")]
        var_value = 0
        if not(Scriptes[i].find("=")==-1) :
            if (Scriptes[i].find("\"")!=-1) :
                var_value = str(Scriptes[i][Scriptes[i].find("\"")+1:Scriptes[i].rfind("\"")])
            elif (Scriptes[i].find("\'")!=-1) :
                var_value = str(Scriptes[i][Scriptes[i].find("\'")+1:Scriptes[i].rfind("\'")])
            elif (Scriptes[i].find("true")!=-1) :
                var_value = True
            elif (Scriptes[i].find("false")!=-1) :
                var_value = False
            elif (Scriptes[i].find(".")!=-1) :
                Str_Script = Str_Script[Str_Script.find("=")+1:]
                if (Str_Script.find(" ")!=-1) :
                    Str_Script = Str_Script[Str_Script.rfind(" ")+1:]
                    var_value =float(Str_Script)
                else :
                    var_value = float(Str_Script[Str_Script[i].find("=")+1:])
            else :
                Str_Script = Str_Script[Str_Script.find("=")+1:]
                if (Str_Script.find(" ")!=-1) :
                    Str_Script = Str_Script[Str_Script.rfind(" ")+1:]
                    var_value = int(Str_Script)
                else :
                    var_value = int(Str_Script[Str_Script.find("=")+1:])
        lists.append([var_name, var_value])
        lists[0].append("10")
        print(lists)

# execute(함수 이름)
# math.im = 가오스, 소수값 등등

# value(change_type, 변수이름, 값)