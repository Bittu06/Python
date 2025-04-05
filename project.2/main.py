import speech_recognition as sr
import webbrowser
import pyttsx3
from music import music_dict  # Changed from 'music' to 'music_dict'
from difflib import SequenceMatcher
import requests  # Add this with other imports
import time  # Add this with other imports
import eventregistry
from eventregistry import *
import google.generativeai as genai
from PIL import Image  # Changed this line
import os
import json

newsapi = "535b640f-32ce-45a3-b66a-230d5139061f"

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

def generate_image(prompt):
    try:
        # Configure the Gemini API
        genai.configure(api_key="AIzaSyBCy1pehGQZZsn7Sqp3PFsHZxIkAMzLizQ")
        
        # Use the gemini-1.5-pro model for text generation
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Create a more specific prompt for image description
        full_prompt = (
            f"Please provide a vivid, artistic description of {prompt}. "
            "Focus on visual details like colors, shapes, textures, and composition."
        )
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        if response.text:
            print(f"Image Description: {response.text}")
            speak("Here's how I would describe that image:")
            speak(response.text)
        else:
            speak("I couldn't generate a description for that image.")
            
    except Exception as e:
        print(f"Error generating image description: {e}")
        speak("Sorry, I encountered an error while trying to create the image description.")

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
        play_song(command)
    elif "news" in command:
        fetch_business_news()
    elif "generate image" in command or "create image" in command:
        # Extract the image description from the command
        prompt = command.replace("generate image", "").replace("create image", "").strip()
        if prompt:
            generate_image(prompt)
        else:
            speak("Please specify what kind of image you'd like me to generate.")
    else:
        # let Gemini handel the request 
        fetch_gemini_response(command)
        
        """speak("Command not recognized")
        print(f"Command not recognized: {command}")"""

def fetch_gemini_response(command):
    try:
        # API endpoint and key
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        api_key = "AIzaSyBCy1pehGQZZsn7Sqp3PFsHZxIkAMzLizQ"
        
        # Prepare headers and data
        headers = {
            'Content-Type': 'application/json'
        }
        
        data = {
            "contents": [{
                "parts":[{"text": command}]
            }]
        }
        
        # Make the API request
        response = requests.post(
            f"{url}?key={api_key}",
            headers=headers,
            json=data
        )
        
        # Check if request was successful
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result:
                response_text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"Gemini: {response_text}")
                speak(response_text)
            else:
                speak("I couldn't understand the response format.")
        else:
            print(f"API Error: {response.status_code}")
            print(f"Response: {response.text}")
            speak("Sorry, I encountered an error while processing your request.")
            
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        speak("Sorry, I encountered an error while processing your request.")

def fetch_business_news():
    try:
        er = EventRegistry(apiKey="535b640f-32ce-45a3-b66a-230d5139061f")
            
            # Create a query for business news articles from New York
        q = QueryArticlesIter(
                conceptUri = er.getConceptUri("business"),
                categoryUri = er.getCategoryUri("business"),
                sourceLocationUri = er.getLocationUri("Kolkata")
            )

        speak("Here are today's top business news from Kolkata:")
            
            # Get top 5 articles sorted by social media score
        count = 0
        for art in q.execQuery(er, sortBy="socialScore", maxItems=10):
            count += 1
            title = art.get('title', 'No title available')
            speak(f"News {count}: {title}")
            print(f"{count}. {title}")
                # Add a small pause between articles
            time.sleep(1)
                
        if count == 0:
            speak("Sorry, no news articles are available at the moment")
                
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("Sorry, I couldn't fetch the news at this moment.")

def play_song(command):
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
