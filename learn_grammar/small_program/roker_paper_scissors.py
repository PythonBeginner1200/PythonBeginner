import random

def result(a, b):
    if a == b:
        print('平局！')
    elif (a == '石头' and b == '剪刀') or (a == '剪刀' and b == '布') or (a == '布' and b == '石头'):
        print('电脑胜！')
    else:
        print('玩家胜！')


def main():
    again = 1
    choice_list = ['石头', '剪刀', '布']
    npc_choice = random.choice(choice_list)
    while again == 1:
        flag = 0
        while flag == 0:
            user_choice = input('石头, 剪刀, 布：')
            if user_choice not in choice_list:
                print('输入有误，请重新输入')
            else:
                flag = 1
        print('电脑：', npc_choice)
        print('你：', user_choice)
        result(npc_choice, user_choice)
        play_again = input('想再来一盘么？（是/否）')
        if play_again == '否' or play_again == 'N' or play_again == 'n':
            again = 0

if __name__ == '__main__':
    main()

