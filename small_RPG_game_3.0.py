"""
Small_RPG_game 3.0
1. 把游戏作为类封装
2. 添加属性克制
"""
import learn_grammar.mapping.mapping_of_RPG_game as info
import learn_grammar.function.tool as tool
import time
import random
import copy


class Role():
    def __init__(self, name):
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)

    def my_info(self):
        print('【我方】 【{}】    血量：{}   攻击：{}'.format(self.name, self.life, self.attack))

    def npc_info(self):
        print('【敌方】 【{}】    血量：{}   攻击：{}'.format(self.name, self.life, self.attack))


class Knight(Role):
    """
    子类 “【圣光骑士】” (英文是Knight)
    血量是随机数的5倍大小，攻击力是随机数的3倍大小
    遇到暗影刺客攻击增加50%
    """

    def __init__(self, name):
        Role.__init__(self, name)
        self.life = self.life * 5
        self.attack = self.attack * 3

    def attack_buff(self, enermy_name):
        if enermy_name == '【暗影刺客】':
            self.attack *= 1.5
            print('【圣光骑士】对【暗影刺客】说：“让无尽光芒制裁你的堕落！”')


class Assassin(Role):
    """
    子类 “【暗影刺客】” (英文是Assassin)
    血量是随机数的3倍大小，攻击力是随机数的5倍大小
    遇到精灵弩手攻击增加50%
    """

    def __init__(self, name):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5

    def attack_buff(self, enermy_name):
        if enermy_name == '【精灵弩手】':
            self.attack *= 1.5
            print('【暗影刺客】对【精灵弩手】说：“主动找死，就别怪我心狠手辣。”')


class Bowman(Role):
    """
    子类 “【精灵弩手】” (英文是Bowman)
    血量是随机数的4倍大小，攻击力是随机数的4倍大小
    遇到圣光骑士攻击增加50%
    """

    def __init__(self, name):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4

    def attack_buff(self, enermy_name):
        if enermy_name == '【圣光骑士】':
            self.attack *= 1.5
            print('【精灵弩手】对【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。”')


class Game():

    def __init__(self):
        print('--------------------欢迎来到“炼狱角斗场”--------------------')
        print('''在昔日的黄昏山脉，奥卢帝国的北境边界上，有传说中的“炼狱角斗场”。
鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！
今日，只要【你的队伍】能取得胜利，你将获得一笔够花500年的财富。
将随机生成【你的队伍】和【敌人队伍】！
            ''')
        input('狭路相逢勇者胜，请按回车继续')
        print('')

    def my_info(self):
        print('--------------------角色信息--------------------')
        print('你的队伍')

    def npc_info(self):
        print('--------------------角色信息--------------------')
        print('敌人队伍')

    def teams(self, role_list, number):
        """
        随机生成角色数量为number的角色list
        :param role_list: list
        :param number: how many games you want to play
        :return: 生成的角色对象list
        """
        team = []
        name_list = copy.deepcopy(role_list)
        for i in range(1, number + 1):
            name = random.choice(name_list)
            if name == '【圣光骑士】':
                role = Knight(name)
            elif name == '【暗影刺客】':
                role = Assassin(name)
            elif name == '【精灵弩手】':
                role = Bowman(name)
            else:
                role = Role(name)
            team.append(role)
            name_list.remove(role.name)
        return team


def game_start():
    player_list = ['【暗影刺客】', '【精灵弩手】', '【圣光骑士】']
    game = Game()
    my_team = game.teams(player_list, 3)
    npc_team = game.teams(player_list, 3)
    game.my_info()
    for i in my_team:
        i.my_info()
    game.npc_info()
    for i in npc_team:
        i.npc_info()
    print('------------------------------------------------')
    input('请按回车键继续。')
    print('')
    return my_team, npc_team

def game_order(team1, team2):
    my_team = tool.role_order_manual_3(team1, 3)
    npc_team = tool.role_order_auto_3(team2, 3)
    input('请按回车键继续。')
    return my_team, npc_team

def pk_start(my_team, npc_team, game):
    for i in range(1, game + 1):
        tool.print_game_info(i)
        time.sleep(info.wait_short)
        tool.print_default_info(my_team[i - 1].name, my_team[i - 1].life, my_team[i - 1].attack,
                                npc_team[i - 1].name, npc_team[i - 1].life,
                                npc_team[i - 1].attack)
        time.sleep(info.wait_short)
        point = tool.pk_3(my_team[i - 1], npc_team[i - 1])
        input('请按回车键继续。')
    return point


if __name__ == '__main__':
    player, npc = game_start()
    ordered_player, ordered_npc = game_order(player, npc)
    result = pk_start(ordered_player, ordered_npc,3)
    tool.final_result(result)

