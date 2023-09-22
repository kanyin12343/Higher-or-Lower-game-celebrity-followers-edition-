
from art import logo
print(logo)

import random 
from game_data import data
from replit import clear
score = 0
game_over = False

#Initialise with a random data input
entry1 = random.choice(data)
while not game_over:
    # Gather details from the initial entry.
    name1 = entry1['name']
    description1 = entry1['description']
    country1 = entry1['country']
    followers1 = entry1['follower_count']
    
    # Show information for option A
    print(f"Compare A: {name1}, a {description1}, from {country1}")
    from art import vs
    print(vs)

    # Choose a random alternative for option B, making sure it differs from option A.
    entry2 = random.choice(data)
    while entry2 == entry1:
        entry2 = random.choice(data)
        
    # Information from the second item (option B) should be extracted.
    name2 = entry2['name']
    description2 = entry2['description']
    country2 = entry2['country']
    followers2 = entry2['follower_count']

    # Show information for option B
    print(f"Against B: {name2}, a {description2}, from {country2}")
    
    # Ask users to predict which person has the most followers.
    guess = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    print(logo)

    # Verify if the user's assumption was accurate.
    if guess == 'A':
        if followers1 > followers2:
            score += 1
            print(f"You guessed it right! Your current score: {score}\n")
        else:
            game_over = True
            print(f"Sorry, that's incorrect. Game over! Your current score: {score}\n")
    elif guess == 'B':
        if followers1< followers2:
            score += 1
            print(f"You guessed it right! Your current score: {score}\n ")
        else:
            game_over = True
            print(f"Sorry, that's incorrect. Game over! Your current score: {score}\n")
    else:
        game_over = True
        print(f"Invalid input. Game over! Your current score: {score}\n")
    
    entry1 = entry2  # Switch the positions of options A and B
    
   


