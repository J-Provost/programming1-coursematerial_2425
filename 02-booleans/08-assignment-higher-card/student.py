# write your code here
def higher_card(card1, card2):
    higher=card2 != 1 and card1>card2
    ace_1= card1==1 and card2!=1
    return higher or ace_1