import random

quotations = [
    'Winter is coming !!!!', 
    'A Lannister always pays his debts.',
    "Chaos isn't a pit. Chaos is a ladder.",
    'The night is dark and full of terrors.',
    'When you play the game of thrones, you win or you die.'
]

disliked_food = ['Capsicum', 'Bitter Gourd', 'Brussels sprout', 'Celery', 'Beetroot']

recommendations = {
    'Manifest': "Manifest is about a plane that disappears and then mysteriously reappears, diving into the lives of its passengers as they uncover strange secrets.",
    
    'Game of Thrones': "Game of Thrones is a fantasy series with lots of drama, politics, and cool stuff like dragons and knights. It's got a ton of surprises and twists.",
    
    'Friends': "Friends is a funny show about a group of friends living in New York City. It's all about their adventures, relationships, and everyday life.",
    
    'Dark': "Dark is a thrilling show from Germany about time travel, mysterious disappearances, and families with a lot of secrets. It's super intense and makes you think.",
    
    'Alice in Borderland': "Alice in Borderland is a suspenseful series where people find themselves in a weird world full of dangerous games. It's like a crazy adventure with lots of surprises."
}

deutch = 'Dankeschön'

def bold(text):
    return f"\033[1m{text}\033[0m"

def know_me():
    print('\n*********************************')
    
    print('Hello Friend, here are some of secrets about me !!! \n')
    
    favorite_quotation = random.choice(quotations)
    my_disliked_food = random.choice(disliked_food)
    favorite_series = random.choice(list(recommendations.keys()))
    
    print(f'• My favorite quotation from Game of Thrones series is: {bold(favorite_quotation)} \n')
    print(f'• I really dont like eating {bold(my_disliked_food)}.\n')
    print(f'• My favorite TV series is {bold(favorite_series)}, and here are the details about it:')
    print(f'  - {recommendations[favorite_series]} \n')

    print(f'• You should really know the German word {bold(deutch)}, which means Thank you !!! \n')  
    
know_me()