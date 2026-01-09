import random

#List of dictionaries of people in game
game_data = [

    {
        "name": "Cristiano Ronaldo",
        "follower_count": 630,
        "description": "Footballer",
        "country": "Portugal"
    },

    {
        "name": "Lionel Messi",
        "follower_count": 500,
        "description": "Footballer",
        "country": "Argentina"
    },

    {
        "name": "Selena Gomez",
        "follower_count": 430,
        "description": "Singer and actress",
        "country": "United States"
    },

    {
        "name": "Kylie Jenner",
        "follower_count": 400,
        "description": "Media personality and businesswoman",
        "country": "United States"
    },

    {
        "name": "Dwayne Johnson",
        "follower_count": 410,
        "description": "Actor and entertainer",
        "country": "United States"
    },

    {
        "name": "Ariana Grande",
        "follower_count": 380,
        "description": "Singer and actress",
        "country": "United States"
    },

    {
        "name": "Kim Kardashian",
        "follower_count": 360,
        "description": "Media personality and businesswoman",
        "country": "United States"
    },

    {
        "name": "Beyoncé",
        "follower_count": 320,
        "description": "Singer and performer",
        "country": "United States"
    },

    {
        "name": "Kendall Jenner",
        "follower_count": 290,
        "description": "Model and media personality",
        "country": "United States"
    },

    {
        "name": "Justin Bieber",
        "follower_count": 290,
        "description": "Singer",
        "country": "Canada"
    },

    {
        "name": "Taylor Swift",
        "follower_count": 280,
        "description": "Singer-songwriter",
        "country": "United States"
    },

    {
        "name": "Virat Kohli",
        "follower_count": 270,
        "description": "Cricketer",
        "country": "India"
    },

    {
        "name": "Neymar Jr",
        "follower_count": 220,
        "description": "Footballer",
        "country": "Brazil"
    },

    {
        "name": "Kourtney Kardashian",
        "follower_count": 222,
        "description": "Media personality",
        "country": "United States"
    },

    {
        "name": "Nicki Minaj",
        "follower_count": 230,
        "description": "Rapper and artist",
        "country": "Trinidad and Tobago"
    },

    {
        "name": "Jennifer Lopez",
        "follower_count": 250,
        "description": "Singer, dancer, and actress",
        "country": "United States"
    },

    {
        "name": "Khloé Kardashian",
        "follower_count": 310,
        "description": "Media personality and businesswoman",
        "country": "United States"
    },

    {
        "name": "Cardi B",
        "follower_count": 170,
        "description": "Rapper and entertainer",
        "country": "United States"
    },

    {
        "name": "Zendaya",
        "follower_count": 180,
        "description": "Actress and model",
        "country": "United States"
    },

    {
        "name": "Billie Eilish",
        "follower_count": 120,
        "description": "Singer-songwriter",
        "country": "United States"
    },

    {
        "name": "Chris Hemsworth",
        "follower_count": 100,
        "description": "Actor",
        "country": "Australia"
    },

    {
        "name": "Kevin Hart",
        "follower_count": 180,
        "description": "Comedian and actor",
        "country": "United States"
    },

    {
        "name": "Shakira",
        "follower_count": 90,
        "description": "Singer and performer",
        "country": "Colombia"
    },

    {
        "name": "Dua Lipa",
        "follower_count": 90,
        "description": "Singer and songwriter",
        "country": "United Kingdom"
    },

    {
        "name": "Kylie Minogue",
        "follower_count": 3,
        "description": "Singer and actress",
        "country": "Australia"
    },

    {
        "name": "Snoop Dogg",
        "follower_count": 85,
        "description": "Rapper and entertainer",
        "country": "United States"
    },

    {
        "name": "Katy Perry",
        "follower_count": 200,
        "description": "Singer-songwriter",
        "country": "United States"
    },

    {
        "name": "LeBron James",
        "follower_count": 160,
        "description": "Basketball player",
        "country": "United States"
    },

    {
        "name": "Gigi Hadid",
        "follower_count": 80,
        "description": "Model",
        "country": "United States"
    },

    {
        "name": "Bella Hadid",
        "follower_count": 75,
        "description": "Model",
        "country": "United States"
    },

    {
        "name": "KSI",
        "follower_count": 13,
        "description": "YouTuber and boxer",
        "country": "United Kingdom"
    },

    {
        "name": "MrBeast",
        "follower_count": 50,
        "description": "YouTuber and philanthropist",
        "country": "United States"
    },

    {
        "name": "Bad Bunny",
        "follower_count": 50,
        "description": "Rapper and singer",
        "country": "Puerto Rico"
    },

    {
        "name": "David Beckham",
        "follower_count": 90,
        "description": "Former footballer",
        "country": "United Kingdom"
    },

    {
        "name": "Sabrina Carpenter",
        "follower_count": 40,
        "description": "Singer and actress",
        "country": "United States"
    },

    {
        "name": "Post Malone",
        "follower_count": 45,
        "description": "Rapper and singer",
        "country": "United States"
    },

    {
        "name": "Zlatan Ibrahimović",
        "follower_count": 65,
        "description": "Footballer",
        "country": "Sweden"
    },

    {
        "name": "Will Smith",
        "follower_count": 75,
        "description": "Actor and creator",
        "country": "United States"
    },

    {
        "name": "Shawn Mendes",
        "follower_count": 75,
        "description": "Singer-songwriter",
        "country": "Canada"
    },

    {
        "name": "Millie Bobby Brown",
        "follower_count": 72,
        "description": "Actress",
        "country": "United Kingdom"
    },

    {
        "name": "Tom Holland",
        "follower_count": 90,
        "description": "Actor",
        "country": "United Kingdom"
    },

    {
        "name": "Emma Watson",
        "follower_count": 75,
        "description": "Actress and activist",
        "country": "United Kingdom"
    },

    {
        "name": "Rihanna",
        "follower_count": 150,
        "description": "Singer and businesswoman",
        "country": "Barbados"
    },

    {
        "name": "Drake",
        "follower_count": 146,
        "description": "Rapper and performer",
        "country": "Canada"
    },

    {
        "name": "Ed Sheeran",
        "follower_count": 90,
        "description": "Singer-songwriter",
        "country": "United Kingdom"
    },

    {
        "name": "Maluma",
        "follower_count": 63,
        "description": "Singer and performer",
        "country": "Colombia"
    },

    {
        "name": "Noah Beck",
        "follower_count": 35,
        "description": "TikTok personality",
        "country": "United States"
    },

    {
        "name": "Charli D'Amelio",
        "follower_count": 55,
        "description": "Dancer and influencer",
        "country": "United States"
    },

    {
        "name": "Khaby Lame",
        "follower_count": 80,
        "description": "Content creator",
        "country": "Italy"
    }

]



def start_game():
    score = int(0)
    end_game = False 

    print("\nWelcome to Higher or Lower (Instagram Edition)!")
    print("Follower counts are in millions.\n")

    #need to randomize and pick two names and follower count from the list 
    person1 = random.choice(game_data)
    person2 = random.choice(game_data)

    if person1 == person2:
        person2 = random.choice(game_data)

    while not end_game:

        #picking out the name
        person1_name = person1["name"]
        person2_name = person2["name"]

        #follower count
        person1_followers = person1["follower_count"]
        person2_followers = person2["follower_count"]

        #description
        person1_description = person1["description"]
        person2_description = person2["description"]

        #where they are from
        person1_from = person1["country"]
        person2_from = person2["country"]

        print(f"Compare {person1_name}, a {person1_description}, from {person1_from}\n")
        print("with\n")
        print(f"{person2_name}, a {person2_description}, from {person2_from}\n")


        #changed variable names for cleaner code
        A = person1_followers
        B = person2_followers

        users_guess = input("Who has more followers? A or B? ").upper().strip()

        if users_guess not in ("A", "B"):
            print("Incorrect input - pick A or B.")
            continue

        #the correct answer
        correct_answers = "A" if A > B else "B"

        if users_guess == correct_answers:
            print("You are correct!\n")
            score += 1
            print(f"Score = {correct_answers}")

            if correct_answers == "B":
                person1 = person2

            person2 = random.choice(game_data)
            #incase theyre the same
            while person2 == person1:
                person2 = random.choice(game_data)
        else:
            print("You're not correct!\n")
            print(f"Final score : {score}")
            end_game = True
        
        




start_game()


