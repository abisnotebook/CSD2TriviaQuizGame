# Welcome to the Cook, Serve, Delicious! 2!! Restaurant Trivia Quiz Game
# First, I set up the Print function for the welcome message

print("""
      Welcome to the Cook, Serve, Delicious! 2!! Restaurant Trivia Quiz Game! 
      In this quiz, we have 10 questions to test your knowledge about the restaurants in this game.
      Ready to take the quiz? Go ahead and good luck! :D
      """)

# Then, I set up the questions and their choices

questions = ("What is the name of the endorser of Pizza That!, who sometimes eat at Gree/Itali Casual Dining?: ",
             "What are the rules in Chinese Food: Beverages and Sauces?: ", 
             "What is the only sport that All The Sports Grill is not allowed to view there?: ", 
             "What is the name of Firekicker's mascot?: ", 
             "What is the name of the controversial documentary that featured Biggs Burger?: ", 
             "When did Gree/Itali Casual Dining was established?: ", 
             "When will Bob Newhand's financial fortune deplete?: ", 
             "What is the sauce from Slammy's Old Fashioned BBQ that is banned in 3 EU countries?: ", 
             "What do Contrast Coffee Company also sell, aside from food meals?: ", 
             "Where is Executive's Decision located?: ")

choices = (("A. Jake", 
            "B. Josh", 
            "C. James",  
            "D. Jim"),
           ("A. We accept checks. No substitutions. Open daily and on some holidays.", 
            "B. We do not accept checks. No substitutions. Open daily and on some holidays.", 
            "C. We do not accept checks. Substitutions are allowed. Open daily and on some holidays.", 
            "D. We do not accept checks. No substitutions. Open daily and closed on holidays."),
           ("A. European football", 
            "B. International vape leagues", 
            "C. E-sports", 
            "D. Athletic sports"),
           ("A. Grillin' Phil ", 
            "B. Steamin' Phil", 
            "C. Mixin' Phil", 
            "D. Flamin' Phil"),
           ("A. Supersize Me", 
            "B. Superlarge Me", 
            "C. Suckerpunch Me",
            "D. Suckerlarge Me"),
           ("A. 100 BC", 
            "B. 146 BC", 
            "C. 128 BC", 
            "D. 153 BC"),
           ("A. 2040", 
            "B. 2025", 
            "C. 2002", 
            "D. 2020"),
           ("A. Super duper secret recipe sauce", 
            "B. Super secret recipe sauce",
            "C. Super ultra secret recipe sauce", 
            "D. Super duper ultra secret recipe sauce"),
           ("A. Facial toners", 
            "B. Dishwashing liquids", 
            "C. Laundry pods", 
            "D. Printer toners"),
           ("A. Ground floor of Teragon Tower", 
            "B. Top floor of Teragon Tower", 
            "C. Parking lot of Teragon Tower", 
            "D. Beside Teragon Tower"))

# Afterwards, I set up the questions, guesses, and their overall score

answers = ("A", "B", "C", "D", "C", "B", "A", "B", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------")
    print(question)
    for choice in choices[question_num]:
        print(choice)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 
        print("Correct! Yay!")
    else:
        print(f"Incorrect. {answers[question_num]} is the correct answer.")
    question_num += 1

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

# Lastly, I set up the scores and what the score means to the player

if score == 100:
    print("""
    Be honest. You didn't look at the game while taking this test, did ya? If that's the case,
    you're a CSD 2 Pro! You spent lots of time playing this game, that you probably read about 
    Brysen a lot too. Congratulations!
    """)

elif score == 90:
    print("""
    Not too bad. You might be too engrossed with Leo and Dennis's office rivalry that you might 
    missed any details about each restaurant's history. That's okay. Rivalries can be better than
    historical events, after all.
    """)

elif score == 80:
    print("""
    Not too bad. You might be too engrossed with Leo and Dennis's office rivalry that you might 
    missed any details about each restaurant's history. That's okay. Rivalries can be better than
    historical events, after all.
    """)

elif score == 70:
    print("""
    Not too bad. You might be too engrossed with Leo and Dennis's office rivalry that you might 
    missed any details about each restaurant's history. That's okay. Rivalries can be better than
    historical events, after all.
    """)

elif score == 60:
    print("""
    Not too bad. You might be too engrossed with Leo and Dennis's office rivalry that you might 
    missed any details about each restaurant's history. That's okay. Rivalries can be better than
    historical events, after all.
    """)

elif score == 50:
    print("""
    Somebody's not paying attention on History class. Just kidding. You might know some restaurant 
    trivia here and there, but you don't take it too seriously. Not that we care. We just wanna let
    you have fun playing the game. We wish we have your confidence too.
    """)

elif score == 40:
    print("""
    Somebody's not paying attention on History class. Just kidding. You might know some restaurant 
    trivia here and there, but you don't take it too seriously. Not that we care. We just wanna let
    you have fun playing the game. We wish we have your confidence too.
    """)

elif score == 30:
    print("""
    Somebody's not paying attention on History class. Just kidding. You might know some restaurant 
    trivia here and there, but you don't take it too seriously. Not that we care. We just wanna let
    you have fun playing the game. We wish we have your confidence too.
    """)

elif score == 20:
    print("""
    Whoops. Busy gaming that you have no time to read? Man, we wish that we wouldn't care about that.
    But it's okay. You can retake this quiz if you're still interested. After all, you're here for the
    game. And you can always read the restaurants' histories later after playing. A for the effort, though.
    """)

elif score == 10:
    print("""
    Whoops. Busy gaming that you have no time to read? Man, we wish that we wouldn't care about that.
    But it's okay. You can retake this quiz if you're still interested. After all, you're here for the
    game. And you can always read the restaurants' histories later after playing. A for the effort, though.
    """)

else:
    print("""
    Whoops. Busy gaming that you have no time to read? Man, we wish that we wouldn't care about that.
    But it's okay. You can retake this quiz if you're still interested. After all, you're here for the
    game. And you can always read the restaurants' histories later after playing. A for the effort, though.
    """)

# The copyright for Cook, Serve, Delicious! 2!! is by Vertigo Gaming Inc, 2017. All rights reserved.