from prettytable import PrettyTable

menu_level_1 = 'MENU:\n1)Press 1 for Premier League 2012/2013\n2)Press 2 for Premier League 2018/2019' \
               '\n3)Press 3 for Seria A 2007/2008\n4)Press 4 to exit the program\n'
menu_level_2 = 'MENU:\n1)Press 1 to show ranking table\n2)Press 2 to show all games of the team\n' \
               '3)Press 3 to show all games of the day\n4)Press 4 to back\n'
choices = ['1', '2', '3', '4']
# Глобальные переменные используемые в функциях
RANK = 0
DATE = 0
DTEAM = 0
HOME = 1
DPREVTEAM = 1
AWAY = 2
GOALH = 3
GOALA = 4
RESULT = 5
SCORED = 5
PREVSCORED = 6
GOALDIF = 7
PREVGOALDIF = 8
POINTS = 8
PREVPOINTS = 9


def load_data(name):
    total = []
    with open(name, 'r') as f:
        f.readline()
        for line in f:
            z = line.split(',')
            total.append([z[1], z[2], z[3], z[4], z[5], z[6]])
    return total


# Создаю словарь, где ключ - название команды
def dict_by_team(matches):
    d = {}
    for i in range(len(matches)):
        team_home = matches[i][HOME]
        team_away = matches[i][AWAY]
        if team_home not in d.keys():
            d[team_home] = []
            d[team_home].append(matches[i])
        else:
            d[team_home].append(matches[i])

        if team_away not in d.keys():
            d[team_away] = []
            d[team_away].append(matches[i])
        else:
            d[team_away].append(matches[i])
    return d


# Создаю словарь, где ключ - дата
def dict_by_date(matches):
    d = {}
    for i in range(len(matches)):
        date1 = matches[i][DATE]
        if date1 not in d.keys():
            d[date1] = []
            d[date1].append(matches[i])
        else:
            d[date1].append(matches[i])
    return d


# Функции для подсчета необходимых показателей для турнирной таблицы
def points(items, d):
    for k, v in items:
        points1 = 0
        for i in range(len(v)):
            if k == v[i][HOME] and v[i][RESULT] == 'H':
                points1 += 3
            elif k == v[i][AWAY] and v[i][RESULT] == 'A':
                points1 += 3
            elif v[i][RESULT] == 'D':
                points1 += 1
        if k not in d.keys():
            d[k] = []
            d[k].append(points1)
        else:
            d[k].append(points1)
    return d


def games_win(items, d):
    for k, v in items:
        wins = 0
        for i in range(len(v)):
            if k == v[i][HOME] and v[i][RESULT] == 'H':
                wins += 1
            elif k == v[i][AWAY] and v[i][RESULT] == 'A':
                wins += 1
        if k not in d.keys():
            d[k] = []
            d[k].append(wins)
        else:
            d[k].append(wins)
    return d


def games_lose(items, d):
    for k, v in items:
        loses = 0
        for i in range(len(v)):
            if k == v[i][HOME] and v[i][RESULT] == 'A':
                loses += 1
            elif k == v[i][AWAY] and v[i][RESULT] == 'H':
                loses += 1
        if k not in d.keys():
            d[k] = []
            d[k].append(loses)
        else:
            d[k].append(loses)
    return d


def games_draw(items, d):
    for k, v in items:
        draws = 0
        for i in range(len(v)):
            if v[i][RESULT] == 'D':
                draws += 1
        if k not in d.keys():
            d[k] = []
            d[k].append(draws)
        else:
            d[k].append(draws)
    return d


def goal_dif(items, d):
    for k, v in items:
        scored = 0
        missed = 0
        for i in range(len(v)):
            if k == v[i][HOME]:
                scored += int(v[i][GOALH])
                missed += int(v[i][GOALA])
            if k == v[i][AWAY]:
                scored += int(v[i][GOALA])
                missed += int(v[i][GOALH])
        dif = scored - missed
        if k not in d.keys():
            d[k] = []
            d[k].append(scored)
            d[k].append(missed)
            d[k].append(dif)
        else:
            d[k].append(scored)
            d[k].append(missed)
            d[k].append(dif)


def matches_played(items, d):
    for k, v in items:
        matches = len(v)
        if k not in d.keys():
            d[k] = []
            d[k].append(matches)
        else:
            d[k].append(matches)


# Правильное распределение мест для Премьер лиги
def sorting_premier(d):
    rank = 0
    for k, v in d.items():
        v.insert(0, k)
    d = list(d.values())
    d.sort(key=lambda z: (z[POINTS], z[GOALDIF], z[SCORED]), reverse=True)
    for i in range(len(d)):
        if d[i][SCORED] == d[i - 1][SCORED] and d[i][POINTS] == d[i - 1][POINTS] and d[i][GOALDIF] == d[i - 1][GOALDIF]:
            d[i].insert(0, d[i - 1][RANK])
            rank += 1
        else:
            d[i].insert(0, rank + 1)
            rank += 1
    return d


# Правильное распределение мест для Серии А
def sorting_seria(d, d_teams):
    rank = 0
    for k, v in d.items():
        v.insert(0, k)
    d = list(d.values())
    d.sort(key=lambda x: (x[POINTS]), reverse=True)
    for i in range(len(d)):
        if i == 0:
            d[i].insert(0, rank + 1)
            rank += 1
        elif d[i][POINTS] == d[i - 1][PREVPOINTS]:
            point = 0
            for u, g in d_teams.items():
                for j in range(len(g)):
                    if u == g[j][HOME] == d[i][DTEAM] and g[j][AWAY] == d[i - 1][DPREVTEAM] and g[j][RESULT] == 'H':
                        point += 3
                    elif u == g[j][AWAY] == d[i][DTEAM] and g[i][HOME] == d[i - 1][DPREVTEAM] and g[j][RESULT] == 'A':
                        point += 3
                    elif ((u == g[j][HOME] == d[i][DTEAM] and g[j][AWAY] == d[i - 1][DPREVTEAM]) or (
                            u == g[j][AWAY] == d[i][DTEAM]
                            and g[j][HOME] == d[i - 1][DPREVTEAM])) and \
                            g[j][RESULT] == 'D':
                        point += 1
            if point >= 4:
                d[i].insert(0, d[i - 1][RANK])
                d[i - 1][RANK] = rank + 1
                rank += 1
            elif point <= 1:
                d[i].insert(RANK, rank + 1)
                rank += 1
            elif point == 2 or point == 3:
                scored = 0
                missed = 0
                dif = 0
                for p, z in d_teams.items():
                    for l in range(len(z)):
                        if p == z[l][HOME] == d[i][DTEAM] and z[l][AWAY] == d[i - 1][DPREVTEAM]:
                            scored += int(z[l][GOALH])
                            missed += int(z[l][GOALA])
                        elif p == z[l][AWAY] == d[i][DTEAM] and z[l][HOME] == d[i - 1][DPREVTEAM]:
                            scored += int(z[l][GOALA])
                            missed += int(z[l][GOALH])
                        dif = scored - missed
                if dif > 0:
                    d[i].insert(0, d[i - 1][RANK])
                    d[i - 1][RANK] = rank + 1
                    rank += 1
                elif dif < 0:
                    d[i].insert(0, rank + 1)
                    rank += 1
                elif dif == 0:
                    if d[i][GOALDIF] > d[i - 1][PREVGOALDIF]:
                        d[i].insert(0, d[i - 1][RANK])
                        d[i - 1][RANK] = rank + 1
                        rank += 1
                    elif d[i][GOALDIF] < d[i - 1][PREVGOALDIF]:
                        d[i].insert(0, rank + 1)
                        rank += 1
                    elif d[i][GOALDIF] == d[i - 1][PREVGOALDIF]:
                        if d[i][SCORED] > d[i - 1][PREVSCORED]:
                            d[i].insert(0, d[i - 1][RANK])
                            d[i - 1][RANK] = rank + 1
                            rank += 1
                        elif d[i][SCORED] < d[i - 1][PREVSCORED]:
                            d[i].insert(0, rank + 1)
                            rank += 1
                        elif d[i][SCORED] == d[i - 1][PREVSCORED]:
                            d[i].insert(0, d[i - 1][RANK])
                            rank += 1
        else:
            d[i].insert(0, rank + 1)
            rank += 1
    d.sort(key=lambda x: (x[RANK]))
    return d


# Оформление вывода
def list_for_menu(d_teams_or_dates):
    d = {}
    d_teams_dates = list(d_teams_or_dates.keys())
    d_teams_dates.sort(key=lambda x: (x[0]))
    for i in range(len(d_teams_dates)):
        d[i + 1] = d_teams_dates[i]
    return d


def team_list_for_menu(d_teams):
    q = list_for_menu(d_teams)
    print('{:<20} {:<15}'.format('Number', 'Team'))
    for number, teams in q.items():
        print('{:<20} {:<15}'.format(number, teams))
    print('\n')


def date_list_for_menu(d_dates):
    q = list_for_menu(d_dates)
    print('{:<20} {:<15}'.format('Number', 'Date'))
    for number, teams in q.items():
        print('{:<20} {:<15}'.format(number, teams))
    print('\n')


def all_matches_team(d_teams, team1):
    x = PrettyTable()
    x.field_names = ['DATE', 'TEAMS', 'SCORE']
    for i in range(len(d_teams[team1])):
        teams = f'{d_teams[team1][i][HOME]}-{d_teams[team1][i][AWAY]}'
        score = f'{d_teams[team1][i][GOALH]}:{d_teams[team1][i][GOALA]}'
        x.add_row([d_teams[team1][i][DATE], teams, score])
    return x


def all_matches_date(d_dates, date1):
    x = PrettyTable()
    x.field_names = ['DATE', 'TEAMS', 'SCORE']
    for i in range(len(d_dates[date1])):
        teams = f'{d_dates[date1][i][HOME]}-{d_dates[date1][i][AWAY]}'
        score = f'{d_dates[date1][i][GOALH]}:{d_dates[date1][i][GOALA]}'
        x.add_row([d_dates[date1][i][RANK], teams, score])
    return x


def final_table(table):
    x = PrettyTable()
    x.field_names = ['Rank', 'Team', 'Games played', 'Games win', 'Games draw', 'Games lose', 'Goals scored',
                     'Goals missed', 'Goals difference', 'Points']
    for i in range(len(table)):
        x.add_row(table[i])
    return x


# Проверка ошибок
def mis(select, listselect):
    while select not in listselect:
        print('Error.Try again')
        select = input('Your choice:\t')
        print()
        if select in listselect:
            break
    return select


all_matches_premier_1213 = load_data("E0.csv")
d_dates_premier_1213 = dict_by_date(all_matches_premier_1213)
d_teams_premier_1213 = dict_by_team(all_matches_premier_1213)
season_premier_1213 = {}
matches_played(d_teams_premier_1213.items(), season_premier_1213)
games_win(d_teams_premier_1213.items(), season_premier_1213)
games_lose(d_teams_premier_1213.items(), season_premier_1213)
games_draw(d_teams_premier_1213.items(), season_premier_1213)
goal_dif(d_teams_premier_1213.items(), season_premier_1213)
points(d_teams_premier_1213.items(), season_premier_1213)
season_premier_1213 = sorting_premier(season_premier_1213)

all_matches_premier_1819 = load_data("PremierLeague1819.csv")
d_dates_premier_1819 = dict_by_date(all_matches_premier_1819)
d_teams_premier_1819 = dict_by_team(all_matches_premier_1819)
season_premier_1819 = {}
matches_played(d_teams_premier_1819.items(), season_premier_1819)
games_win(d_teams_premier_1819.items(), season_premier_1819)
games_lose(d_teams_premier_1819.items(), season_premier_1819)
games_draw(d_teams_premier_1819.items(), season_premier_1819)
goal_dif(d_teams_premier_1819.items(), season_premier_1819)
points(d_teams_premier_1819.items(), season_premier_1819)
season_premier_1819 = sorting_premier(season_premier_1819)

all_matches_SeriaA = load_data("SeriaA78.csv")
d_dates_SeriaA = dict_by_date(all_matches_SeriaA)
d_teams_SeriaA = dict_by_team(all_matches_SeriaA)
season_SeriaA = {}
matches_played(d_teams_SeriaA.items(), season_SeriaA)
games_win(d_teams_SeriaA.items(), season_SeriaA)
games_lose(d_teams_SeriaA.items(), season_SeriaA)
games_draw(d_teams_SeriaA.items(), season_SeriaA)
goal_dif(d_teams_SeriaA.items(), season_SeriaA)
points(d_teams_SeriaA.items(), season_SeriaA)
season_SeriaA = sorting_seria(season_SeriaA, d_teams_SeriaA)
# Меню
print(menu_level_1)
print()
choice = input('Your choice:\t')
print()
choice = mis(choice, choices)
while True:
    if choice == '1':
        print(menu_level_2)
        print()
        choice = input('Your choice:\t')
        choice = mis(choice, choices)
        if choice == '1':
            print(final_table(season_premier_1213))
            print()
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '2':
            team_list_for_menu(d_teams_premier_1213)
            choice_team = list_for_menu(d_teams_premier_1213)
            team = input('Press number of the teem you need:\t')
            print()
            while True:
                try:
                    team = int(team)
                    print('All games of', choice_team[team])
                    print()
                    print(all_matches_team(d_teams_premier_1213, choice_team[team]))
                    print()
                    break
                except ValueError:
                    print('Error. Try again\n')
                    team = input('Press number of the teem you need:\t')
                except KeyError:
                    print('Error. Try again\n')
                    team = input('Press number of the teem you need:\t')
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            print()
            choice = mis(choice, choices)
        elif choice == '3':
            date_list_for_menu(d_dates_premier_1213)
            choice_date = list_for_menu(d_dates_premier_1213)
            date = input('Press number of the date you need:\t')
            while True:
                try:
                    date = int(date)
                    print('All games of:', choice_date[date])
                    print()
                    print(all_matches_date(d_dates_premier_1213, choice_date[date]))
                    print()
                    break
                except ValueError:
                    print('Error. Try again\n')
                    date = input('Press number of the teem you need:\t')
                except KeyError:
                    print('Error. Try again\n')
                    date = input('Press number of the teem you need:\t')
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '4':
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
    elif choice == '2':
        print(menu_level_2)
        print()
        choice = input('Your choice:\t')
        choice = mis(choice, choices)
        if choice == '1':
            print((final_table(season_premier_1819)))
            print()
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '2':
            team_list_for_menu(d_teams_premier_1819)
            choice_team = list_for_menu(d_teams_premier_1819)
            team = input('Press number of the teem you need:\t')
            while True:
                try:
                    team = int(team)
                    print('All games of', choice_team[team])
                    print()
                    print(all_matches_team(d_teams_premier_1819, choice_team[team]))
                    print()
                    break
                except ValueError:
                    print('Error. Try again\n')
                    team = input('Press number of the teem you need:\t')
                except KeyError:
                    print('Error. Try again\n')
                    team = input('Press number of the teem you need:\t')
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '3':
            date_list_for_menu(d_dates_premier_1819)
            choice_date = list_for_menu(d_dates_premier_1819)
            date = input('Press number of the date you need:\t')
            while True:
                try:
                    date = int(date)
                    print('All games of:', choice_date[date])
                    print()
                    print(all_matches_date(d_dates_premier_1819, choice_date[date]))
                    print()
                    break
                except ValueError:
                    print('Error. Try again\n')
                    date = input('Press number of the teem you need:\t')
                except KeyError:
                    print('Error. Try again\n')
                    date = input('Press number of the teem you need:\t')
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '4':
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
    elif choice == '3':
        print(menu_level_2)
        print()
        choice = input('Your choice:\t')
        choice = mis(choice, choices)
        if choice == '1':
            print((final_table(season_SeriaA)))
            print()
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '2':
            team_list_for_menu(d_teams_SeriaA)
            choice_team = list_for_menu(d_teams_SeriaA)
            team = input('Press number of the teem you need:\t')
            while True:
                try:
                    team = int(team)
                    print('All games of', choice_team[team])
                    print()
                    print(all_matches_team(d_teams_SeriaA, choice_team[team]))
                    print()
                    break
                except ValueError:
                    print('Error. Try again\n')
                    team = input('Press number of the teem you need:\t')
                except KeyError:
                    print('Error. Try again\n')
                    team = input('Press number of the teem you need:\t')
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '3':
            date_list_for_menu(d_dates_SeriaA)
            choice_date = list_for_menu(d_dates_SeriaA)
            date = input('Press number of the date you need:\t')
            while True:
                try:
                    date = int(date)
                    print('All games of:', choice_date[date])
                    print()
                    print(all_matches_date(d_dates_SeriaA, choice_date[date]))
                    print()
                    break
                except ValueError:
                    print('Error. Try again\n')
                    date = input('Press number of the teem you need:\t')
                except KeyError:
                    print('Error. Try again\n')
                    date = input('Press number of the teem you need:\t')
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
        elif choice == '4':
            print(menu_level_1)
            print()
            choice = input('Your choice:\t')
            choice = mis(choice, choices)
    elif choice == '4':
        break
