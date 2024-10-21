def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skipped=0
    if grade1==None:
        skipped+=1
        grade1=0
    if grade2==None:
        skipped+=1
        grade2=0
    if grade3==None:
        skipped+=1
        grade3=0
    if grade4==None:
        skipped+=1
        grade4=0
    if grade5==None:
        skipped+=1
        grade5=0
    if skipped==5:
        total= False
    else:
        total=((grade1+grade2+grade3+grade4+grade5)/(5-skipped))>=12
    skipped_total= skipped<=1
    return total and skipped_total