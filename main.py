import main_other as t
from random import randint
import time
import os


class Character:
    def __init__(self, name, power=1, hp=1000):
        self.name = name
        self.hp = hp
        self.power = power  # 1~10사이의 랜덤한 정수
        self.damage = self.power * randint(1, self.power * 10) * 2  # 물리공격
        self.magic = self.power * randint(1, self.power * 10) * 2   # 마법공격
        self.r = 0  # 아이템으로 얻는 방어력
        self.heal_tem = 3
        self.alive = True

    def alive_check(self):
        if self.hp < 0:
            self.alive = False

    # 아이템
    def item(self):
        print("\n----------------------------- \n")
        print("\033[33m 무작위 아이템을 받았습니다. \033[0m\n")
        item_num = randint(1, 5)
        if item_num == 1:
            if self.hp < 1000:
                print("\033[32m 체력을 500 회복합니다. \033[0m\n")
                self.hp += 500
            else:
                print("이미 체력이 최대입니다. \n 새로운 선물을 드리죠^ㅇ^")
                return user.item()  # 최대 체력일 시 다시 호출
        elif item_num == 2:
            print("\033[31m power가 1 감소했습니다.\033[0m\n")
            self.power -= 1
        elif item_num == 3:
            print("\033[32m power가 1 증가했습니다. \033[0m \n")
            if self.power == 10:
                print("이런! 이미 파워가 최대치군요.. 이를 어쩐담.. \n")
                print("\033[32m 아하! 대신 새로운 선물을 드릴께요!! 뾰로롱! \033[0m")
                return user.item()  # 최대 파워일 시 다시 호출
            else:
                self.power += 1
        elif item_num == 4:
            print("\033[32m 힐 포션 1개 획득! \n \033[0m")
            self.heal_tem += 1
        else:
            print("\033[96m 몬스터의 공격력을 50 감소시킵니다. \033[0m\n")
            self.r += 50
        print("----------------------------- \n\n")


class User(Character):
    def show_info(self):
        if level == 1:
            print(f"\033[92m-------플레이어 정보---------\n"
                  f"플레이어 : {self.name} \n"
                  f"LEVEL : {level}Lv \n"
                  f"heal_item : {self.heal_tem}개 \n"
                  f"HP : {self.hp}hp \n"
                  f"POWER : {self.power} \n"
                  f"DAMAGE(물리 공격) : {self.damage}\n"
                  f"MAGIC(마법 공격) : {self.magic}\n"
                  f"방어력 : {self.r} \n"
                  f"총 공격량 : {total_dmg} \n"
                  f"--------------------------\033[0m")
        else:
            print(f"\033[92m-------플레이어 정보---------\n"
                  f"플레이어 : {self.name} \n"
                  f"LEVEL : {level}Lv \n"
                  f"heal_item : {self.heal_tem}개 \n"
                  f"HP : {self.hp}hp \n"
                  f"POWER : {self.power} \n"
                  f"DAMAGE(물리 공격) : {self.damage}(+{level * 10})\n"
                  f"MAGIC(마법 공격) : {self.magic}(+{level * 10})\n"
                  f"방어력 : {self.r} \n"
                  f"총 공격량 : {total_dmg} \n"
                  f"--------------------------\033[0m")

    # 유저 우선 공격
    def user_attack(self, select, mr, r):
        # 1 : 물리공격, 2 : 마법공격
        # 몬스터의 방어력과 마저로 인해 플레이어 데미지 감소
        # 물리공격
        if select == 1:
            # power에 따른 데미지의 큰 편차를 줄이기 위해 분리
            if self.power < 6:
                # 치명타 확률 5/8
                super_attack = randint(3, 10)
                if super_attack > 5:
                    user_damage = self.damage + 500 - monster.m_r * 2
                    print("\033[33m --치명타 발동!!-- \033[0m")
                else:
                    user_damage = randint(1, self.damage) + 100 - monster.m_r * 2
            else:
                # 치명타 확률 2/7
                super_attack = randint(1, 7)
                if super_attack > 5:
                    user_damage = self.damage + 100 - monster.m_r * 2
                    print("\033[33m --치명타 발동!!-- \033[0m")
                else:
                    user_damage = randint(1, self.damage) - monster.m_r * 2
            print(f"몬스터의 방어력으로 인해 \033[31m{monster.m_r * 2}만큼 데미지가 감소했습니다.\033[31m")
            if user_damage < monster.m_r * 2:
                print("\033[93m 몬스터가 공격을 회피했습니다. \033[0m")
                user_damage = 0
            else:
                print(f"\033[33m{self.name}님이 몬스터에게 (물리 공격){user_damage}데미지를 가했습니다.\033[0m")
        # 마법공격
        else:
            if self.power < 6:
                # 치명타 확률 5/8
                super_attack = randint(3, 10)
                if super_attack > 5:
                    user_damage = self.magic + 500 - monster.m_mr * 2
                    print("\033[31m --치명타 발동!!-- \033[0m")
                else:
                    user_damage = randint(1, self.magic) + 100 - monster.m_mr * 2
            else:
                # 치명타 확률 2/7
                super_attack = randint(1, 7)
                if super_attack > 5:
                    user_damage = self.magic + 100 - monster.m_mr * 2
                    print("\033[31m --치명타 발동!!-- \033[0m")
                else:
                    user_damage = randint(1, self.magic) - monster.m_mr * 2
            print(f"몬스터의 방어력으로 인해 \033[31m{monster.m_mr * 2}만큼 데미지가 감소했습니다.\033[31m")
            if user_damage < monster.m_mr * 2:
                print(f"\033[93m 몬스터가 공격을 회피했습니다. \n \033[0m")
                user_damage = 0
            else:
                print(f"\033[33m{self.name}님이 (마법공격){user_damage}데미지를 가했습니다.\033[0m \n")
        return user_damage

    def u_status(self, m_attack):
        if monster.alive:  # 몬스터가 죽었을 때 마지막 데미지는 들어오지 않음.
            self.hp -= m_attack
        if self.hp > 0:
            print(f"플레이어의 남은 HP는 {self.hp}입니다.")


class Monster(Character):
    def __init__(self, name, hp, mr, r, damage):
        super().__init__(name)
        self.hp = hp + level * 10
        self.m_mr = mr + level * 10
        self.m_r = r + level * 10
        self.damage = damage + level * 10

    def m_info(self):
        print(f"\033[91m-----{self.name} 스탯----- \n"
              f"HP : {self.hp} \n"
              f"DAMAGE : {self.damage}\n"
              f"마법 저항 : {self.m_mr} \n"
              f"방어력 : {self.m_r} \n"
              f"------------------\033[0m")
        r, mr = self.m_r, self.m_mr
        return r, mr

    def m_damage(self, damage_receive):
        self.hp -= damage_receive
        if self.hp < 0:
            self.alive = False

    def m_attack(self):
        m_damage = randint(1, self.damage) - user.r
        heal_hp = randint(1, 5)
        if self.alive:
            if heal_hp > 3:
                self.hp += 100
                print("\033[31m!!몬스터 효과 발동!!\033[0m")
                print("몬스터가 100hp를 획득했습니다.")
            print(f'{self.name}의 남은 hp는 {self.hp}입니다. \n \n {self.name}이 공격합니다.')
            if user.r == 0:
                print(f" \033[31m {self.name}가 플레이어에게 {m_damage}데미지를 입혔습니다. \033[0m \n")
            else:
                print(f"{self.name}이 플레이어에게 {m_damage}(-{user.r})데미지를 입혔습니다. \n")
        else:
            print('꽥! 죽었닷! 두고보자!!!')
        return m_damage


def select_attack():
    while True:
        select = input("공격 방법을 선택해 주세요. \n"
                       "1.물리 공격 \n"
                       "2.마법 공격 \n"
                       "3.스탯 확인 \n"
                       "4.포션 사용 \n")
        if select == '':
            print("입력된 값이 없습니다. 다시 입력해주세요. \n")
        elif not select.isdigit():
            print("숫자로만 입력해 주세요.")
        elif int(select) < 1 or int(select) > 4:
            print('선택 범위를 벗어났습니다.')
        elif int(select) == 3:
            user.show_info()
            monster.m_info()
            return select_attack()  # 스탯보기 반복시 그만큼 다시 선택 해야하는 오류 -> return 추가
        elif int(select) == 4:
            if user.heal_tem > 0:
                if user.hp < 1000:
                    print(f"\033[33m-------------------------- \n"
                          f"200의 체력을 회복합니다. \n"
                          f"{user.hp} -> {user.hp + 200} \n"
                          f"--------------------------\033[0m")
                    user.hp += 200
                    if user.hp > 1000:
                        print("-------------------------- \n"
                              "최대 체력인 1000으로 회복합니다. \n"
                              "--------------------------\033[0m \n")
                        user.hp = 1000
                    user.heal_tem -= 1
                else:
                    print("\n \033[31m 이미 체력이 최대입니다.\033[0m \n")
            else:
                print("\033[31m 모든 포션을 사용하셨습니다. \033[0m")
            return select_attack()  # 4번은 공격이 아니므로 선택시 select_attack함수 다시 호출
        else:
            return int(select)


level = 1
total = 0
total_dmg = 0

# 설명서

print("\033[33m-----------------------게임 설명--------------------- \n"
      "1.유저를 등록하면 랜덤한 power가 부여됩니다. \n"
      "2.power는 한번만 변경 할 수 있습니다. \n"
      "3.힐 포션을 사용하면 200hp를 회복합니다.(최대 1000hp까지만 가능) \n"
      "4.power가 높을 수록 데미지가 크지만, 치명타 확률은 낮아집니다.\n"
      "5.공격은 물리공격과 마법공격이 있으며, 이는 power에 비례합니다. \n"
      "6.level이 오를 수록 몬스터와 플레이어가 성장합니다. \n"
      "7.게임종료 5초 후 콘솔이 리셋됩니다. \n"
      "----------------------------------------------------\033[0m\n")


name_receive = t.make_player()  # 유저이름 입력
power_receive = t.make_power()  # 유저 파워 랜덤생성
user = User(name_receive, power_receive)  # user라는 Character생성
user.show_info()  # 유저의 정보 출력
monster_receive = t.make_monster()  # 몬스터 선택
if monster_receive == 1:
    monster = Monster('핑핑몬', randint(200, 300), 30, 10, 100)  # hp, mr, r , damage
elif monster_receive == 2:
    monster = Monster('디지몬', randint(200, 350), 5, 35, 200)
elif monster_receive == 3:
    monster = Monster('포켓몬', randint(100, 200), 25, 15, 250)
else:
    monster = Monster('구몬', randint(100, 200), 35, 35, 150)
m_mr, m_r = monster.m_info()

while True:
    # 첫 전투 신청
    if total == 0:
        print("몬스터에게 전투를 신청하시겠습니까? \n"
              "'아니오'를 선택하면 게임이 종료됩니다.")
        game_start = t.check_answer()
    if game_start == 1:
        u_attack = select_attack()
        user_damage_give = user.user_attack(u_attack, m_mr, m_r)  # 유저 먼저 공격
        monster.m_damage(user_damage_give)  # 몬스터 데미지에 유저 attack 입력
        attack = monster.m_attack()  # 몬스터 공격
        user.u_status(attack)  # 유저 체력 관리
        user.alive_check()  # 유저 체력 확인
        total += 1  # 전투횟수 추가
        total_dmg += user_damage_give
    else:
        print('게임을 종료합니다.')
        break
    if not user.alive:
        print(f'유저가 사망했습니다. 게임을 종료합니다.')
        break
    if monster.alive:
        print("다시 공격 하시겠습니까? \n"
              "'아니오'를 선택하면 게임이 종료됩니다.")
        re_attack = t.check_answer()
    else:
        print(f"총 {total}번의 전투 끝에 승리했습니다!\n")
        print("\n\033[33m 아이템은 5의 배수 레벨에서 얻을 수 있습니다! \033[0m\n")
        print("다음 레벨에 도전 하시겠습니까?\n"
              "'아니오'를 선택하면 게임이 종료됩니다.")
        re_start = t.check_answer()
        if re_start == 1:
            total = 0
            level += 1
            user.damage += level * 10
            user.magic += level * 10
            print("\033[33m !!!!level up!!!!! \033[0m\n")
            if level % 5 == 0:
                user.item()
                time.sleep(1)
            user.show_info()
            monster_receive = t.make_monster()
            if monster_receive == 1:
                monster = Monster('핑핑몬', randint(200, 300), 30, 10, 100)  # hp, mr, r , damage
            elif monster_receive == 2:
                monster = Monster('디지몬', randint(200, 350), 5, 25, 200)
            elif monster_receive == 3:
                monster = Monster('포켓몬', randint(100, 200), 25, 15, 250)
            else:
                monster = Monster('구몬', randint(100, 200), 25, 25, 150)
            monster.m_info()
        else:
            print('게임을 종료합니다.')
            break
    try:
        if re_attack == 1:
            continue
        else:
             break
    except:
        continue


# 게임 종료시 최종 스탯을 보여줌
user.show_info()
print("5초 후 모든 내용이 삭제됩니다.")
time.sleep(5)
os.system('clear')  # 콘솔창 clear

