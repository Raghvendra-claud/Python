import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170) 
engine.setProperty('volume', 1.0)

# Get current hour as an integer for easier comparison
hour = int(time.strftime('%H'))
timestamp_str = time.asctime()

# Determine Greeting
if 6 <= hour < 12:
    greeting = "Good Morning Sir!"
elif 12 <= hour < 18:
    greeting = "Good Afternoon Sir!"
elif 18 <= hour < 22:
    greeting = "Good Evening Sir!"
else:
    greeting = "Good Night Sir!"

# Execution
print(f"Time: {timestamp_str}")
engine.say(f"The time is {timestamp_str}")
engine.say(greeting)
engine.runAndWait()