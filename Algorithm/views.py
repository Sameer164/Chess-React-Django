from django.shortcuts import render

#HELLO
# Create your views here.


from stockfish import Stockfish
import chess
import chess.engine

def run(request, *args, **kwargs):


# this function will create our f(x) (score)
    def stockfish(board, depth):
        with chess.engine.SimpleEngine.popen_uci("stockfish_api/stockfish_14_x64_avx2.exe") as sf:
            result = sf.analyse(board, chess.engine.Limit(depth=depth))
            score = result['score'].white().score()
            return score


    def secondbestMove(legalmoves,board2):
        moves=[]
        analyzed_moves=[]
        for  move in range(len(legalmoves)):
            board3= board2.copy()
            board3.push_xboard(str(legalmoves[move]))
            if(stockfish(board3,10)!=None):
                moves.append(str(legalmoves[move]))
                analyzed_moves.append(stockfish(board3,10))

        zipped_moves=zip(analyzed_moves,moves)
        moves_dict = dict(zipped_moves)
        sorted_moves = list(moves_dict.keys())
        sorted_moves.sort()
        if len(sorted_moves)==1:
            return moves_dict[sorted_moves[0]]
        second_best_move = moves_dict[sorted_moves[-2]]
        return second_best_move




    board = chess.Board()
    def AnalyzeBoard(board):
        for i in range(100):
            if i%2!=0:
                second_best_move=secondbestMove(list(board.legal_moves),board)
                print("AI's move: "+second_best_move)
                board.push_xboard(second_best_move)
                print(board)
                print('')
                if list(board.legal_moves)[0] == 'null':
                    break
            if i%2==0:
                print(board.legal_moves)
                move=input('Enter your move: ')
                if(move=='exit'):
                    break
                board.push_xboard(str(move))
                if list(board.legal_moves)[0] == 'null':
                    break
        print('Game Over') 
    AnalyzeBoard(board)
    context  = {"board": board}


    return render(request, "Algorithm/hello.html", context)

    

