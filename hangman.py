import random
words = ["python", "computer", "java", "coding", "cyber"]
#choose a random word
word = random.choice(words)
#letter gussed by the user
guess = ""
#chances left
chances = 6
print("=======================")
print("============Welcome to hanGman game===========")
print("You have only 6 chances")
while chances > 0:
    display = ""
for letter in word:
    if letter in guess:
        display = display + letter
    else:
        display = display + "_"
    print("\nword:", display)
    if display == word:
        print("Congratulations! you won")
        break
    guess = input("Enter guess: ").lower()
    if guess(len) > 1:
        print("please enter only one letter")
    if guess in word:
        print("Correct guess")
    else:
        chances = chances - 1
        print("wrong guess")
        print("chances left:", chances)

    if chances == 0:
      print("\n GameOver")
      print("the word is", word)