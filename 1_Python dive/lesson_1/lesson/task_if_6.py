color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зеленый':
        print('Ты не охотник?')
    case _:
        print('Тебя не понять')
