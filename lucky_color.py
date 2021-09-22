print("明日のラッキーカラーを占います！")

lucky_color = str(input("知りたいなと思ったら半角の'1'を入力してください："))

import random
num = random.randint(0,10)


if lucky_color == str(1):
    if num == 0:
        print("明日のラッキーカラーは赤です！")
    elif num == 1:
        print("明日のラッキーカラーは青です！")
    elif num == 2:
        print("明日のラッキーカラーは緑です！")
    elif num == 3:
        print("明日のラッキーカラーは黄色です！")
    elif num == 4:
        print("明日のラッキーカラーは紫です！")
    elif num == 5:
        print("明日のラッキーカラーは水色です！")
    elif num == 6:
        print("明日のラッキーカラーはピンクです！")
    elif num == 7:
        print("明日のラッキーカラーはオレンジです！")
    elif num == 8:
        print("明日のラッキーカラーは黄緑です！")
    elif num == 9:
        print("明日のラッキーカラーは白です！")
    elif num == 10:
        print("明日のラッキーカラーは黒です！")
else:
    print("半角の'1'を入力してください！")