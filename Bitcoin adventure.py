import time

class Player:
    def __init__(self, name):
        self.name = name
        self.bitcoin = 0
        self.money = 1000

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def invest_bitcoin(player):
    delay_print(f"欢迎来到《穿越投资比特币财富》游戏，{player.name}！")
    delay_print("你将在这个游戏中穿越到21世纪，决定是否投资比特币，追求财富。")

    while player.money > 0:
        delay_print(f"\n{player.name}，你目前有现金：{player.money}元，比特币：{player.bitcoin}个。")
        action = input("请选择你的操作（投资/卖出/结束）：").strip().lower()

        if action == "投资":
            investment = int(input("请输入你要投资的现金数额："))
            if investment <= player.money:
                player.money -= investment
                player.bitcoin += investment // 100  # 假设比特币价格为100元
                delay_print(f"{player.name}投资了{investment}元，持有比特币{player.bitcoin}个。")
            else:
                delay_print("你的现金不足。")
        elif action == "卖出":
            bitcoins_to_sell = int(input("请输入你要卖出的比特币数量："))
            if bitcoins_to_sell <= player.bitcoin:
                player.bitcoin -= bitcoins_to_sell
                player.money += bitcoins_to_sell * 100  # 假设比特币价格为100元
                delay_print(f"{player.name}卖出了{bitcoins_to_sell}个比特币，获得{bitcoins_to_sell * 100}元现金。")
            else:
                delay_print("你的比特币不足。")
        elif action == "结束":
            delay_print(f"谢谢参与穿越投资比特币财富游戏！最终财产：现金{player.money}元，比特币{player.bitcoin}个。")
            exit()
        else:
            delay_print("无效的操作。")

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    invest_bitcoin(player)

if __name__ == "__main__":
    main()
