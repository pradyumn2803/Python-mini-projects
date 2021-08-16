import random
import time


def play():
    print("Lets start the game ")
    print()
    n = 0
    x = 0
    z = 0
    d = 0
    print("\n")
    while n < 3:
        print(f"{k} vs computer round {n+1}:")
        p = input("s for snake, w for water, g for gun ")
        game = ["s", "w", "g"]
        c = random.choice(game)
        if c == "s" and p == "w":
            x += 1
            print(f"computer chose {c}")
            print("oops try again")
        elif c == "w" and p == "s":
            z += 1
            print(f"computer chose {c}")
            print("well done you earned one point")
        elif c == "s" and p == "g":
            z += 1
            print(f"computer chose {c}")
            print("well done you earned one point")
        elif c == "g" and p == "s":
            x += 1
            print(f"computer chose {c}")
            print("oops try again")
        elif c == "w" and p == "g":
            x += 1
            print(f"computer chose {c}")
            print("oops try again")
        elif c == "g" and p == "w":
            z += 1
            print(f"computer chose {c}")
            print("well done you earned one point")
        elif c == "s" and p == "s" or c == "w" and p == "w" or c == "g" and p == "g":
            x += 0
            z += 0
            print(f"computer chose {c}")
            print("no point")
        else:
            while d < 3:
                print("invalid input")
                d += 1
                break
        n += 1
    if d == 3:
        print("Results cannot be produced")
        print("your score= NA")
        print("computer score= NA")
    else:
        points(x, z)


def play_1():
    n = 0
    x = 0
    z = 0
    d = 0
    while n < 3:
        print("\n")
        print(f"Adam vs Eve Round {n+1} begins: ")
        game = ["s", "w", "g"]
        c = random.choice(game)
        p = random.choice(game)
        print("\n")
        print("s for snake, w for water, g for gun ")
        if c == "s" and p == "w":
            x += 1
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("Adam wins this round")
            time.sleep(3)
        elif c == "w" and p == "s":
            z += 1
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("Eve wins wins this round")
            time.sleep(3)
        elif c == "s" and p == "g":
            z += 1
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("Eve wins wins this round")
            time.sleep(3)
        elif c == "g" and p == "s":
            x += 1
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("Adam wins wins this round")
            time.sleep(3)
        elif c == "w" and p == "g":
            x += 1
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("Adam wins wins this round")
            time.sleep(3)
        elif c == "g" and p == "w":
            z += 1
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("Eve wins wins this round")
            time.sleep(3)
        elif c == "s" and p == "s" or c == "w" and p == "w" or c == "g" and p == "g":
            x += 0
            z += 0
            print(f"Adam chose {c} \n"
                  f"Eve chose {p}")
            print("no one wins this round")
            time.sleep(3)
        else:
            while d < 3:
                print("invalid input")
                d += 1
                break
        n += 1
    if d == 3:
        print("Results cannot be produced")
        print("Adam score= NA")
        print("Eve score= NA")
    else:
        points_1(x, z)


def points(pp1, pp2):
    print("\n")
    print("the final scores are ")
    print("computer score= ", pp1)
    print(f"{k} score=", pp2)
    if pp1 > pp2:
        print("you lost")
    elif pp1 == pp2:
        print("draw")
    else:
        print("you win ")


def points_1(pp1, pp2):
    print("\n")
    print("the final scores are ")
    print("Adam= ", pp1)
    print("Eve=", pp2)
    if pp1 > pp2:
        print("Adam wins this game")
    elif pp1 == pp2:
        print("draw")
    else:
        print("Eve wins this game ")


def start(e):
    if e == 1:
        global k
        k = input("Enter your name \n")
        print(f"welcome {k}")
        play()
    elif e == 2:
        play_1()


print("welcome to snake water gun gameplay")
print("Press 1 for player vs computer "
      "Press 2 for computer vs computer")
f = int(input())
start(f)


while True:
    print("Do you want to play again? y or n")
    o = input()
    if o == "y":
        print()
        print("welcome to snake water gun gameplay")
        print("Press 1 for player vs computer "
              "Press 2 for computer vs computer")
        f = int(input())
        start(f)
    else:
        break


print("thank you")
