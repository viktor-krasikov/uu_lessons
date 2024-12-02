team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = f'Победа команды {team1_name}!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = f'Победа команды {team2_name}!'
else:
    challenge_result = 'Ничья!'

print("В команде %s участников: %d !" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print("Команда {0} решила задач: {1} !".format(team2_name, score_2))
print("{name} решили задачи за {time:.1f} с !".format(name=team2_name, time=team2_time))

print(f"Команды {team1_name} и {team2_name} решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")
