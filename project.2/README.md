# Alexa-like Voice Assistant 🎵🤖

A Python-based voice assistant that can handle various tasks including music playback, web navigation, news updates, and AI-powered conversations using the Gemini API.

## 🚀 Features

- Voice command recognition with wake word "Alexa"
- Website navigation (LinkedIn, Google, YouTube, Instagram)
- Music playback from YouTube with fuzzy matching
- Business news updates from Kolkata
- AI-powered conversations using Google's Gemini API
- Image description generation
- Natural language processing
- Flexible wake word detection

## 🛠️ Prerequisites

Before running this project, make sure you have Python 3.12+ installed. Then install the required packages:

```bash
pip install speechrecognition
pip install pyaudio
pip install pyttsx3
pip install google-generativeai
pip install requests
pip install Pillow
pip install eventregistry
```

## 📁 Project Structure

### main.py
The core voice assistant implementation:
- Voice recognition and wake word detection
- Command processing and routing
- API integrations (Gemini, EventRegistry)
- Error handling and feedback

### music.py
Music library configuration:
- Dictionary of song names and YouTube URLs
- Bengali and Hindi songs support
- Fuzzy matching for song names

## 🎯 Commands

1. **Wake Word**: "Alexa" (and variations like "Alex", "Alexaa")

2. **Website Navigation**:
   - "open linkedin"
   - "open google"
   - "open youtube"
   - "open instagram"

3. **Music Playback**:
   - "play [song name]"
   - Supports fuzzy matching for song names
   - Example: "play Hare Krishna"

4. **News Updates**:
   - "news"
   - "tell me the news"
   - Gets latest business news from Kolkata

5. **Image Descriptions**:
   - "generate image of [description]"
   - "create image of [description]"

6. **AI Conversations**:
   - Ask any question
   - Get detailed responses powered by Gemini AI

## 🎵 Available Songs
- Gori Kalaiya
- Sokhi Bhabona Kahare Bole
- Bhogoban
- Preme Pora Baron
- Hare Krishna

## ⚙️ API Keys Required
- Gemini API Key
- EventRegistry API Key
- News API Key

## 🔧 Setup & Configuration

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**:
   ```bash
   # Windows
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**:
   Update the following keys in main.py:
   - `GEMINI_API_KEY`
   - `NEWS_API_KEY`
   - `EVENTREGISTRY_API_KEY`

## 🚀 Running the Application

1. Ensure your virtual environment is activated
2. Check your microphone settings
3. Run the main script:
   ```bash
   python main.py
   ```
4. Wait for "Initializing Alexa voice assistant..."
5. Say "Alexa" to wake up the assistant
6. Give your command when prompted

## 🔍 Troubleshooting

1. **Microphone Issues**:
   - Check system audio settings
   - Verify microphone permissions
   - Adjust energy threshold if needed

2. **API Errors**:
   - Verify API keys are valid
   - Check internet connection
   - Review API quotas and limits

3. **Voice Recognition**:
   - Speak clearly and at normal speed
   - Minimize background noise
   - Check microphone volume levels

## 👤 Author

Bittu Dey
- LinkedIn: [Bittu Dey](https://www.linkedin.com/in/bittu-dey-71242114b/)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.