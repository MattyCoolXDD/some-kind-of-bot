import requests, threading

url = "https://ptb.discord.com/api/webhooks/1174743549712011265/j5FdeaLfqfMh4OJWNW0Sqsd32HFJSBNuZeVUu2sQ0ds9hzi2V4QWikGLTOb630fPMjjj"

while True:

    text = input("Message: ")
    def function():
        requests.post(url,json={'content': text})
    function()