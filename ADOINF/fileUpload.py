import os

class File :
    def Create(name) :
        try :
            a = open(f'{name}.txt', 'r')
            a.close()
            print("Error : ExistingFile")
        except FileNotFoundError :
            a = open(f'{name}.txt', 'a')
            a.close()
    def Edit(name, fiLe) :
        try :
            a = open(f'{name}.txt', 'w')
            for k, v in fiLe['setting'].items() :
                a.write(f"{k}:{v} ")
            a.write("end:100\n\n")

            for i in range(len(fiLe['notes'])) :
                for k, v in fiLe['notes'][i].items() :
                    a.write(f"{k}:{v},")
                a.write(" ")
            a.write("end:100")
            a.close()
        except FileNotFoundError :
            print("Error : UnFoundFile")
    def Delete(name) :
        try :
            os.remove(f"{name}.txt")
        except FileNotFoundError :
            print("Error : UnFoundFile")
    def Load(name) :
        try :
            Fi = open(f"{name}.txt", 'r')
            Fi_lines = Fi.readlines()
            Fi_list = []
            for item in Fi_lines :
                Fi_list.append(str(item.strip()))
            
            note, setting = [], {}

            Fi_str = Fi_list[0]
            while Fi_str.find(" ")+1 :
                F_str = Fi_str[:Fi_str.find(" ")]
                Fi_str = Fi_str[Fi_str.find(" ")+1:]
                F_attri_name = F_str[:F_str.find(":")]
                F_attri_val = F_str[F_str.find(":")+1:]
                setting[F_attri_name] = F_attri_val

            Fi_str = Fi_list[2]
            ind = 0

            while Fi_str.find(" ")+1 :
                note.append({})
                F_str = Fi_str[:Fi_str.find(" ")]
                Fi_str = Fi_str[Fi_str.find(" ")+1:]
                while F_str.find(",")+1 :
                    F_attribute = F_str[:F_str.find(",")]
                    F_str = F_str[F_str.find(",")+1:]
                    F_attri_name = F_attribute[:F_attribute.find(":")]
                    F_attri_val = F_attribute[F_attribute.find(":")+1:]
                    note[ind][F_attri_name] = float(F_attri_val)
                ind += 1

            save_ = {"setting":setting, "notes":note}
            return save_
        except FileNotFoundError:
            print("Error : UnFoundFile")