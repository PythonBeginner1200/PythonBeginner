"""
Small_RPG_game 1.1
1. 比赛三局，角色属性随机
2. 打出比赛最终结果
3. 可选择再战一次

Small_RPG_game 2.0（计划）
1. 每场比赛玩家和NPC均拥有三个不同角色，共三局
2. 每个角色属性不同，即血量和攻击力不同，且固定
3. 玩家可自选角色出场顺序
4. NPC角色出场顺序随机
5. 最终print出比赛结果
"""
import learn_grammar.mapping.mapping_of_RPG_game as info
import learn_grammar.function.tool as tool
import time
import random


def npc_game():
    """
    游戏主程序
    :return:
    """
    play_again = True
    while play_again:
        score = 0
        for game in range(1, 4):
            player1 = {'name': '玩家', 'life': random.randint(180, 200), 'attack': random.randint(80, 100)}
            player2 = {'name': '敌人', 'life': random.randint(180, 200), 'attack': random.randint(80, 100)}
            tool.print_game_info(game)
            time.sleep(info.wait_short)
            tool.print_default_info(player1['name'], player1['life'], player1['attack'])
            time.sleep(info.wait_short)
            tool.print_default_info(player2['name'], player2['life'], player2['attack'])
            time.sleep(info.wait_short)
            point = tool.pk(player1, player2)
            score += point
        tool.final_result(score)
        if input('想再来一盘么？（是/否）') == '否':
            play_again = False
    return

if __name__ == '__main__':
    npc_game()

