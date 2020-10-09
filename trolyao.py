import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_aer = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_aer.listen(mic)
    print("Robot: ....")
    try:
        you = robot_aer.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    if you == "":
        robot_brain = " I can'n hear you, try again"
    elif "hello" in you:
        robot_brain = "Helle Chuyen lai"
    elif "gay" in you:
        robot_brain = " Hoàng Là Một Thằng Gay"
    elif "do" in you:
        robot_brain = " Hoàng thích được Gay"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconnds")
    elif "bye" in you:
        robot_brain = "Bye Chuyen"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
