#The program should be able to take a user's
#mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

import mood_module
from text_utils import make_title, make_encoded


mood = input("How are you feeling today? (happy/sad/ambitious/nervous/bored) ")
print(mood_module.mood_response(mood))

make_title(mood)
make_encoded(mood)