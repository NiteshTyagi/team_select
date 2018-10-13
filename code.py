from random import choice

print('LET\'S PLAY GAME THAT CREATE 2 TEAM RANDOMLY\n'.center(70,'*'))

playernumber=int(input("ENTER THE NUMBER OF THE PLAYERS:\n"))

print("NOW ENTER THE NAME OF THE PLAYER NAMES:\n")
players=[]
for i in range(playernumber):
    players.append(input())


teamnumber=int(input("\nENTER THE NUMBER OF THE TEAM:"))
team=[]
for i in range(teamnumber):
    team.append(input())

print('\nPlayers:',players,)
print('Teams:',team,'\n')

choice1=int(input('ENTER THE NUMBER OF THE PLAYERS WHO WANT IN YOUR TEAM,MUST BE LESS THAN THE TOTAL NUMBER OF THE PLAYERS'))

if choice1<playernumber:
    selectplayer=[]
    for i in range(choice1):
        player=choice(players)
        selectplayer.append(player)
        players.remove(player)
    selectteam=choice(team)
    print("HERE IS YOUR TEAM".center(70,'*'))
    print(selectteam,':',selectplayer)
    team.remove(selectteam)
    
    print(choice(team),":",players)
else:
    print("PLEASE ENTER THE TEAM SIZE LESS THAN TOTAL NUMBER OF PLAYERS")

