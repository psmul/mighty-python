
# tasks = open('tasks.txt', 'a')
# print('Put out the trash.', file=tasks)
# tasks.close()
#
#
# myfile = open('tasks.txt')
# for line in myfile:
#     print(line, end='')


with open('tasks.txt') as some_tasks:
    for line in some_tasks:
        print(line, end='')
