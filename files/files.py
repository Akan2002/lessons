# with open ('users.txt', 'w+') as f:
#     login = input('Введите логин:')
#     password = input('Введите пароль:')
#     f.write(login)
#     f.write('\n')
#     f.write(password)
#     f.write('\n')
# with open ('users.txt','r') as f:
#     d = f.read().split()
#     for i in d:
#         if 'w'in i:
#             print(True)
#         else:
#             print(False)
# print('Вы создали успешно файл') 

# from macpath import split


# with open ('python.txt', 'w') as f:
#     f.write('''Python is a widely  used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.''')
# t_words = []
# with open('python.txt', 'r') as f:
#     r = f.read().split()
#     for i in r:
#         if 't' in i or 'T' in i:
#             t_words.append(i)
# print(t_words)        



