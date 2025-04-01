import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
# Adjust the energy threshold for better wake word detection
recognizer.energy_threshold = 4000
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Define wake words (add variations of pronunciation)
    WAKE_WORDS = ["bittu", "bitu", "beetle", "bitter"]
    speak("Initializing voice assistant...")
    
    while True:
        with sr.Microphone() as source:
            print("\nListening for wake word (Say 'Bittu')...")
            print(f"Energy threshold: {recognizer.energy_threshold}")
            
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            audio = recognizer.listen(source)
            
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Heard: {command}")  # Debug print
                
                # Check if any wake word variation is in the command
                if any(word in command for word in WAKE_WORDS):
                    print("Wake word detected!")
                    speak("How can I help you?")
                    print("Listening for command...")
                    
                    # Adjust for ambient noise again
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)
                    
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        print(f"You said: {command}")
                        
                        # More flexible command recognition
                        if any(word in command for word in ["linkedin", "linked in"]):
                            url = "https://www.linkedin.com/in/bittu-dey-71242114b/"
                            webbrowser.open(url)
                            speak("Opening your LinkedIn profile")
                            print(f"Opening URL: {url}")
                        else:
                            speak("Command not recognized")
                            print(f"Command not recognized: {command}")
                    except sr.UnknownValueError:
                        print("Sorry, I did not understand that.")
                        speak("Sorry, I did not understand that.")
            except sr.UnknownValueError:
                print("No speech detected")
                continue
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                speak("Could not request results.")
            except Exception as e:
                print(f"An error occurred: {e}")
                speak("An error occurred.")