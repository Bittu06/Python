# Voice Assistant with Music Player 🎵

A Python-based voice assistant that can open websites and play music on command. Similar to Alexa, it responds to voice commands and can handle various tasks.

## 🚀 Features

- Voice command recognition
- Website navigation (LinkedIn, Google, YouTube, Instagram)
- Music playback from YouTube
- Fuzzy matching for song names
- Wake word detection ("Alexa" and variations)

## 🛠️ Prerequisites

Before running this project, make sure you have Python 3.12+ installed. Then install the required packages:

```bash
pip install speechrecognition pyaudio
pip install setuptools
pip install pyttsx3
```

## 📁 Project Structure

### main.py
The core voice assistant implementation:
- Voice recognition and command processing
- Website navigation functionality
- Music playback integration
- Error handling and user feedback

### music.py
Contains the music library configuration:
- Dictionary of song names and YouTube URLs
- Support for Bengali and Hindi songs
- Easy to extend music collection

## 🎯 Commands

1. **Wake Word**: "Alexa" (and variations)
2. **Website Commands**:
   - "open linkedin"
   - "open google"
   - "open youtube"
   - "open instagram"
3. **Music Commands**:
   - "play [song name]"
   - Example: "play Hare Krishna"

## 🎵 Available Songs
- Gori Kalaiya
- Sokhi Bhabona Kahare Bole
- Bhogoban
- Preme Pora Baron
- Hare Krishna

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

## 🚀 Running the Application

1. Activate your virtual environment
2. Run the main script:
   ```bash
   python main.py
   ```
3. Wait for "Initializing Alexa voice assistant..."
4. Say "Alexa" to wake up the assistant
5. Give your command when prompted

## 🤝 Contributing

Feel free to fork this project and add your own improvements. Some ideas:
- Add more commands
- Expand the music library
- Improve voice recognition accuracy
- Add new features

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Bittu Dey
- LinkedIn: [Bittu Dey](https://www.linkedin.com/in/bittu-dey-71242114b/)

## 🔍 Troubleshooting

If you encounter any issues:
1. Check your microphone settings
2. Ensure all dependencies are installed
3. Verify Python version compatibility
4. Check internet connection for voice recognition