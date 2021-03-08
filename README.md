# it3038c-scripts

Lab 7
========


I created a Python3 script and stored in it folder Labs. The script is called Pillow1.py
Assuming you already have Python3 installed you must run these commands:
```powershell
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
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

```javascript
JavaScript code block to highlight whats up above btw
```
