import pygame

pygame.init()
pygame.display.set_caption("Menu")

screen = pygame.display.set_mode((720, 720))

done = False

BS = pygame.transform.scale(pygame.image.load("black_square.png"), (90, 90))
WS = pygame.transform.scale(pygame.image.load("white_square.png"), (90, 90))
images = {"p" : pygame.transform.scale(pygame.image.load("black_pawn.png"), (90, 90)), "P" : pygame.transform.scale(pygame.image.load("white_pawn.png"), (90, 90)),
          "b" : pygame.transform.scale(pygame.image.load("black_bishop.png"), (90, 90)), "B" : pygame.transform.scale(pygame.image.load("white_bishop.png"), (90, 90)),
          "n" : pygame.transform.scale(pygame.image.load("black_knight.png"), (90, 90)), "N" : pygame.transform.scale(pygame.image.load("white_knight.png"), (90, 90)),
          "r" : pygame.transform.scale(pygame.image.load("black_rook.png"), (90, 90)), "R" : pygame.transform.scale(pygame.image.load("white_rook.png"), (90, 90)),
          "q" : pygame.transform.scale(pygame.image.load("black_queen.png"), (90, 90)), "Q" : pygame.transform.scale(pygame.image.load("white_queen.png"), (90, 90)),
          "k" : pygame.transform.scale(pygame.image.load("black_king.png"), (90, 90)), "K" : pygame.transform.scale(pygame.image.load("white_king.png"), (90, 90)),
          "s" : pygame.transform.scale(pygame.image.load("select.png"), (90, 90)), "S" : pygame.transform.scale(pygame.image.load("select2.png"), (90, 90))}

chess_board = [[{'piece' : 'r', 'attack' : []}, {'piece' : 'n', 'attack' : []},{'piece' : 'b', 'attack' : []}, {'piece' : 'q', 'attack' : []},{'piece' : 'k', 'attack' : []}, {'piece' : 'b', 'attack' : []},{'piece' : 'n', 'attack' : []}, {'piece' : 'r', 'attack' : []}],
               [{'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}, {'piece' : 'p', 'attack' : []}],
               [{'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}],
               [{'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}],
               [{'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}],
               [{'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}, {'piece' : '', 'attack' : []}],
               [{'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}, {'piece' : 'P', 'attack' : []}],
               [{'piece' : 'R', 'attack' : []}, {'piece' : 'N', 'attack' : []},{'piece' : 'B', 'attack' : []}, {'piece' : 'Q', 'attack' : []},{'piece' : 'K', 'attack' : []}, {'piece' : 'B', 'attack' : []},{'piece' : 'N', 'attack' : []}, {'piece' : 'R', 'attack' : []}]]

BlackPiece = ["p", 'n', 'b', 'r', 'q', 'k']
WhitePiece = ["P", "N", "B", "R", "Q", "K"]

selected = {}
selPos = ()
turn = "W"
captured = False

class SetMoveDetail :
    def DeleteMove(x, y) :
        type = chess_board[x][y]['piece']
        pass

    def SetAtk(x, y) :
        type = chess_board[x][y]['piece']
        if (type=="P") :
            try :
                chess_board[x-1][y-1]['attack'].append(('P', 0, (x, y)))
            except :
                pass
            
            try :
                chess_board[x+1][y-1]['attack'].append(('P', 0, (x, y)))
            except :
                pass
        
        if (type=="p") :
            try :
                chess_board[x-1][y+1]['attack'].append(('p', 0, (x, y)))
            except :
                pass
            
            try :
                chess_board[x+1][y+1]['attack'].append(('p', 0, (x, y)))
            except :
                pass

        if (type=="N" or type == 'n') :
            PX = [2, -2, 1, -1]
            PY = [0, [2, -2], [1, -1]]
            for i in PX :
                for j in PY[abs(i)] :
                    try :
                        chess_board[x+i][y+i]['attack'].append((type, 0, (x, y)))
                    except :
                        pass

        if (type=="R" or type=="r") :
            i = 1
            rookMove = [True, True, True, True]
            blocked = [0, 0, 0, 0]
            while rookMove[0] or rookMove[1] or rookMove[2] or rookMove[3] :
                if rookMove[0] :
                    try :
                        chess_board[x+i][y]['attack'].append((type, blocked[0], (x, y)))
                        if (chess_board[x+i][y]['piece']!='') :
                            blocked[0]+=1
                    except IndexError :
                        rookMove[0] = False
                
                if rookMove[1] :
                    try :
                        chess_board[x-i][y]['attack'].append((type, blocked[1], (x, y)))
                        if (chess_board[x-i][y]['piece']!='') :
                            blocked[1]+=1
                    except IndexError :
                        rookMove[1] = False
                
                if rookMove[2] :
                    try :
                        chess_board[x][y+i]['attack'].append((type, blocked[2], (x, y)))
                        if (chess_board[x][y+i]['piece']!='') :
                            blocked[2]+=1
                    except IndexError :
                        rookMove[2] = False
                
                if rookMove[3] :
                    try :
                        chess_board[x][y-i]['attack'].append((type, blocked[3], (x, y)))
                        if (chess_board[x][y-i]['piece']!='') :
                            blocked[3]+=1
                    except IndexError :
                        rookMove[3] = False
                i+= 1

        if (type=="B" or type=='b') :
            i = 1
            BishopMove = [True, True, True, True]
            blocked = [0, 0, 0, 0]
            while BishopMove[0] or BishopMove[1] or BishopMove[2] or BishopMove[3] :
                if BishopMove[0] :
                    try :
                        chess_board[x+i][y+i]['attack'].append((type, blocked[0], (x, y)))
                        if (chess_board[x+i][y+i]['piece']!='') :
                            blocked[0]+=1
                    except IndexError :
                        BishopMove[0] = False
                
                if BishopMove[1] :
                    try :
                        chess_board[x-i][y-i]['attack'].append((type, blocked[1], (x, y)))
                        if (chess_board[x-i][y-i]['piece']!='') :
                            blocked[1]+=1
                    except IndexError :
                        BishopMove[1] = False
                
                if BishopMove[2] :
                    try :
                        chess_board[x-i][y+i]['attack'].append((type, blocked[2], (x, y)))
                        if (chess_board[x-i][y+i]['piece']!='') :
                            blocked[2]+=1
                    except IndexError :
                        BishopMove[2] = False
                
                if BishopMove[3] :
                    try :
                        chess_board[x+i][y-i]['attack'].append((type, blocked[3], (x, y)))
                        if (chess_board[x+i][y-i]['piece']!='') :
                            blocked[3]+=1
                    except IndexError :
                        BishopMove[3] = False
                i+= 1

        if (type=="Q" or type=='q') :
            i = 1
            rookMove = [True, True, True, True]
            BishopMove = [True, True, True, True]
            blocked = [0, 0, 0, 0, 0, 0, 0, 0]
            while rookMove[0] or rookMove[1] or rookMove[2] or rookMove[3] or BishopMove[0] or BishopMove[1] or BishopMove[2] or BishopMove[3] :
                if rookMove[0] :
                    try :
                        chess_board[x+i][y]['attack'].append((type, blocked[0], (x, y)))
                        if (chess_board[x+i][y]['piece']!='') :
                            blocked[0]+=1
                    except IndexError :
                        rookMove[0] = False
                
                if rookMove[1] :
                    try :
                        chess_board[x-i][y]['attack'].append((type, blocked[1], (x, y)))
                        if (chess_board[x-i][y]['piece']!='') :
                            blocked[1]+=1
                    except IndexError :
                        rookMove[1] = False
                
                if rookMove[2] :
                    try :
                        chess_board[x][y+i]['attack'].append((type, blocked[2], (x, y)))
                        if (chess_board[x][y+i]['piece']!='') :
                            blocked[2]+=1
                    except IndexError :
                        rookMove[2] = False
                
                if rookMove[3] :
                    try :
                        chess_board[x][y-i]['attack'].append((type, blocked[3], (x, y)))
                        if (chess_board[x][y-i]['piece']!='') :
                            blocked[3]+=1
                    except IndexError :
                        rookMove[3] = False

                if BishopMove[0] :
                    try :
                        chess_board[x+i][y+i]['attack'].append((type, blocked[0], (x, y)))
                        if (chess_board[x+i][y+i]['piece']!='') :
                            blocked[0]+=1
                    except IndexError :
                        BishopMove[0] = False
                
                if BishopMove[1] :
                    try :
                        chess_board[x-i][y-i]['attack'].append((type, blocked[1], (x, y)))
                        if (chess_board[x-i][y-i]['piece']!='') :
                            blocked[1]+=1
                    except IndexError :
                        BishopMove[1] = False
                
                if BishopMove[2] :
                    try :
                        chess_board[x-i][y+i]['attack'].append((type, blocked[2], (x, y)))
                        if (chess_board[x-i][y+i]['piece']!='') :
                            blocked[2]+=1
                    except IndexError :
                        BishopMove[2] = False
                
                if BishopMove[3] :
                    try :
                        chess_board[x+i][y-i]['attack'].append((type, blocked[3], (x, y)))
                        if (chess_board[x+i][y-i]['piece']!='') :
                            blocked[3]+=1
                    except IndexError :
                        BishopMove[3] = False
                i+=1

        if (type=="K" or type=='k') :
            moveKing = [(1, 1), (1, 0), (1, -1),
                    (0, 1), (0, -1),
                    (-1, 1), (-1, 0), (-1, -1)]

            for i in moveKing :
                try :
                    chess_board[x+i[0]][y+i[0]]['attack'].append(type, 0, (x, y))
                except IndexError :
                    pass

    def PawnMove(x, y) :
        global chess_board, selected, selPos, turn
        if turn =="W" :
            selPos = (x, y)
            try :
                if (chess_board[x-1][y]['piece']=='') :
                    selected[(y, x-1)] = "s"
                    if (chess_board[x-2][y]['piece']=='' and x==6) :
                        selected[(y, x-2)] = 's'
            except IndexError :
                turn = turn
            try  :
                if (chess_board[x-1][y+1]['piece'] in BlackPiece) :
                    selected[(y+1, x-1)] = 'S'
            except IndexError :
                turn = turn
            try :
                if (chess_board[x-1][y-1]['piece'] in BlackPiece) :
                    selected[(y-1, x-1)] = 'S'
            except IndexError :
                turn = turn
        
        if turn == "B" :
            selPos = (x, y)
            try :
                if (chess_board[x+1][y]['piece']=='') :
                    selected[(y, x+1)] = "s"
                    if (chess_board[x+2][y]['piece']=='' and x==1) :
                        selected[(y, x+2)] = 's'
            except IndexError :
                turn = turn
            try  :
                if (chess_board[x+1][y+1]['piece'] in WhitePiece) :
                    selected[(y+1, x+1)] = 'S'
            except IndexError :
                turn = turn
            try :
                if (chess_board[x+1][y-1]['piece'] in WhitePiece) :
                    selected[(y-1, x+1)] = 'S'
            except IndexError :
                turn = turn

    def KnightMove(x, y) :
        global chess_board, selected, selPos, turn
        selPos = (x, y)
        PX = [2, -2, 1, -1]
        PY = [0, [2, -2], [1, -1]]
        for i in PX :
            for j in PY[abs(i)] :
                try :
                    if (chess_board[x+i][y+j]['piece']=='') :
                        selected[(y+j, x+i)] = 's'
                    if (chess_board[x+i][y+j]['piece'] in BlackPiece)*(turn=='W') or (chess_board[x+i][y+j]['piece'] in WhitePiece)*(turn=='B') :
                        selected[(y+j, x+i)] = 'S'
                except IndexError :
                    turn = turn

    def RookMove(x, y) :
        global chess_board, selected, selPos, turn
        selPos = (x, y)
        # 최적화 필요

        i = 1
        rookMove = [True, True, True, True]
        while rookMove[0] or rookMove[1] or rookMove[2] or rookMove[3] :
            if rookMove[0] :
                try :
                    if (chess_board[x+i][y]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i][y]['piece'] in WhitePiece and turn=="B") :
                        selected[(y, x+i)] = "S"
                        rookMove[0] = False
                    elif (chess_board[x+i][y]['piece']=='') :
                        selected[(y, x+i)] = 's'
                    else :
                        rookMove[0] = False
                except IndexError :
                    rookMove[0] = False
            
            if rookMove[1] :
                try :
                    if (chess_board[x-i][y]['piece'] in BlackPiece and turn=="W") or (chess_board[x-i][y]['piece'] in WhitePiece and turn=="B") :
                        selected[(y, x-i)] = "S"
                        rookMove[1] = False
                    elif (chess_board[x-i][y]['piece']=='') :
                        selected[(y, x-i)] = 's'
                    else :
                        rookMove[1] = False
                except IndexError :
                    rookMove[1] = False
            
            if rookMove[2] :
                try :
                    if (chess_board[x][y+i]['piece'] in BlackPiece and turn=="W") or (chess_board[x][y+i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y+i, x)] = "S"
                        rookMove[2] = False
                    elif (chess_board[x][y+i]['piece']=='') :
                        selected[(y+i, x)] = 's'
                    else :
                        rookMove[2] = False
                except IndexError :
                    rookMove[2] = False
            
            if rookMove[3] :
                try :
                    if (chess_board[x][y-i]['piece'] in BlackPiece and turn=="W") or (chess_board[x][y-i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y-i, x)] = "S"
                        rookMove[3] = False
                    elif (chess_board[x][y-i]['piece']=='') :
                        selected[(y-i, x)] = 's'
                    else :
                        rookMove[3] = False
                except IndexError :
                    rookMove[3] = False
            i+= 1

    def BishopMove(x, y) :
        global chess_board, selected, selPos, turn
        selPos = (x, y) # 최적화 필요

        i = 1
        BishopMove = [True, True, True, True]
        while BishopMove[0] or BishopMove[1] or BishopMove[2] or BishopMove[3] :
            if BishopMove[0] :
                try :
                    if (chess_board[x+i][y+i]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i][y+i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y+i, x+i)] = "S"
                        BishopMove[0] = False
                    elif (chess_board[x+i][y+i]['piece']=='') :
                        selected[(y+i, x+i)] = 's'
                    else :
                        BishopMove[0] = False
                except IndexError :
                    BishopMove[0] = False
            
            if BishopMove[1] :
                try :
                    if (chess_board[x-i][y-i]['piece'] in BlackPiece and turn=="W") or (chess_board[x-i][y-i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y-i, x-i)] = "S"
                        BishopMove[1] = False
                    elif (chess_board[x-i][y-i]['piece']=='') :
                        selected[(y-i, x-i)] = 's'
                    else :
                        BishopMove[1] = False
                except IndexError :
                    BishopMove[1] = False
            
            if BishopMove[2] :
                try :
                    if (chess_board[x-i][y+i]['piece'] in BlackPiece and turn=="W") or (chess_board[x-i][y+i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y+i, x-i)] = "S"
                        BishopMove[2] = False
                    elif (chess_board[x-i][y+i]['piece']=='') :
                        selected[(y+i, x-i)] = 's'
                    else :
                        BishopMove[2] = False
                except IndexError :
                    BishopMove[2] = False
            
            if BishopMove[3] :
                try :
                    if (chess_board[x+i][y-i]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i][y-i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y-i, x+i)] = "S"
                        BishopMove[3] = False
                    elif (chess_board[x+i][y-i]['piece']=='') :
                        selected[(y-i, x+i)] = 's'
                    else :
                        BishopMove[3] = False
                except IndexError :
                    BishopMove[3] = False
            i+= 1

    def QueenMove(x, y) :
        global chess_board, selected, selPos, turn
        selPos = (x, y)
        # 최적화 필요

        i = 1
        rookMove = [True, True, True, True]
        BishopMove = [True, True, True, True]
        while rookMove[0] or rookMove[1] or rookMove[2] or rookMove[3] or BishopMove[0] or BishopMove[1] or BishopMove[2] or BishopMove[3] :
            if rookMove[0] :
                try :
                    if (chess_board[x+i][y]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i][y]['piece'] in WhitePiece and turn=="B") :
                        selected[(y, x+i)] = "S"
                        rookMove[0] = False
                    elif (chess_board[x+i][y]['piece']=='') :
                        selected[(y, x+i)] = 's'
                    else :
                        rookMove[0] = False
                except IndexError :
                    rookMove[0] = False
            
            if rookMove[1] :
                try :
                    if (chess_board[x-i][y]['piece'] in BlackPiece and turn=="W") or (chess_board[x-i][y]['piece'] in WhitePiece and turn=="B") :
                        selected[(y, x-i)] = "S"
                        rookMove[1] = False
                    elif (chess_board[x-i][y]['piece']=='') :
                        selected[(y, x-i)] = 's'
                    else :
                        rookMove[1] = False
                except IndexError :
                    rookMove[1] = False
            
            if rookMove[2] :
                try :
                    if (chess_board[x][y+i]['piece'] in BlackPiece and turn=="W") or (chess_board[x][y+i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y+i, x)] = "S"
                        rookMove[2] = False
                    elif (chess_board[x][y+i]['piece']=='') :
                        selected[(y+i, x)] = 's'
                    else :
                        rookMove[2] = False
                except IndexError :
                    rookMove[2] = False
            
            if rookMove[3] :
                try :
                    if (chess_board[x][y-i]['piece'] in BlackPiece and turn=="W") or (chess_board[x][y-i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y-i, x)] = "S"
                        rookMove[3] = False
                    elif (chess_board[x][y-i]['piece']=='') :
                        selected[(y-i, x)] = 's'
                    else :
                        rookMove[3] = False
                except IndexError :
                    rookMove[3] = False

            if BishopMove[0] :
                try :
                    if (chess_board[x+i][y+i]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i][y+i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y+i, x+i)] = "S"
                        BishopMove[0] = False
                    elif (chess_board[x+i][y+i]['piece']=='') :
                        selected[(y+i, x+i)] = 's'
                    else :
                        BishopMove[0] = False
                except IndexError :
                    BishopMove[0] = False
            
            if BishopMove[1] :
                try :
                    if (chess_board[x-i][y-i]['piece'] in BlackPiece and turn=="W") or (chess_board[x-i][y-i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y-i, x-i)] = "S"
                        BishopMove[1] = False
                    elif (chess_board[x-i][y-i]['piece']=='') :
                        selected[(y-i, x-i)] = 's'
                    else :
                        BishopMove[1] = False
                except IndexError :
                    BishopMove[1] = False
            
            if BishopMove[2] :
                
                try :
                    if (chess_board[x-i][y+i]['piece'] in BlackPiece and turn=="W") or (chess_board[x-i][y+i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y+i, x-i)] = "S"
                        BishopMove[2] = False
                    elif (chess_board[x-i][y+i]['piece']=='') :
                        selected[(y+i, x-i)] = 's'
                    else :
                        BishopMove[2] = False
                except IndexError :
                    BishopMove[2] = False
            
            if BishopMove[3] :
                try :
                    if (chess_board[x+i][y-i]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i][y-i]['piece'] in WhitePiece and turn=="B") :
                        selected[(y-i, x+i)] = "S"
                        BishopMove[3] = False
                    elif (chess_board[x+i][y-i]['piece']=='') :
                        selected[(y-i, x+i)] = 's'
                    else :
                        BishopMove[3] = False
                except IndexError :
                    BishopMove[3] = False

            i+=1

    def KingMove(x, y) :
        global chess_board, selected, selPos, turn
        selPos = (x, y)

        moveKing = [(1, 1), (1, 0), (1, -1),
                    (0, 1), (0, -1),
                    (-1, 1), (-1, 0), (-1, -1)]

        for i in moveKing :
            try :
                if (chess_board[x+i[0]][y+i[1]]['piece'] in BlackPiece and turn=="W") or (chess_board[x+i[0]][y+i[1]]['piece'] in WhitePiece and turn=="B") :
                    selected[(y+i[1], x+i[0])] = "S"
                elif (chess_board[x+i[0]][y+i[1]]['piece'] == '') :
                    selected[(y+i[1], x+i[0])] = 's'
            except IndexError :
                turn = turn

def TransSMD(x, y) :
    global chess_board
    type = chess_board[x][y]['piece']
    if (type == 'P' or type=='p') :
        SetMoveDetail.PawnMove(x, y)
    if (type == "N" or type=='n') :
        SetMoveDetail.KnightMove(x, y)
    if (type == 'B' or type=='b') :
        SetMoveDetail.BishopMove(x, y)
    if (type == "R" or type=='r') :
        SetMoveDetail.RookMove(x, y)
    if (type == 'Q' or type=='q') :
        SetMoveDetail.QueenMove(x, y)
    if (type == "K" or type=='k') :
        SetMoveDetail.KingMove(x, y)

def SetSelect(x, y) :
    global selected, selPos, turn
    captured =False

    if ((y, x) in selected) :
        chess_board[x][y]['piece'] = chess_board[selPos[0]][selPos[1]]['piece']
        chess_board[selPos[0]][selPos[1]]['piece'] = ''
        if (selected[(y, x)]!='') :
            captured = True

        if turn == "W" :
            turn = "B"
        else :
            turn = "W"

    selected.clear()
    selected.clear()

    type = chess_board[x][y]['piece']

    if (type in WhitePiece and turn == "W") or (type in BlackPiece and turn == 'B') :
        TransSMD(x, y)

    if captured :
        selected.clear()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            sY = int(mouseX/90)
            sX = int(mouseY/90)
            SetSelect(sX, sY)

    screen.fill("WHITE")

    for i in range(8) :
        for j in range(8) :
            if ((i+j)%2==0) :
                screen.blit(WS, [j*90, i*90])
            else :
                screen.blit(BS, [j*90, i*90])

    for i in range(8) :
        for j in range(8) :
            if chess_board[i][j]['piece']!="" :
                screen.blit(images[chess_board[i][j]['piece']], [j*90, i*90])

    for k, v in selected.items() :
        screen.blit(images[v], [k[0]*90, k[1]*90])


    pygame.display.flip()