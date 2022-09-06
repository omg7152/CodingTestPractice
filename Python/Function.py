# 함수
balance = 0

def open_account():
    print("계좌생성 완료.")

def deposit(balance, money):
    type = "입금"
    addmoney = money
    if money < 0:
        type = "출금"
        if balance < money * -1:
            print("잔액이 부족합니다. 잔액 : " + str(balance))
            return 0

    print(str(money) + "원이 " + type + "되었습니다. 잔액 : " + str(balance + addmoney))
    return balance + addmoney

open_account()
balance = deposit(balance, 10000)
balance = deposit(balance, -100000)


# 함수(기본값)
def profile(name, age = 27, main_lang = "Python"):
    print(name + "\t" + str(age) + "\t" + main_lang)

profile("안세웅")
profile("이찬형")


# 함수(키워드)
def profile(name, age, main_lang):
    print(name + "\t" + str(age) + "\t" + main_lang)

profile("안세웅", main_lang = "Java", age = 27)
profile(age = 27, name = "이찬형", main_lang = "Python")


# 함수(가변인자)
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(name + "\t" + str(age) + "\t", end = " ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("안세웅", 27, "Java", "Python", "C", "C++", "C#")

def profile2(name, age, *language):
    print(name + "\t" + str(age) + "\t", end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile2("안세웅", 27, "Java", "Python", "C", "C++", "C#", "Swift")




