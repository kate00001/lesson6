my_dict = {'Name': 'Екатерина', 'born': 2000, 'breakfast': 'Кофе','sleep, ч.': 4}
print(my_dict)
print('Имя:', my_dict['Name'])
my_dict['Pet'] = 'Кактус'
print('Домашнее животное:', my_dict['Pet'])
my_dict.update({'father': 'Валера', 'mother': 'Светлана'})
a = my_dict.pop('sleep, ч.')        #del my_dict['sleep, ч.']
print('Спала сегодня, ч.: ',a)      #print('Спала сегодня, ч.: ', my_dict.get('sleep, ч.'))


my_set = {72, 72, 'Капуста', 'Брокколи', True, True, 11, 3, False, 11}
print(my_set)
my_set.add('Суп')
my_set.add('Не Суп')
my_set.discard(72)
print(my_set)