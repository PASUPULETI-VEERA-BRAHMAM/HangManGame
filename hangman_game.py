import random
words=['apple','elephant','banana','house','zebra','love','restaurant']
c=random.choice(words)
l=[]
for x in c: l.append(x)
ul=[]
length=len(l)
for i in l: ul.append('_')
print(ul)

hangman=['''
    +----+
    |    |      
    0    |
   /|\   |
   / \   |
         |
    ====== 
''','''
    +----+
    |    |      
    0    |
   /|\   |
   /     |
         |
    ======
''','''
    +----+
    |    |      
    0    |
   /|\   |
         |
         |
    ======
''','''
    +----+
    |    |      
    0    |
   /|    |
         |
         |
    ======
''','''
    +----+
    |    |      
    0    |
    |    |
         |
         |
    ======
''','''
    +----+
    |    |      
    0    |
         |
         |
         |
    ======
''','''
    +----+
    |    |      
         |
         |
         |
         |
    ======''']
life=6
while True:
    if life==0 or ul==l:
        break
    else:
        guess = input('Guess the character: ')
        if guess in l:
            print('Your guess is correct')
            for i in range(length):
                if guess == l[i]:
                    ul[i]=guess
            print(ul)
        else:
            print('Your guess is wrong')
            life-=1
        print(f'you are at stage {hangman[life]}')
if ul==l:
    print('You Won')
else:
    print('You Lost')
