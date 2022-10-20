def get_j_season(num):
    if num ==3 or num==4 or num==5:
        a="春"
    elif num==6 or num==7 or num==8:
        a="ふたりの夏物語"
    elif num==9 or num==10 or num==11:
        a="秋"
    else:
        a="冬"
    return a

num=int(input("季節を調べたい月を整数で入力してください。"))

val=get_j_season(num)
print(str(num)+"月は"+str(val)+"です。")