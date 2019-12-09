# coding=utf-8
"""
随机生成玩家和敌人的血量和攻击力，互相攻击会减去血量，任意一方血量小于0则游戏结束
血量范围为1到200，攻击范围为1到50
"""
import random
import time


play_again = True
while play_again:
    score = 0
    for game in range(1, 4):
        print('——————————现在是第{}局——————————'.format(game))
        time.sleep(1.5)
        player = {'name': '玩家', '血量': random.randint(100, 200), '攻击': random.randint(1, 100)}
        NPC = {'name': '敌人', '血量': random.randint(100, 200), '攻击': random.randint(1, 100)}
        print("""【{}】\n血量: {}\n攻击: {}\n----------------------""".format(player['name'], player['血量'], player['攻击']))
        time.sleep(1.5)
        print("""【{}】\n血量: {}\n攻击: {}\n----------------------""".format(NPC['name'], NPC['血量'], NPC['攻击']))
        time.sleep(1.5)
        while player['血量'] > 0 and NPC['血量'] > 0:
            player['血量'] -= NPC['攻击']
            NPC['血量'] -= player['攻击']
            print("""敌人发起了攻击，【玩家】剩余血量{}\n你发起了攻击，【敌人】剩余血量{}""".format(player['血量'], NPC['血量']))
            time.sleep(1.5)
        if player['血量'] < 0 and NPC['血量'] > 0:
            print('悲催，敌人把你干掉了！')
            time.sleep(3)
            score -=1
        elif player['血量'] > 0 and NPC['血量'] < 0:
            print('恭喜你，战胜了敌人！')
            time.sleep(3)
            score +=1
        else:
            print('还好，平局')
        print(score)
    if score < 0:
        print('【最终结果：你输了！】')
    elif score > 0:
        print('【最终结果：你赢了！】')
    else:
        print('【最终结果：平局！】')
    if input('想再来一盘么？（是/否）') == '否':
        play_again = False
