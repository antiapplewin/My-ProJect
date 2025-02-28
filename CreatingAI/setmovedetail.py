class SetMoveDetail :
    def PawnMove(chess_board, x, y, turn) :
        if turn =="W" :
            if (type == "P") :
                selPos = (x, y)
                try :
                    if (chess_board[x-1][y]=='') :
                        selected[(y, x-1)] = "s"
                        if (chess_board[x-2][y]=='' and x==6) :
                            selected[(y, x-2)] = 's'
                except IndexError :
                    turn = turn

                try  :
                    if (chess_board[x-1][y+1] in BlackPiece) :
                        selected[(y+1, x-1)] = 'S'
                except IndexError :
                    turn = turn

                try :
                    if (chess_board[x-1][y-1] in BlackPiece) :
                        selected[(y-1, x-1)] = 'S'
                except IndexError :
                    turn = turn
        
        if turn == "B" :
            if (type == "p") :
                selPos = (x, y)
                try :
                    if (chess_board[x+1][y]=='') :
                        selected[(y, x+1)] = "s"
                        if (chess_board[x+2][y]=='' and x==1) :
                            selected[(y, x+2)] = 's'
                except IndexError :
                    turn = turn

                try  :
                    if (chess_board[x+1][y+1] in WhitePiece) :
                        selected[(y+1, x+1)] = 'S'
                except IndexError :
                    turn = turn

                try :
                    if (chess_board[x+1][y-1] in WhitePiece) :
                        selected[(y-1, x+1)] = 'S'
                except IndexError :
                    turn = turn