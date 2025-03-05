import random, os

PossibleMoves = {"BBB/W--/-WW":["c3-c2", "b3-a2", 'b3-b2'], "BBB/-W-/W-W":["a3-a2", "a3-b2", "c3-c2", 'c3-b2'],
                 "B-B/BW-/--W":["a2-a1", 'a3-b2', 'c3-b2', 'c3-c2'], "-BB/WB-/--W":["b3-a2", 'b2-b1', 'c3-c2'],
                 "B-B/WW-/-W-":['a3-b2', 'c3-b2', 'c3-c2'], "BB-/W-W/--W":['b3-b2', 'b3-a2', 'b3-c2'],
                 "-BB/-BW/W--":['b2-a1', 'b2-a2', 'b3-c2'], "-BB/BWW/W--":['b3-c2', 'c3-b2'], "B-B/B-W/-W-":['a2-a1', 'a2-b1'],
                 '-BB/-W-/--W':['c3-b2', 'c3-c2'], "-BB/-W-/W--":['c3-b2', 'c3-c2'], 'B-B/W--/--W':['c3-c2'],
                 '--B/BBW/---':['a2-a1', 'b2-b1'],"B--/WWW/---":['a3-b2'], "-B-/BWW/---":['b3-c2', 'a2-a1'],
                 'B--/BBW/---':['a2-a1', 'b2-b1'],'--B/BW-/---':['a2-a1', 'c3-b2', 'c3-c2'], "-B-/WB-/---":['b3-a2', 'b2-b1'],
                 'B--/BW-/---':['a3-b2', 'a2-a1']}

Game = "BBB/---/WWW"
currentMove = ()
Uwin, Bwin = 0, 0

class GameSYS :
    def PossibleMove(move) :
        global Game
        index = 0
        if (move[1]=='1') : index = 10
        if (move[1]=='2') : index = 6
        if (move[0]=='a') : index -= 2
        if (move[0]=='b') : index -= 1

        if (Game[index]!='W') :
            return False

        addtion = {'a':1, 'b':2, 'c':3}
        
        if (move[3]==move[0] and Game[index-4]!='-') : return False
        if (move[3]!=move[0] and Game[index-4+addtion[move[3]]-addtion[move[0]]]!='B') : return False

        return True
    
    def MakeMove(move) :
        global Game
        index = 0

        if (move[1]=='3') : index = 2
        if (move[1]=='1') : index = 10
        if (move[1]=='2') : index = 6
        if (move[0]=='a') : index -= 2
        if (move[0]=='b') : index -= 1

        newIndex = 0

        if (move[4]=='3') : newIndex = 2
        if (move[4]=='2') : newIndex = 6
        if (move[4]=='1') : newIndex = 10
        if (move[3]=='a') : newIndex -= 2
        if (move[3]=='b') : newIndex -= 1

        lGame = list(Game)
        lGame[newIndex] = lGame[index]
        lGame[index]='-'
        Game = ''.join(lGame)

    def CalculTheNextMove() :
        global Game, currentMove
        
        try :
            choices = PossibleMoves[Game]
            choose = random.choice(choices)
            currentMove = (Game, choose)
            print(choose)
            GameSYS.MakeMove(choose)
        except :
            tempGame, TGame = "", Game
            str1, str2, str3 = "".join(reversed(Game[:3])), "".join(reversed(Game[4:7])), "".join(reversed(Game[8:]))
            tempGame = str1+"/"+str2+"/"+str3
            Game = TGame
            choices = PossibleMoves[tempGame]
            choose = random.choice(choices)

            currentMove = (tempGame, choose)

            tchoose = ""
            
            for i in range(len(choose)) :
                if (choose[i]=='a') : tchoose+='c'
                elif (choose[i]=='c') : tchoose+='a'
                else : tchoose += choose[i]
            
            choose = ''.join(tchoose)
            
            print(choose)
            GameSYS.MakeMove(choose)
    
    def DidWon(turn) :
        global Game
        revT = {'B':'W', 'W':'B'}
        indexs = []
        for i in range(len(Game)) :
            if (Game[i]==turn) :
                indexs.append(i)
            if Game[i]==revT[turn] :
                if (0<=i and i<3 and turn == 'B') :
                    return 'W'
                if (8<=i and turn=="W") :
                    return "B"

        if (indexs==[]) :
            return revT[turn]
        
        cantmoveCNT = 0

        if turn=='W' :
            for index in indexs :
                if (Game[index-4]!='-') :
                    try :
                        if (Game[index-5]!='/') :
                            if (Game[index-5]!='B') :
                                cantmoveCNT+=0.5
                        else : cantmoveCNT+=0.5
                    except :
                        cantmoveCNT+=0.5
                    try :
                        if (Game[index-3]!='/') :
                            if (Game[index-3]!='B') :
                                cantmoveCNT+=0.5
                        else : cantmoveCNT+=0.5
                    except :
                        cantmoveCNT+=0.5
        else :
            for index in indexs :
                if (Game[index+4]!='-') :
                    try :
                        if (Game[index+5]!='/') :
                            if (Game[index+5]!='W') :
                                cantmoveCNT+=0.5
                        else : cantmoveCNT+=0.5
                    except :
                        cantmoveCNT+=0.5
                    try :
                        if (Game[index+3]!='/') :
                            if (Game[index+3]!='W') :
                                cantmoveCNT+=0.5
                        else : cantmoveCNT+=0.5
                    except :
                        cantmoveCNT+=0.5

        if cantmoveCNT == len(indexs) :
            return revT[turn]
        
        return "N"

    def DelMove() :
        global currentMove, PossibleMoves

        PossibleMoves[currentMove[0]].remove(currentMove[1])

won = ""

while True :
    os.system('cls')
    if (won=="W") :
        print("You had won the last game")
        GameSYS.DelMove()
        currentMove = ()
        Uwin+= 1
    elif (won=='B') :
        print("Bot had won the last game")
        Bwin += 1
    Game = "BBB/---/WWW"
    try :
        print(f"U : {int(Uwin/(Uwin+Bwin)*10000)/100}% / B : {int(Bwin/(Uwin+Bwin)*10000)/100}%")
    except :
        print("U : -% / B : -%")
    while True :
        print(f"\n{Game[:3]}\n{Game[4:7]}\n{Game[8:]}")
        PlayerMove = input("What would you play? (originalS-NewS) : ")
        if not(GameSYS.PossibleMove(PlayerMove)) :
            while not(GameSYS.PossibleMove(PlayerMove)) :
                print("The following actions are not possible\nThe actions must be in this form\norignalSquare-NewSquare ex)a2-a3")
                PlayerMove = input("What would you play? (originalS-NewS) : ")
        
        os.system('cls')
        print(PlayerMove)
        GameSYS.MakeMove(PlayerMove)

        won = GameSYS.DidWon("B")

        if (won=='W') :
            print("Player Won!")
            break

        GameSYS.CalculTheNextMove()

        won = GameSYS.DidWon("W")

        if (won=='B') :
            print("Bot Won!")
            break