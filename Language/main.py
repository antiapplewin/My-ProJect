class MathCal :
    def add(x, y) :
        return x+y
    def sub(x, y) :
        return x-y
    def mul(x, y) :
        return x*y
    def dis(x, y) :
        return x/y
    def rest(x, y) :
        return x%y
    


Scriptes, Executed, lists = [], [], []
varibles = {}

string  = input()

while (string!="run") :
    Scriptes.append(string)
    string = input()

for i in range(len(Scriptes)) :
    if (Scriptes[i][0:3]=="var") : # 변수 : int, float, string, bool
        space_bar = Scriptes[i].find(" ")
        Str_Script = Scriptes[i][space_bar+1:]
        if (Str_Script.find(" ")!=-1) :
            if (Str_Script[Str_Script.find("=")+1:].find("=")!=-1) :
                var_name = Str_Script[:Str_Script.find(" ")]
            elif (Str_Script.find("=")>Str_Script.find(" ")) :
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
        print(varibles) # 변수 코드 end
    elif (Scriptes[i][0:5]=="print") :
        quotes1, quotes2 = Scriptes[i].find("\""), Scriptes[i].rfind("\"")
        plot = Scriptes[i][quotes1+1:quotes2]
        plot2 = plot
        vars = []
        exe = 0
        while (plot2.find("\&{")!=-1) :
            # print(plot2)
            var_name_start = plot2.find("\&{")+2
            var_name_end = plot2[var_name_start+1:].find("}")+var_name_start+1
            # print(var_name_start, var_name_end, exe)
            # print(plot2[var_name_start+1:var_name_end])
            
            pvns, pvne = var_name_start+exe, var_name_end+exe
            vars.append([plot2[var_name_start+1:var_name_end], pvns, pvne])
            plot2 = plot[pvne+1:]
            exe = pvne+1

        # print(plot2)
            
        exe2 = 0

        for i in range(len(vars)) :
            # print("for : ", vars[i])
            plot_bef = plot[:vars[i][1]-2-exe2]
            plot_aft = plot[vars[i][2]+1-exe2:]
            # print("plot 설정 plot_bef :  ", plot_bef, "plot_var : ", plot_var, "plot_aft : ", plot_aft)
            plot_var = str(varibles[str(vars[i][0])])
            plot = plot_bef + plot_var + plot_aft
            exe2 += 4+len(vars[i][0])-len(plot_var)

        print(plot)

    if (Scriptes[i][:3] == "set") : # 기본적으로는 정수만 계산
        print("waiting")
