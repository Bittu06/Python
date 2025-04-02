import speech_recognition as sr
import webbrowser
import pyttsx3
from music import music_dict  # Changed from 'music' to 'music_dict'
from difflib import SequenceMatcher

recognizer = sr.Recognizer()
# Adjust the energy threshold for better wake word detection
recognizer.energy_threshold = 4000
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def similarity_ratio(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def find_closest_match(input_song, available_songs, threshold=0.8):
    input_song = input_song.lower()
    best_match = None
    highest_ratio = 0
    
    for song in available_songs:
        ratio = similarity_ratio(input_song, song)
        if ratio > highest_ratio and ratio >= threshold:
            highest_ratio = ratio
            best_match = song
    
    return best_match

def processCommand(command):
    if any(word in command for word in ["linkedin", "linked in"]):
        url = "https://www.linkedin.com/in/bittu-dey-71242114b/"
        webbrowser.open(url)
        speak("Opening your LinkedIn profile")
    elif "open google" in command:
        url = "https://www.google.com/"
        webbrowser.open(url)
        speak("Opening Google")
    elif "open youtube" in command:
        url = "https://www.youtube.com/"
        webbrowser.open(url)
        speak("Opening YouTube")
    elif "open instagram" in command:
        url = "https://www.instagram.com/"
        webbrowser.open(url)
        speak("Opening Instagram")
    elif "play" in command:
        try:
            # Get everything after "play"
            song_name = " ".join(command.split()[1:])
            # Find the closest match
            matched_song = find_closest_match(song_name, music_dict.keys())
            
            if matched_song:
                url = music_dict[matched_song]
                webbrowser.open(url)
                speak(f"Playing {matched_song}")
            else:
                speak("Song not found in the music library.")
                print(f"Available songs: {', '.join(music_dict.keys())}")
                print(f"You said: {song_name}")
        except IndexError:
            speak("Please specify a song name")
    else:
        speak("Command not recognized")
        print(f"Command not recognized: {command}")

if __name__ == "__main__":
    # Define wake words (add variations of pronunciation)
    WAKE_WORDS = ["alexa", "alex", "alexaa", "Alax", "Alixa", "Alaxa", "Alexha"]
    speak("Initializing Alexa voice assistant...")
    
    while True:
        with sr.Microphone() as source:
            print("\nListening for wake word (Say 'Alexa')...")
            print(f"Energy threshold: {recognizer.energy_threshold}")
            
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration= 0.5)
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
                        
                        processCommand(command)
                        
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