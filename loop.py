# names = [123,456,789,'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# numbers = []
# letters = []
# for i in names:
#     if type (i) == str:
#         letters.append(i)
#     else: 
#             numbers.append(i)
# print(numbers)
# print(letters)     

# lang1 = 'go'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages: 
#     if i == lang1:
#      print("его там нет")

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:b = []
#     if i == "javascript":
#        break
#     print(i)
# b = 1
# a = 7
# for i in range(5):
#     b *=  a 
# print(b

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i , j in enumerate (languages):
#     print(i + 1, j)

# a = []
# b = []
# for i in range(1,11):
#     a.append(i)
#     b.append(i)
# a.reverse()
# for i in a:
#     if i < 10:
#         b.append(i)
#  print(b)


# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)

# lst = [[1,2,3], [4,5,6], [7,8,9]]
# lst2 = []
# for i in lst:
#     for j in i:
#         lst2.append(j)
# print(lst2)
         
# lst = [[1,2,3], ['first','second','third'], [7,8,9]]
# letters = []
# numbers = []
# for i in lst:
#     for j in i:
#         if type(j) == str:
#             letters.append(j) 
#         else:
#             numbers.append(j) 
# print(numbers)
# print(letters)
numbers = []
while True:
    command = input('Введи четные числа,end для выхода:')
    numbers.append(command)
    if command == 'end':
        break
numbers.pop()
print(numbers)

a = '' 
for i in numbers:
    a += i
    a += ', '
print(f'Вы ввели {a}')

b = 0
for i in numbers:
    b += int(i)
print(f'Сумма{b}')

c = b/len(numbers)
print(f'Среднее ариф {c}')


