year = int(input("年を入力してください。"))
month = int(input("月を入力してください。"))
day = int(input("日を入力してください。"))

if month == 1 or month ==2:
    year = year - 1
    month = month + 1

weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7


if weekday ==  0:
    w="日曜日"
elif weekday == 1:
    w="月曜日"
elif weekday == 2:
    w="火曜日"
elif weekday == 3:
    w="水曜日"
elif weekday == 4:
    w="木曜日"
elif weekday == 5:
    w="金曜日"
elif weekday == 6:
    w="土曜日"
else:
    print("うーん、うまくいかなかった。")

print("その日は",w,"です。")