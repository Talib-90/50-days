import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 364,
        'description': 'Social Media Platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and Professional Wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and Actress',
        'country': 'United States'
    }
]

score = 0
is_gameover = False
random_data1 = random.choice(data)
random_data2 = random.choice(data)


if random_data1 == random_data2:
    random_data2 = random.choice(data)

while not is_gameover:
    print(f"Compare A: {random_data1["name"]}, {random_data1["description"]}, from {random_data1["country"]}.")
    print("VS")
    print(f"Against B: {random_data2["name"]}, {random_data2["description"]}, from {random_data2["country"]}.")
    choose = input("Who has more followers? type 'a' or 'b' ").lower()
    
    if random_data1['follower_count'] > random_data2['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'
    
    if choose == correct_answer:
        score += 1
        print(f"You're right! final score: {score}")
    
        random_data1 = random_data2
        random_data2 = random.choice(data)

        while random_data1 == random_data2:
            random_data2 = random.choice(data)

    else:
        is_gameover = True
        print(f"Sorry! That's wrong Final score is:{score}")