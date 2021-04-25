import inquirer
import os

tasks = []
res = None 

while True:
    print(tasks)
    res = input("Add a task or type .q to quit:\n")
    if res == ".q":
        break
    tasks.append(res)

while len(tasks) > 0:
    os.system('clear')
    questions = [
        inquirer.List('tasks',
            message="What task have you completed?",
            choices = tasks
        )
    ]
    answer = inquirer.prompt(questions)
    tasks.remove(answer['tasks'])
