from random import randint

def numberGame():
    # 1から100の間にある数字を1つ選択する
    number = randint(1, 100)

    print("1から100までのどれかを推測しています")
    guess = int(input("いくつだと思いますか？"))

    while guess:
        if number == guess:
            print("正解です！答えは", number, "でした")
            break
        elif number > guess:
            print("違います。もっと大きいです。")
        else:
            print("違います。もっと小さいです。")
        guess = int(input("いくつだと思いますか？"))

numberGame()
   