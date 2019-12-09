"""
存放需要的方法模块
"""
import learn_grammar.mapping.mapping_of_RPG_game as m
import time


def print_default_info(name, life, attack):
    """
    打印初始信息
    :return:
    """
    print(m.default_info.format(name, life, attack))


def print_PK_info(name1, name2, life):
    """
    打印PK过程中战斗信息
    :return:
    """
    print(m.PK_info.format(name1, name2, life))
    return


def print_game_info(game):
    """
    打印局数信息
    :return:
    """
    print(m.game_info.format(game))
    return


def pk(player1, player2):
    """
    pk过程
    :param player1: player {'name': '', 'life': , 'attack': , 'point': 0}
    :param player2: NPC {'name': '', 'life': , 'attack': , 'point': 0}
    :return:
    """
    while player1['life'] > 0 and player2['life'] > 0:
        player2['life'] -= player1['attack']
        print(m.PK_info.format(player1['name'], player2['name'], player2['life']))
        player1['life'] -= player2['attack']
        print(m.PK_info.format(player2['name'], player1['name'], player1['life']))
        print('-----------------------------------')
        time.sleep(1.5)
    if player1['life'] < 0 and player2['life'] > 0:
        print(m.fail_info)
        time.sleep(3)
        player2['point'] += 1
    elif player1['life'] > 0 and player2['life'] < 0:
        print(m.win_info)
        time.sleep(3)
        player1['point'] += 1
    else:
        print(m.draw_info)
    result = {player1['name']:player1['point'], player2['name']:player2['point']}
    return result


def final_result(point1, point2):
    """
    记录最后结果
    :param point1: player points
    :param point2: NPC points
    :return:
    """
    if point1 > point2:
        print(m.final_win)
    elif point1 < point2:
        print(m.final_fail)
    else:
        print(m.final_draw)


if __name__ == '__main__':
    player = {'name': '玩家', 'life': 50, 'attack': 50, 'point': 0}
    NPC = {'name': 'NPC', 'life': 49, 'attack': 51, 'point': 0}
    result = pk(player, NPC)
    final_result(result['玩家'], result['NPC'])