# write your code here
def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice==player2_choice:
        result=0
    elif player1_choice==0 and player2_choice==2:
        result=1
    elif player1_choice==1 and player2_choice==0:
        result=1
    elif player1_choice==2 and player2_choice==1:
        result=1
    else:
        result=2
    return result