from random import randint
level = 1
total = 0
total_dmg = 0


# 유저 정보 입력
def make_player():
    player = input('플레이어의 이름을 정해주세요 : ')
    return player


# 유저의 power부여
def make_power():
    random_power = randint(1, 10)
    print(f"당신의 power는 {random_power}입니다. (1~10)")
    print("power를 다시 부여 받고 싶으신가요? \n 남은 기회는 1번입니다")
    re_power = check_answer()
    if re_power == 1:
        random_power = randint(1, 10)
        print(f"power를 {random_power}로 다시 부여 받았습니다.")
        return random_power
    else:
        return random_power


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


# 몬스터 선택
def make_monster():
    user_monster = input(f"상대할 몬스터를 선택해 주세요. 몬스터는 랜덤의 스텟을 가집니다. \n"
                         f"1. 핑핑몬({level}Lv) -마법 저항력 : {30 + level * 10}, 방어력 : {10 + level * 10}- \n "
                         f"2. 디지몬({level}Lv) -마법 저항력 : {5 + level * 10}, 방어력 : {35 + level * 10}- \n "
                         f"3. 포켓몬({level}Lv) -마법 저항력 : {25 + level * 10}, 방어력 : {15 + level * 10}- \n "
                         f"4. 구몬({level}Lv) -마법 저항력 : {35 + level * 10}, 방어력 : {35 + level * 10}- \n ")
    if not user_monster.isdigit():
        print('숫자로만 입력해 주세요.')
        make_monster()
    elif int(user_monster) < 1 or int(user_monster) > 4:
        print('선택할 수 있는 범위를 벗어났습니다.')
        make_monster()
    else:
        monster_num = int(user_monster)
        return monster_num


# 대답 유효성 판단
def check_answer():
    while True:
        check = input("1.예 2.아니오\n")
        if check == '':
            print("입력된 값이 없습니다. 다시 입력해주세요. \n")
        elif not check.isdigit():
            print('숫자로만 입력해주세요.')
        elif int(check) < 1 or int(check) > 2:
            print("1 또는 2 중에서 선택해주세요.\n")
        else:
            return int(check)