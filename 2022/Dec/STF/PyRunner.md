# PyRunner Writeup

First, taking a look at the provided source code, specifically `app.py`.
![](images/Pasted%20image%2020221205190823.png)

We can see that first, there is a list of blacklisted words and characters found in `disallowed`. Additionally, this blacklist is being used in the `textfilter()` function.

If we take a look at the `textfilter()` function, it iterates through the blacklist and strips them out of the `text` value
```
def textfilter(text):
    for i in disallowed:
        if i in text:
            text = text.replace(i, "")
    return text
```

However, this replacement is only one-time per blacklisted keyword/value. Suggesting that suppose we provide the input `evevalal`, this should return the value `eval` giving us the bypass to the blacklist.

As a sanity check, let's test this out in a local python CLI. Assuming we want the string `eval` to be returned, we can try to inject `evevalal` into the `textfilter()` function.

![](images/Pasted%20image%2020221205191533.png)

And yes! It does work as intended. From here, we can essentially add an "embedded-dummy" blacklisted keyword to obtain the desired blacklisted commands we want.

Now, let's take a look at the actual application.

![](images/Pasted%20image%2020221205192024.png)

We are presented with a template for us to run python code. And the boxed line of code seems interesting and could be the vector for our command injection, assumming it is just replacing our provided input into the `<title>` placeholder.

To make sure we are on to the right assumption, let's go back to code review!
![](images/Pasted%20image%2020221205192303.png)

Seeing the `run_template()` function, we can see that the `<title>` placeholder is replaced with our `title` input. And of course this input is passed into the stripping function `textfilter()` as mentioned above. Then the application runs our newly generated python code. 

We can then see that if we provide the input `"`, this will break the entire syntax since the resulting code will become

```
print("Webserver: "")
```

Which is to be expected and gives us the vector to inject arbitary code. 

But here's the catch since we are trying to inject our command injection into the same line, we require semi-colon (which is blacklisted), or do we really need it hmmm? ;)

Perhaps, we could try commas instead. Let's go back to local testing on a python CLI. We can start by trying `import os, os.system('ls')`.
![](images/Pasted%20image%2020221205193542.png)

It seems that this isn't a valid syntax. But what if I pack the import into a function call, maybe `exec`?
![](images/Pasted%20image%2020221205193558.png)

> It seems that in order to use commas to contain 2 lines of codes in one, we require both to be function calls.

And hey! We are able to run commands now and properly this time round within one line. 

Thus, we can craft the following the exploit input into the `title` field.
```
",evevalal("exexecec('impimportort ooss'), ooss.popen('/readflag').read()"))#
```

With that, we can send it as the `title` input field and running the template gives us the flag!

![](images/Pasted%20image%2020221205194656.png)

And to summarize and break down the parts of the exploit input,

```
",evevalal("exexecec('impimportort ooss'), ooss.popen('/readflag').read()"))#
```

1. `"` to escape the current double-quotes string.
2. `,` to result in the following `print(str1, str2)` syntax which is allowed in python.
3. `evevalal` which becomes `eval` to run the `exec()` and `os.popen`command
4. `exexecec` which becomes `exec` to help import our package (i.e. `import os`)
5. `os.popen('/readflag').read()` to run the read flag binary
6. `)#` to close the print function and comment out anything after it.

## Flag 

```
STF22{4ut0m4t3d_c0mm4nd_1nj3ct10n}
```
