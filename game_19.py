def main():
    while True:
        print("Консольные игры:19 вариант")
        print("1. Начать игру")
        print("2. Правила")
        print("0. Выход")
        choice = read_choice("Выберите пункт меню",["0","1","2"])
        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Выход из игры,до свидания")
            break
def show_rules():
    print("ПРАВИЛА ИГРЫ:ЗАРЯДИ РОБОТА")
    print("1. Заряд робота начинается с 0")
    print("2.За один ход вы можете  3, прибавить 5 или вычесть 2")
    print("3.  Цель - ровно 20 за максимум 6 ходов")
    print("4. Заряд вне 0-20 запрещён, такой ввод не расходует ход.")
    print("5. Победа достигается если заряд 20 за 6 или менее ходов")
    print("6. Поражение если  за 6 ходов не набралось 20 заряда")
def read_choice(prompt,allowed):
    while True:
        n = input(prompt).strip()
        if n in allowed:
            return n
        print(f"Ошибка ввода. Допустимые значения:{', '.join(allowed)}. Попробуйте снова")
def can_change(charge,delta):
    if delta not in [3,5,-2]:
        return False 
    new_charge = charge + delta
    return 0 <= new_charge <= 20
def change_charge(charge,delta):
    return charge + delta
def is_charged(charge):
    return charge == 20
def play_game():
    charge = 0
    max_attempts = 6
    attempts_left = max_attempts
    print("Начало игры")
    print("Текущий заряд робота:{charge}")
    while attempts_left > 0:
        print("Осталось ходов =:{attempts_left}")
        print("Допустимые действия:+3(Ввдите 3),+5(введите 5),-2(введите ), или 0 для выхода в меню")
        choice_str = read_choice("Введите изменение заряда(3,5,-2) или 0 для выхода:",["3","5","-2","0"])
        if choice_str == "0":
            print("Возрат в главное меню")
            return 
        delta = int(choice_str)
        if not can_change(charge,delta):
            print("Недопустимый ход! ")
            continue
        charge = change_charge(charge,delta)
        attempts_left -= 1
        print(f"текущий заряд:{charge}")
        if is_charged(charge):
            print("Поздравляем! Робот полностью заряжен до 20! Вы победили")
            return
    print(f"Игра окончена")
if __name__ == "__main__":
    main()