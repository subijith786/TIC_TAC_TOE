def printboard(xstate,zstate):
    zero="X" if xstate[0]==1 else ("O" if zstate[0]==1 else 0)
    one="X" if xstate[1]==1 else ('O' if zstate[1]==1 else 1)
    two="X" if xstate[2]==1 else ('O' if zstate[2]==1 else 2)
    three="X" if xstate[3]==1 else ('O' if zstate[3]==1 else 3)
    four="X" if xstate[4]==1 else ('O' if zstate[4]==1 else 4)
    five="X" if xstate[5]==1 else ('O' if zstate[5]==1 else 5)
    six="X" if xstate[6]==1 else ('O' if zstate[6]==1 else 6)
    seven="X" if xstate[7]==1 else ('O' if zstate[7]==1 else 7)
    eight="X" if xstate[8]==1 else ('O' if zstate[8]==1 else 8)
    print(f'    {zero} | {one} | {two} ')
    print(f'   ---|---|---')
    print(f'    {three} | {four} | {five} ')
    print(f'   ---|---|---')
    print(f'    {six} | {seven} | {eight} ')
def sum1(a,b,c):
    return a+b+c
def checkwin():
    win=[[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[2,4,6],[6,7,8],[3,4,5]]
    for i in win:
        if sum1(xstate[i[0]],xstate[i[1]],xstate[i[2]])==3:
            return 1
        elif sum1(zstate[i[0]],zstate[i[1]],zstate[i[2]])==3:
            return 0



xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]
turn=1
print('WELCOME TO TIC-TAC-TOE')
print('THE PLAYER WANT TO SELECT A VALUE ACCORDINGLY TO PLAY')
n=1
while True:
    printboard(xstate,zstate)
    if turn==1:
        print("X's TURN")
        value=int(input('ENTER THE VALUE:'))
        if zstate[value]==0 and xstate[value]==0:
            xstate[value]=1
        else:
            print("PLAYER X LOST THE TURN")
    else:
        print("O's TURN")
        value=int(input('ENTER THE VALUE:'))
        if xstate[value]==0 and zstate[value]==0:
            zstate[value]=1
        else:
            print("PLAYER O LOST THE TURN")
    if checkwin()==1:
        printboard(xstate,zstate)
        print('X wins the match')
        break
    elif checkwin()==0:
        printboard(xstate,zstate)
        print('O wins the match')
        break
    elif sum(xstate)+sum(zstate)==9:
        printboard(xstate, zstate)
        print('THE MATCH IS TIE')
        break

    n += 1
    turn = 1 - turn








