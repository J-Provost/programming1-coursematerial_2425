def multiple_choice(right_answer, given_answer):
    if given_answer==None:
        return 0
    if given_answer==right_answer:
        return 1
    else:
        return -0.2