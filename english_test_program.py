print("Привет! Предлагаю проверить свои знания английского!\nНаберите ready, чтобы начать!")
start = input()

# Будет спрашивать пока не введут "ready"
while start != "ready":
    print("Кажется, вы не хотите играть. Очень жаль")
    start = input()

# Списки
questions = ['My name ___  Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']
uncorrect_answers = ["Осталось попыток: 2, попробуйте ещё раз!", "Осталось попыток: 1, попробуйте ещё раз!"]

# Переменные
correct_answers = 0
score = 0
percent_of_correct = 0
# Переменная для правильной постановки окончания
correct = ("")

print('')
print('Впишите правильные ответы в пропуски')
print('')
# Цикл
for i in range(len(questions)):
    print('')
    print(f"Вопрос № {i + 1}")
    print(questions[i])
    answer = input()
    if answer != answers[i]:
        print(uncorrect_answers[0])
        print(questions[i])
        answer = input()
        if answer != answers[i]:
            print(uncorrect_answers[1])
            print(questions[i])
            answer = input()
            if answer != answers[i]:
                print(f"Увы, но нет. Верный ответ: {answers[i]}")
            else:
                correct_answers += 1
                score += 1
                percent_of_correct += 33.3
                print("Ответ верный! Вы заработали 1 балл")
        else:
            correct_answers += 1
            score += 2
            percent_of_correct += 33.3
            print("Ответ верный! Вы заработали 2 балла")
    else:
        correct_answers += 1
        score += 3
        percent_of_correct += 33.3
        print("Ответ верный! Вы заработали 3 балла")

# Вывод првильного окончания
if correct_answers == 3:
    correct += ("все вопросы")
elif correct_answers == 2:
    correct += ("2 вопроса из 3")
elif correct_answers == 1:
    correct += ("1 вопрос из 3")
else:
    correct += ("0 вопросов из 3")

print("")
print(f"Вот и все!", f"Вы ответили на {correct} верно.", f"Вы заработали {score} баллов.",
      f"Это {round(percent_of_correct)} процентов", sep='\n')
