# def solid():
#     global param
#     a = input('param: ')
#     if int(a) == 1:
#         param = False

# param = True
# while param is True:
#     solid()
    
# ask = None
# if not ask:
#     print(2)

# a = 2
# def solid():
#     while True:
#         if a == 2:
#             continue

#     print("DONE")

# solid()

# open('test_reflections.txt', 'a')
# file.truncate(0)
# open('date_log.txt', 'a')


with open('reflections.txt', 'a') as file:
    file.truncate(0)

with open('date_log.txt', 'a') as file:
    file.truncate(0)
