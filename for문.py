def solution():
    for i in range(3):
        print('소미는커엽다')
# solution()

def solution1():
    for i in range(3):
        x=int(input("나이 몇?"))
        if x<13:
            print('신생아')
        elif x>13:
            print('늙음')
        else:
            print('칭구칭긔')
# solution1()


def solution2():
    for x in range(1,10):
        for i in range(1,10):
            print (x, "곱하기", i, "는", i*x)
# solution2()

def solution3():
    for i in range(ord('A'), ord("Z")+1, 1):
        for x in range(ord('A'), ord("Z")+1, 1):
            for n in range(ord('A'), ord("Z")+1, 1):
                print (chr(i), chr(x), chr(n))
# solution3()


def solution4():
    for i in range(1,4):
        for t in ["아침", "점심", "저녁"]:
            print(i,"일 ",t)
solution4()


