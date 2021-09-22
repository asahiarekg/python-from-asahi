print("明日の東京都の天気を予想します！")

weather_tk = str(input("知りたくなったら半角の'1'を入力してください："))

import random
num = random.randint(0,7)

if weather_tk == str(1):
    if num == 0:
        print("明日の東京都の天気は晴れだと思います！いぇい！")
    elif num == 1:
        print("明日の東京都の天気は曇りだと思います！涼しい！")
    elif num == 2:
        print("明日の東京都の天気は雨だと思います！傘を忘れずに！")
    elif num == 3:
        print("明日の東京都の天気は嵐だと思います！気を付けてください！")
    elif num == 4:
        print("明日の東京都の天気は台風だと思います！気を付けてください！")
    elif num == 5:
        print("明日の東京都の天気は雪だと思います！滑らないように気を付けてください！")
    elif num == 6:
        print("明日の東京都の天気は快晴だと思います！熱中症に気を付けてください！")
    elif num == 7:
        print("明日の東京都の天気は雷だと思います！家にいてください！")
else:
    print("半角の'1'を入力してください！")