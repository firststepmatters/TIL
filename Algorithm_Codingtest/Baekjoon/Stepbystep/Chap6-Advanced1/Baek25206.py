import sys
input = sys.stdin.readline
gradetable = {'A+':4.5, 'A0':4, 'B+':3.5,'B0':3,'C+':2.5,'C0':2,'D+':1.5,'D0':1,'F':0}
score_sum = 0
grade_sum = 0
while 1 == 1:
    aaa = input()
    if aaa == "" : break
    a, score, grade = aaa.split()
    if grade == "P" : continue
    score_sum += float(score)
    grade_sum += float(gradetable[grade])*float(score)
    
print(grade_sum/score_sum)


'''
match-case 를 사용할수도 있군. 
나는 딕셔너리를 사용함
'''