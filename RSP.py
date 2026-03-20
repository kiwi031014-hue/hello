import random

def play():
    hand = ['가위', '바위', '보']
    print("🎮 가위... 바위... 보! (그만하려면 '종료')")

    while True:
        com = random.choice(hand)
        user = input("\n나: ")

        if user == '종료': break
        if user not in hand:
            print("❌ 똑바로 내세요! 가위, 바위, 보 중에서만!")
            continue

        print(f"컴퓨터: {com}")

        if user == com:
            print("🔄 비겼네? 한 번 더 해, 쫄았니?")
        elif (user=='가위' and com=='보') or (user=='바위' and com=='가위') or (user=='보' and com=='바위'):
            print("✅ 올~ 운 좋게 이겼는데? 인정 안 함!")
        else:
            print("🔥 졌죠? 킹받죠? 아무것도 못 하죠?")

play()
