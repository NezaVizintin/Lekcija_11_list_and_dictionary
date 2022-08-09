import random
import json
import datetime
import operator

secret = random.randint(1, 30)
attempts = 0

name = input("Enter player name: ")
wrong_guesses = []


print("Top scores: ")
with open("score_list.json", "r") as score_file: # opens score file to read
    score_list = json.loads(score_file.read())
    if score_list: # checks it score_list is empty
        score_list.sort(key=operator.itemgetter('attempts')) #sorts score_list by best score ascending
        for x in range(5): # shows top 5 results
            print(score_list[x].get("name") + ": " + str(score_list[x]["attempts"]) + " attempts, date: " + score_list[x].get("date"))

while True:
    print()
    print("Previous guesses: " + str(wrong_guesses))
    guess = int(input("Guess the secret number (between 1 and 30): "))
    print()
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "wrong_guesses": wrong_guesses})
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You guessed it! The secret number is " + str(guess))
        print("Attempts needed: " + str(attempts))
        break
    elif guess < secret:
        wrong_guesses.append(guess)
        print("Not quite there, try going a bit higher!")
    elif guess > secret:
        wrong_guesses.append(guess)
        print("Not quite there, try going a bit lower!")
