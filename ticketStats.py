#!/usr/bin/python
#
# Written by Joshthehero91
#  Importing the nessecary modules: 
#   'requests' to make the httpd request for the URL.
#
import requests

#
#  Getting the sites data:
#   This calls an internal site so this will need to be ran on Company's network.
#   Pulling admin data.
#   In this case, it's mine.
#   Also ensures HTTP response is 200 before proceeding:
#
url = "https://wallboard.supportdev.company.com/api/data/agents/joshthehero91"
html = requests.get(url)
text = html.text
text = text.split('"')
end = len(text)

if html.status_code != 200:
    raise requests.ConnectionError("Expected status code 200, but got {}".format(page.status_code))

#
# Here's the magic:
#  Loop through the lines of the URL and if a ticket status is found as 'work_in_progress',
#  pull the status, ticket number, and subject number.
#  Makes it pretty!
#
print()
print("Active tickets:")
print("---------------")
print()
for i in range(0, end):
    if text[i] == 'work_in_progress':
        hit = i
        sta = int(hit)
        tix = int(int(hit) + int(8))
        sub = int(int(hit) + int(18))
        words = "| Status: " + text[sta] + " | Ticket: " + text[tix] + " | Subject: " + text[sub] + " |"
        dashes = int(len(words))
        print("-" * dashes)
        print(words)
        print("-" * dashes)

print()
print()
print("That's it. ya bum!")
###
#
#
# The folling is for debugging
#
###
#print()
#print()
#print()
#print("-"*10+" Debugging " +"-"*10)        
#print(text)
