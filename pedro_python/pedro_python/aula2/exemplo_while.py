i = 1
# enquando i foi menor que 6

while i < 6:
    print(i)
    i = i + 1 
# somando i + 1

#pare o código enquando o i valer 3

i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i = i + 1

#break = para o looping
#continue = pula para o proximo looping

i = 1
while i < 6:
    i = i + 1
    if i == 3:
        continue 
    print(i)
