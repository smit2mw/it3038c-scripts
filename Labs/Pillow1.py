from PIL import Image,ImageFilter
#Open image using Image module
pathGiven = input("give me the path of the file: ")
print("Is this the correct path: ", pathGiven, "?")
ans = input()
if ans == "yes":
    im = Image.open(pathGiven)
    im.load
    im = im.rotate(180)
    im = im.resize((5000,4500))
    im = im.filter(ImageFilter.UnsharpMask(50,200,8))
    im.show()
elif ans == "no":
    print("Please run script again.")