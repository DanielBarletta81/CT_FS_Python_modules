#Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module 
# that asks the user how they are feeling today and responds 
# with a custom message based on the mood entered.

#- Expected Outcome: The program should be able to take a user's
#mood as input (e.g., happy, sad, excited) and return a corresponding custom message.


def mood_response(mood):
    try:

        if mood == "happy":
            print(f"That's great to hear you are feeling {mood}")
        elif mood == "sad":
            print(f"I'm sorry to hear that you are feeling {mood}")
        elif mood == "ambitious":
            print(f"Its good you are feeling {mood}! We have a lot to work on.")
        elif mood == "nervous":
            print(f"Everyone gets {mood} sometimes, but everything will be okay!")
        elif mood == "bored":
            print(f"If you get {mood} easily, you might want to add new hobbies to your routine.")
        else:
            print("Please select a mood from the list.")
    except ValueError:
        print("Please only enter letters.")
  