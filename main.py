import eel
import random

eel.init("web")  # Folder where HTML/CSS/JS files are stored

choices = {-1: "Water", 0: "Gun", 1: "Snake"}
youDict = {"s": 1, "w": -1, "g": 0}

@eel.expose  # Expose function to JS
def play(choice):
    computer = random.choice([-1, 0, 1])
    you = youDict[choice]
    result = ""

    if computer == you:
        result = "It's a Draw!"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result = "🎉 You Win!"
    else:
        result = "😢 You Lose!"

    return {
        "user_choice": choices[you],
        "computer_choice": choices[computer],
        "result": result
    }

eel.start("index.html", size=(500, 500))
