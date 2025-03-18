# i have a api key from gemini 
# i will use the api key to get the data from gemini
# I want to chatbot which will give all kind of answers using gemini apipip install -q -U google-genai

from google import genai

client = genai.Client(api_key="AIzaSyBw99X-nMitysli0xdKum4lbUlMoicRfKU")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Who composed the song 'Ode to Joy' and when? Which larger classical composition is this song part of?"
)
print(response.text)