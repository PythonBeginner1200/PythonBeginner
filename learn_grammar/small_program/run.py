import threading
import time
import learn_grammar.mapping.mapping_of_RPG_game as info

exitFlag = 0

class myThread(threading.Thread): #{'order': 1, 'name': '【枪弹专家】', 'life': 120, 'attack': 80}
    def __init__(self, name1, name2, life, attack, attack_speed):
        threading.Thread.__init__(self)
        self.name1 = name1
        self.name2 = name2
        self.life = life
        self.attack = attack
        self.attack_speed = attack_speed

    def run(self):
        print_time(self.name1, self.name2,self.attack, self.attack_speed, self.life)



def print_time(name1, name2, attack_other, attack_speed, life2):
    while life2 > 0:
        if exitFlag:
            name1.exit()
        time.sleep(attack_speed)
        print(info.PK_info.format(name2, name1, life2))
        life2 -= attack_other


if __name__ == '__main__':
    player = myThread('[player]', '[NPC]', 100, 10, 1)
    computer = myThread('[NPC]', '[player]', 88, 22, 3)
    player.start()
    computer.start()
    player.join()
    computer.join()
    print('over')