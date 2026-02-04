from google import genai

client = genai.Client(api_key='AIzaSyBQd759VUItncOEO3hKHr-tD0ahc6ri1K0')

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="why do you exist?"
)

print(response.text)
