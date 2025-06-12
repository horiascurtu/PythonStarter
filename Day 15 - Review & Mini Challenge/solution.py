score = 0

def ask(question, answer):
    global score
    if input(question).lower() == answer:
        score += 1

ask("What color is the sky? ", "blue")
ask("What is 2+2? ", "4")
ask("What language are we learning? ", "python")

print("Your score:", score)
