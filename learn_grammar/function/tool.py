# coding=utf-8
"""
存放需要的方法模块
"""
import learn_grammar.mapping.mapping_of_RPG_game as info
import time


def print_default_info(name, life, attack):
    """
    打印初始信息
    :return:
    """
    print(info.default_info.format(name, life, attack))


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


if __name__ == '__main__':
    player = {'name': '玩家', 'life': 50, 'attack': 50, 'point': 0}
    NPC = {'name': 'NPC', 'life': 49, 'attack': 51, 'point': 0}
    result = pk(player, NPC)
    final_result(result['玩家'], result['NPC'])