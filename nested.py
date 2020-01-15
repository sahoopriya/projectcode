report_card=[]
score_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        report_card+=[[name,score]]
        score_list+=[score]

    p=list(set(score_list))
    b=sorted(p)[1] 
    for a,c in sorted(report_card):
            if c==b:
                print(a)
