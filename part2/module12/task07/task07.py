from TaskManager import TaskManager

print('Задача 7. Стек')

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
print()
manager.remove_task("помыть посуду")
print(manager)
print()
manager.new_task("сделать уборку", 3)
print(manager)
