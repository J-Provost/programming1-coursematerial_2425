# write your code here
def passing_percentage(grades):
    passed=0
    failed=0
    for grade in grades:
        if grade>=10:
            passed+=1
    if passed==0:
        return 0
    result=passed/len(grades)*100
    return result
