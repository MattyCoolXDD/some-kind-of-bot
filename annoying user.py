import requests, threading

url = "https://ptb.discord.com/api/webhooks/1174750600383168672/h-SxbViF7fRingZM0ufjZiOiN2qoakS3is6FnLxN-YKuMBrzU3EZKeW16UP335pozswx"


while True:

    text = input("Message: ")
    def function():
        requests.post(url,json={'content': text})
    function()