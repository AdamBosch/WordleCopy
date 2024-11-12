import enchant
with open("valid-wordle-words.txt", "r") as file:
    lines = file.readlines()

dict = enchant.Dict("en_US")
for line in lines:
    if dict.check(line) == False:
        print(line)
