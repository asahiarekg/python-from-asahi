# 今の年、月、日、時間、分を取得できるモジュールを呼び出す
import datetime
# モジュールのデータを変数に格納
dt_now = datetime.datetime.now()
# 今の年、月、日、時間、分をそれぞれ変数に格納
year = dt_now.year
month = dt_now.month
day = dt_now.day
hour = dt_now.hour
min = dt_now.minute
# 今の年、月、日、時間、分を画面に表示
print(year,"/",month,"/",day,"  ",hour,":",min,sep="")
#　時間によって挨拶を変える
if 4 <= hour and hour <= 7:
    print("おはようございます！早起きですね！今日も一日頑張りましょう。")
elif 8 <= hour and hour <= 10:
    print("おはようございます！今日も一日頑張りましょう。")
elif 11 <= hour and hour <=16:
    print("こんにちは！")
elif 17<= hour and hour <=20:
    print("こんばんは！")
elif 21<= hour and hour <= 0:
    print("こんばんは！今日も一日お疲れ様です。")
else:
    ("こんばんは！寝なくて平気ですか？")