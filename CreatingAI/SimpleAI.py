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
chooseMove = {}

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
        global Game
        
        try :
            choices = PossibleMoves[Game]
            choose = random.choice(choices)
            try :
                chooseMove[Game].append(choose)
            except :
                chooseMove[Game] = [choose]
            print(choose)
            GameSYS.MakeMove(choose)
        except :
            tempGame, TGame = "", Game
            while (Game.find("/")+1) :
                tempGame += "/".join(reversed(Game[:3]))
                Game = Game[4:]
            tempGame = tempGame[1:]
            Game = TGame
            choices = PossibleMoves[tempGame]
            choose = random.choice(choices)

            lchoose = list(choose)
            
            for i in range(len(lchoose)) :
                if (lchoose[i]=='a') : lchoose[i]='c'
                if (lchoose[i]=='c') : lchoose[i]='a'
            
            choose = ''.join(lchoose)
            
            try :
                chooseMove[Game].append(choose)
            except :
                chooseMove[Game] = [choose]
            print(choose)
            GameSYS.MakeMove(choose)

while True :
    os.system('cls')
    while True :
        print(f"\n{Game[:3]}\n{Game[4:7]}\n{Game[8:]}")
        PlayerMove = input("What would you play? (originalS-NewS) : ")
        if not(GameSYS.PossibleMove(PlayerMove)) :
            while not(GameSYS.PossibleMove(PlayerMove)) :
                print("The following actions are not possible\nThe actions must be in this form\norignalSquare-NewSquare ex)a2-a3")
                PlayerMove = input("What would you play? (originalS-NewS) : ")
        
        print(PlayerMove)
        GameSYS.MakeMove(PlayerMove)

        GameSYS.CalculTheNextMove()