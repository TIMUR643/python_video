def player1(name,health,damage):
    dicts = {'Имя':name,'Живучесть': health, 'Наносисый урон': damage}
    Nick_name = name
    heal      = int(health)
    damag     = int(damage)
    print('Состояние игрока')
    print(f"Имя игрока {Nick_name}, Живучесть {heal} %.")
    if damag > 0:
        heal = heal - damag
        print(f'Живучесть после  нанесеного дамага = {damag}%, состовляет {heal}% ')
        dicts['Живучесть'] = heal
        print(dicts)

def damage_armor(damage,armor):
    damag       = int(damage)
    arm         = float(armor)
    result_heal = damag / arm
    print(f'Получаемый урон при Armor(защите противника) / {armor} =  {result_heal}')
    return (result_heal)

# Вычисляем наносимый урон противнику
damaged = damage_armor(30,1.2)
