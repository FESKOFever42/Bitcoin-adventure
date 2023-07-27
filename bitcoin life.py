import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.bitcoin = 0
        self.cash = 1000
        self.energy = 100
        self.age = 18

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_status(player):
    print(f"\n{name}比特币数量：{player.bitcoin}  现金：{player.cash}  能量：{player.energy}  年龄：{player.age}")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 挖矿")
    print("3. 投资比特币")
    print("4. 进行交易")
    print("5. 休息")
    print("6. 结束游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5/6）："))
            if 1 <= choice <= 6:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def mine_bitcoin(player):
    energy_cost = random.randint(10, 30)
    bitcoin_mined = random.randint(1, 5)

    if player.energy >= energy_cost:
        player.energy -= energy_cost
        player.bitcoin += bitcoin_mined
        delay_print(f"{player.name}挖矿获得了{bitcoin_mined}个比特币，消耗了{energy_cost}点能量。")
    else:
        delay_print(f"{player.name}能量不足，无法挖矿。")

def invest_bitcoin(player):
    if player.bitcoin > 0:
        bitcoin_investment = random.randint(1, player.bitcoin)
        bitcoin_price = random.randint(50, 100)
        player.bitcoin -= bitcoin_investment
        player.cash += bitcoin_investment * bitcoin_price
        delay_print(f"{player.name}投资了{bitcoin_investment}个比特币，以每个比特币{bitcoin_price}美元的价格出售。")
    else:
        delay_print(f"{player.name}没有比特币，无法进行投资。")

def trade_bitcoin(player):
    if player.bitcoin > 0:
        bitcoin_trade = random.randint(1, player.bitcoin)
        bitcoin_price = random.randint(50, 100)
        player.bitcoin -= bitcoin_trade
        player.cash += bitcoin_trade * bitcoin_price
        delay_print(f"{player.name}交易了{bitcoin_trade}个比特币，以每个比特币{bitcoin_price}美元的价格出售。")
    else:
        delay_print(f"{player.name}没有比特币，无法进行交易。")

def rest(player):
    energy_recovered = random.randint(10, 30)
    player.energy = min(100, player.energy + energy_recovered)
    delay_print(f"{player.name}休息了，恢复了{energy_recovered}点能量。")

def play_game():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    delay_print(f"欢迎来到比特币诞生时期模拟人生游戏，{player_name}！")
    delay_print("你将在这个游戏中体验早期比特币的世界。")

    while True:
        show_status(player)
        action = choose_action()

        if action == 1:
            show_status(player)
        elif action == 2:
            mine_bitcoin(player)
        elif action == 3:
            invest_bitcoin(player)
        elif action == 4:
            trade_bitcoin(player)
        elif action == 5:
            rest(player)
        elif action == 6:
            delay_print("谢谢你玩比特币诞生时期模拟人生游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()
