def situation(there, providedlist):
    if there:
        age, month = 0, 0
        action = [] # (action, time)
        time = 0
    else :
        age, month = providedlist['age'], providedlist['month']
        time = providedlist['time']
        action = providedlist['action']
    
    avaaction = ['feed', 'bath']

    while True :
        time += 1

        a = input("What did you do? : ")
        
        if (a.lower() in avaaction) :
            action.append((a, time))

        deleteaction = []

        for act in action :
            if (time-act[1]>=2) :
                if (a==act[0]) :
                    deleteaction.append(act)
                else :
                    print(f"time to {act[0]} your baby ({time-act[1]}h ago)")

        for act in deleteaction :
            action.remove(act)

        print("")

playerlist = {'age':0, 'month':2, 'action':[('feed', 1)], 'time':2}
situation(not(len(playerlist)), playerlist)