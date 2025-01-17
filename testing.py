import random

messages = [
    "Today you will get a surprise from the universe.",
    "Stay calm.",
    "Be positive, you are in the right place at the right time.",
    "You are loved.",
    "It's a perfect day to rest."
]

def luck_message():
    return random.choice(messages) 
print(luck_message())
print("------------------------")
# --------------------------------------------------------------------------------------------

def all_messages():
    selected_msg = random.sample(range(len(messages)), len(messages))
    for i in selected_msg:
        yield messages[i]

for message in all_messages():
    print(message)        
   