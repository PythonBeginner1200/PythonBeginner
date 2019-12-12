# coding=utf-8
"""
存放需要的方法模块
"""
import learn_grammar.mapping.mapping_of_RPG_game as info
import time
import random
import copy


def print_default_info(name1, life1, attack1, name2, life2, attack2):
    """
    打印初始信息
    :return:
    """
    print(info.default_info.format(name1, name2, name1, life1, attack1, name2, life2, attack2))


def print_PK_info(name1, name2, life):
    """
    打印PK过程中战斗信息
    :return:
    """
    print(info.PK_info.format(name1, name2, life))
    return


def print_game_info(game):
    """
    打印局数信息
    :return:
    """
    print(info.game_info.format(game))
    return


def pk(player1, player2):
    """
    pk过程
    :param player1: player {'name': '', 'life': , 'attack': }
    :param player2: NPC {'name': '', 'life': , 'attack': }
    :return: 该场比赛结果，play1赢返回1， play2赢返回-1，平局返回0
    """
    while player1['life'] > 0 and player2['life'] > 0:
        player2['life'] -= player1['attack']
        print(info.PK_info.format(player1['name'], player2['name'], player2['life']))
        player1['life'] -= player2['attack']
        print(info.PK_info.format(player2['name'], player1['name'], player1['life']))
        print('-----------------------------------')
        time.sleep(info.wait_short)
    if player1['life'] < 0 and player2['life'] > 0:
        print(info.fail_info)
        point = -1
        time.sleep(info.wait_long)
    elif player1['life'] > 0 and player2['life'] < 0:
        print(info.win_info)
        point = 1
        time.sleep(info.wait_long)
    else:
        print(info.draw_info)
        point = 0
    return point


def final_result(point):
    """
    记录最后结果
    :param
    :return:
    """
    if point > 0:
        print(info.final_win)
    elif point < 0:
        print(info.final_fail)
    else:
        print(info.final_draw)


def role_builder(role_list, game):
    """
    选取角色
    :param role_list: 角色池
    :param game: 局数
    :return:
    """
    roles = copy.deepcopy(random.sample(role_list, game))
    for i in range(0,len(roles)):
        print(info.role_info.format(roles[i]['name'], roles[i]['life'], roles[i]['attack']))
    print('-------------------------------------')
    return roles


def role_order_manual(roles, game):
    """
    玩家决定角色出场顺序
    :param roles: 角色池
    :param game: 局数
    :return:
    """
    sorted_roles = []
    for role in roles:
        if len(roles) > 1:
            role['order'] = int(input('你想将{}放在第几个上场(请输入1~{})：'.format(role['name'], game)))
            print('---------------------------------------')
            print('我方的出场顺序是：', end='')
    for i in range(1, game+1):
        for role in roles:
            if role['order'] == i:
                sorted_roles.append(role)
                print(role['name'], end='')
    print('')
    return sorted_roles


def role_order_auto(roles, game):
    """
    为NPC决定出场顺序
    :param roles: role list
    :param game: 局数
    :return:
    """
    sorted_roles = []
    order_list = list(range(1, game+1))
    for role in roles:
        role_index = random.sample(order_list, 1)[0]
        role['order'] = role_index
        order_list.remove(role_index)
    print('敌方的出场顺序是：', end='')
    for i in range(1, game+1):
        for role in roles:
            if role['order'] == i:
                sorted_roles.append(role)
                print(role['name'], end='')
    print('')
    print('')
    return sorted_roles




if __name__ == '__main__':
    # player = role_builder(info.role_list, 3)
    computer = role_builder(info.role_list, 3)
    # print(role_order_manual(player, 3))
    print(role_order_auto(computer, 3))
    # print(info.role_list)
    # list1 = [{'a': 0}, {'b': 1}, {'c': 2}]
    # # list1 = [0,10,2]
    # list2 = random.sample(list1,2)
    # list3 = copy.deepcopy(list2)
    # list3[list3.index({'c': 2})]['c'] = 9
    # print(list3)
    # print(list2)
    # print(list1)