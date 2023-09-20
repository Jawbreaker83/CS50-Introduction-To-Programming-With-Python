#  Well, let me propose that we create this animated GIF, not by just using some off-the-shelf program that we downloaded, but by writing our own code. Let me go ahead and run
#  code of costumes.py and create our very own program that's going to take, as input, two or even more image files and then generate an animated GIF from them by essentially 
#  creating this animated GIF by toggling back and forth endlessly between those two images. 

#  Well, how am I going to do this? Well, let's assume that this will be a program called costumes.py that expects two command line arguments, the names of the files, 
#  the individual costumes that we want to animate back and forth. So to do that, I'm going to import sys so that we ultimately have access to sys.argv. I'm then, from this
#  pillow library, going to import support for images specifically. So from PIL import Image-- capital I, as per the library's documentation. 

#  Now I'm going to give myself an empty list called images, just so I have a list in which to store one, or two, or more of these images. And now let me do this.
#  For each argument in sys.argv, I'm going to go ahead and create a new image variable, set it equal to this Image.open function, passing in arg. Now, what is this doing? 

#  I'm proposing that, eventually, I want to be able to run python of costumes.py, and then as command line argument, specify costume1.gif, space, costume2.gif. 
#  So I want to take in those file names from the command line as my arguments. So what am I doing here? Well, I'm iterating over sys.argv all of the words in my command line 
#  arguments. I'm creating a variable called image, and I'm passing to this function, Image.open from the pillow library, that specific argument. And that library is essentially 
#  going to open that image in a way that gives me a lot of functionality for manipulating it, like animating. 

#  Now I'm going to go ahead and append to my images list that particular image. And that's it. So this loop's purpose in life is just to iterate over the command line
#  arguments and open those images using this library. The last line is pretty straightforward. I'm going to say this. 

#  I'm going to grab the first of those images, which is going to be in my list at location 0, and I'm going to save it to disk. That is, I'm going to save this file. 
#  Now, in the past when we use CSVs or text files, I had to do the file opening. 

#  I had to do the file writing, maybe even the closing. I don't need to do that with this library. The pillow library takes care of the opening, the closing, and the
#  saving for me by just calling save. 

#  I'm going to call this save function. And just to leave space, because I have a number of arguments to pass, I'm going to move to another line so it fits. I'm going to
#  pass in the name of the file that I want to create, costumes.gif-- that will be the name of my animated GIF. I'm going to tell this library to save all of the frames that I
#  pass to it-- so the first costume, the second costume, and even more if I gave them. 

#  I'm going to then append to this first image-- the images 0-- the following images, equals this list of images. And this is a bit clever, but I'm going to do this. 
#  I want to append the next image there, images[1]. And now I want to specify a duration of 200 milliseconds for each of these frames, and I want this to loop forever. 
#  And if you specify loop=0, that is time 0, it means it's just not going to loop a finite number of times, but an infinite number of times instead. 

#  And I need to do one other thing. Recall that sys.argv contains not just the words I typed after my program's name, but what else does sys.argv contain? If you think 
#  back to our discussion of command line arguments, what else is sys.argv besides the words I'm about to type, like costume1.gif and costume2? 

#  DAVID MALAN: Indeed, we'll get the original name of the program, costumes.py in this case, which is not a GIF, obviously. So remember that using slices in Python, we 
#  can do this. If sys.argv is a list, and we want to get a slice of that list, everything after the first element, we can do 1, colon, which says, start it location 1, 
#  not 0, and take a slice all the way to the end. So give me everything except the first thing in that list, which, to McKenzie's point, is the name of the program. 

#  Now, if I haven't made any mistakes, let's see what happens. I'm going to run python of costumes.py, and now I'm going to specify the two images that I want to 
#  animate-- so costume1.gif and costume2.gif. What is the code now going to do? Well, to recap, we're using the sys library to access those command line arguments. 
#  We're using the pillow library to treat those files as images and with all the functionality that comes with that library. I'm using this images list just to accumulate 
#  all of these images, one at a time from the command line. 

#  And in lines 7 through 9, I'm just using a loop to iterate over all of them and just add them to this list after opening them with the library. And the last step,
#  which is really just one line of code broken onto three so that it all fits, I'm going to save the first image, but I'm asking the library to append this other image to it 
#  as well-- not bracket 0, but bracket 1. And if I had more, I could express those as well. 

#  I want to save all of these files together. I want to pause 200 milliseconds-- a fifth of a second in between each frame. And I want it to loop infinitely many times. 

#  So now if I cross my fingers as always, hit Enter, nothing bad happened, and that's almost always a good thing. Let me now run code of costumes.gif to open up in VS
#  Code the final image. And what I think I should see is a very happy cat? And indeed. 

#  So now we've seen not only that we can read and write files, be it textually. We can read and now write files that are binary zeros and ones. We've just scratched 
#  the surface. This is using the library called pillow. But ultimately, this is going to give us the ability to read and write files however we want. 

#  So we've now seen that via File I/O, we can manipulate not just textual files, be it TXT files, or CSVs, but even binary files as well. In this case, they happen 
#  to be images. But if we dived in deeper, we could explore audio, and video, and so much more all by way of these simple primitives, this ability, somehow, to
#  read and write files. That's it for now. We'll see you next time. 

# Opens and saves binary files

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
