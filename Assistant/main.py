import pyttsx3
from rapidChat import *
import promptToImage

engine = pyttsx3.init()  # object creation

# Get the Jarvis voice
jarvis_voice = engine.getProperty('voices')[1]

if jarvis_voice is not None:
    engine.setProperty('voice', jarvis_voice.id)
else:
    print("Jarvis voice not found.")

# set speed of engine
engine.setProperty('rate', 152)

def say(text):
    engine.say(text)
    engine.runAndWait()

optionList = """"
        1. Analyse text data
        2. Analyse Code
        3. Custom Prompt
        4. Prompt to Image    
"""

if __name__ == "__main__":
    print(optionList)

    while True:
        # engine.say("Enter your option")
        # engine.runAndWait()
        option = input("Enter your option: ")
        print()

        if option == "1":
            while True:
                question = input("Enter your question: ")
                print("\n")
                if doWork(question, "textData.txt") == -1:
                    break
                response = doWork(question, "textData.txt")
                print(response, end="\n\n" + 80 * '-' + '\n\n')
                say(response)

        elif option == "2":
            while True:
                question = input("Enter your question: ")
                print("\n")
                if doWork(question, "codeData.txt") == -1:
                    break
                response = doWork(question, "codeData.txt")
                print(response, end="\n\n" + 80 * '-' + '\n\n')
                say(response)

        elif option == "3":
            while True:
                prompt = input("Enter your prompt: ")
                print("\n")
                if prompt == "exit":
                    break
                response = chat(prompt)
                print(response, end="\n\n" + 80 * '-' + '\n\n')
                say(response)

        elif option == "4":
            prompt = input("Enter your prompt: ")
            print("Generating image...")
            response = promptToImage.createImage(prompt)
            print(response, end="\n\n" + 80 * '-' + '\n\n')

        elif option == "exit":
            break

        else:
            print("Invalid option")
            break