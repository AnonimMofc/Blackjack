#                         _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_     REDACTED    TO    VERSION    |||   1.0.5   |||   _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
#                                                                                         { F I X E D }
#                                                                  -1-       If you gonna get >1 aces -> it sums to   *has_11*
#                                                                  -2-       Did a      ~ This title list~  (ig it would be good)
#                                                                  -3-       Fortnite balls im gay i like boys i kidnap autistic kidz lil mozy is watchin T-rex
#                                                     [][][][][][][][][][][][][]  -  Be greateful, Ludomaniac   -  [][][][][][][][][][][][][][][][]

from time import sleep
from random import choice
#              _______________________________________________ ФУНКЦИИ _____________________________________________________
def write_text_beatifully(x):
    for _ in x:
        print(_, flush=True, end='')
        sleep(0.04)
    return ''
def take_a_card(player):
    global has_11
    givepoints = choice(stuck)
    stuck.remove(givepoints)
    if givepoints == 11:
        print(write_text_beatifully(f'Вы достали карту номинала {givepoints} или 1'))
        has_11 += 1
    if givepoints == 11 and player >= 11:
        has_11 -= 1
        return 1  
    elif givepoints != 11:
        print(write_text_beatifully(f'Вы достали карту номинала {givepoints}'))
        if has_11 > 0 and player+givepoints > 21:
            has_11 -= 1
            return -10 + givepoints
        else:
            return givepoints
def check_valid(givepoints, player):
    global has_11
    if givepoints == 11:
        print(write_text_beatifully(f'Вы достали карту номинала {givepoints} или 1'))
        has_11 += 1
    if givepoints == 11 and player >= 11:
        has_11-=1
        return 1  
    elif givepoints != 11:
        print(write_text_beatifully(f'Вы достали карту номинала {givepoints}'))
        if has_11 > 0 and player+givepoints >= 21:
            has_11 -= 1
            return -10 + givepoints
        else:
            return givepoints
def end_the_game(player, dealer):
    print(write_text_beatifully(f'У дилера {dealer} очков.'))
    if dealer < 17:
        givepoints = choice(stuck)
        stuck.remove(givepoints)
        if givepoints == 11 and dealer >= 11:
            dealer+=1
        else:
            dealer+=givepoints
        print(write_text_beatifully(f'Дилер добрал карту.'), end='\n')
        return end_the_game(player,dealer)
    if player > dealer or (player <= 21 and dealer > 21):
        print(write_text_beatifully('Вы победили.'))
    elif player < dealer:
        print(write_text_beatifully('Вы проиграли'))
    elif player == dealer or (player > 21 and dealer > 21):
        print(write_text_beatifully('Ничья.'))
#              ____________________________________________ ВСЕ ВАЖНЫЕ КОЛОДЫ ______________________________________________
stuck = [2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11]
has_11 = int(0)
#              _____________________________________________________________________________________________________________

print(write_text_beatifully('Происходит раздача карт...'))
players_points = int(0)
dealer_points = int(0)
for y in range(2):
  tosmbpoints = 0
  for x in range(2):
    givepoints = choice(stuck)
    stuck.remove(givepoints)
    if givepoints != 11:
        tosmbpoints += givepoints
    else:
        has_11 += 1
        if players_points >= 11:
            tosmbpoints+=1
            has_11-=1
        else:
            tosmbpoints+=givepoints
    if y == 0:
        players_points = tosmbpoints
        if givepoints != 11:
            print(write_text_beatifully(f'Вы достали карту номинала {givepoints}'))
        else:
            print(write_text_beatifully(f'Вы достали карту номинала {givepoints} или 1'))
    else:
        dealer_points = tosmbpoints
while True:
    if players_points < 22:
        print(write_text_beatifully(f'У вас {players_points} очков. Желаете взять еще карту?(да/нет)         '))
        a = input()
        if a == 'да':
            players_points+=take_a_card(players_points)
        elif a == 'нет':
            end_the_game(players_points, dealer_points)
            break
        elif a == 'cheatcode_21numberUNLOCK':
            print(write_text_beatifully(f'Вы взяли карту номинала {21-players_points}'))
            print(write_text_beatifully('У вас 21 очков'))
            end_the_game(21, dealer_points)
            break
        elif 'takecard' in a:
            number = int(a.split(' ')[1])
            if number:
                players_points+=check_valid(number, players_points)
            else:
                continue
    else:
        print(write_text_beatifully(f'У вас {players_points} очков. Вы проиграли.'))
        breakы проиграли.'))
        break
