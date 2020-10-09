import speech_recognition

robot_aer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    audio = robot_aer.listen(mic)
try:
    you = robot_aer.recognize_google(audio)
except :
    you = ""

print("You: " + you)