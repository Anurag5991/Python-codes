sceret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != sceret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input ("Enter guess : ")
        guess_count +=1
    else:
        out_of_guesses =  True
if out_of_guesses:
    print (" you are out of guesses")
else:
    print ("You win")
