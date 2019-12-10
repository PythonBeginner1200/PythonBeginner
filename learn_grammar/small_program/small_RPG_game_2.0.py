"""
Small_RPG_game 1.1
1. 比赛三局，角色属性随机
2. 打出比赛最终结果
3. 可选择再战一次

Small_RPG_game 2.0
1. 每场比赛玩家和NPC均拥有n个不同角色，共n局
2. 每个角色属性不同，即血量和攻击力不同，且固定
3. 玩家可自选角色出场顺序
4. NPC角色出场顺序随机
5. 最终print出比赛结果
"""
import learn_grammar.mapping.mapping_of_RPG_game as info
import learn_grammar.function.tool as tool
import time
import random


def rpg_game():
    """
    游戏主程序
    :return:
    """
    play_again = True
    games = int(input('你想玩几局比赛：'))
    while play_again:
        score = 0
        print('-----------------角色信息--------------------')
        print('你的人物')
        player = tool.role_builder(info.role_list, games)
        print('NPC人物')
        computer = tool.role_builder(info.role_list, games)
        input('请按回车键继续。')
        player = tool.role_order_manual(player, games)
        computer = tool.role_order_auto(computer, games)
        for game in range(1, games + 1):
            tool.print_game_info(game)
            time.sleep(info.wait_short)
            tool.print_default_info(player[game - 1]['name'], player[game - 1]['life'], player[game - 1]['attack'],
                                    computer[game - 1]['name'], computer[game - 1]['life'],
                                    computer[game - 1]['attack'])
            time.sleep(info.wait_short)
            point = tool.pk(player[game - 1], computer[game - 1])
            input('请按回车键继续。')
            score += point
        tool.final_result(score)
        again = input('想再来一盘么？（是/否）')
        if again == '否' or again == 'N' or again == 'n':
            play_again = False
    return


if __name__ == '__main__':
    rpg_game()
