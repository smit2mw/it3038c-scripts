# it3038c-scripts

Project 2
========


The cript I created is written in BASH which is the native shell language of linux machines. I wrote this on 
a Windows computer and so it is meant to be run on a windows computer. The steps below will guide you on how to run the command on your windows machine.
If you do not want to follow my instructions there is a video you may watch as well that may help you: 

```web
     https://www.youtube.com/watch?v=4zp7m7nkt-A&ab_channel=SavvyNik
```

First you will want to go to this website
```html
     https://www.cygwin.com/
```
Once you have downloaded my script you can use the following command to run it:
```python
    Pillow1.py
```
This script will promt you for the exact file path and then ask you to confirm that you have given it correctly.
The script I have written will use the following code to alter the image in an undesirable way
```python
    im = im.rotate(180)
    im = im.resize((5000,4500))
    im = im.filter(ImageFilter.UnsharpMask(50,200,8))
```
Then it will show your new image automatically with:
```python
    im.show()
```
JavaScript code block to highlight whats up above btw

