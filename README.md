# EE180DA Projects and Tutorials
#### By Henry Kou (participant)
##### UID: 204921239, Lab Section 1A
### Class Syllabus
[EE180D by Kambiz Shoarinejad, Fall 2020](https://ccle.ucla.edu/pluginfile.php/3532596/local_ucla_syllabus/syllabus/74925/ECE180DA_Fall2020_syllabus_1%20(Last%20modified%202020-09-16--18-21).pdf)

## Tutorial 0 (Week 0)
[Tutorial Prompt](https://ccle.ucla.edu/mod/resource/view.php?id=3250395)

- Task 1: 
Open a Git-maintained public repository ”180DA-WarmUp” in your personal Github
account on Github and add your name, Github ID in the correct teamID that you want to
be a part of (for the capstone project) here. Your repo for this session should be visible to
me at www.github.com/your github id/180DA-WarmUp/.
Play around with SourceTree (optional). Watch out for and accept an invite after class
to join the 180D Github organization which will be the main hub for your capstone project,
NOT your tutorial code - that will be in your own local Github account.

- Task 2: 
In the local repo, please finish section 3 and within the virtual environment, open
a new file test.txt and save some sample text. Add, commit and push to remote repo and
verify that it shows up in your GUIs (Github, SourceTree).

- Task 3:
Task 3: The following code is written in SublimeText (the color codes are fantastic in this
editor IMO). Please type it into your editor and save it as test.py IN the local repo. Run
(AFTER activating the VIRT. ENV) as: $ python3 filename.py. To finish off, please add, commit and push changes to your remote repo. Now you should
have 2 files in the remote location (please verify)

- Task 4:
Do this task individually. You can share your results with your teammates to see if their
results are similar to yours.
1. Choose something that is relatively monochromatic with a color fairly different from
your background surroundings (a water bottle, a piece of clothing). Try to create
a video stream where you track this object with a bounding box surrounding it by
thresholding HSV or RGB values. Is HSV or RGB typically better? How large is the
threshold range that you need to track the object?
2. Now change the lighting condition (turn on or off the lights or turn on your phone
flashlight on the object). Is there a major difference in the tracking ability of your
object?
3. Now navigate to a Color Picker on your phone (Zoom into the color zone so that it
covers a good portion of your phone screen). Since you can pick your color with the
website, see if that is the color (with a small range) that you can pick up with your
camera. Does changing your phone brightness help or hurt with how your code is able
to track the color?
4. Create a new piece of code that can determine the “dominant” color in a designated
(central) rectangle in your video feed (Use K-Means, see a tutorial to find an image’s
dominant colors). Use your non-phone object and change the brightness of its surroundings. Note the change of the color. Do the same with your phone. Is one or the
other more robust to brightness?
You CAN use any of the BASELINE scripts linked above. CITE the references AND provide
any improvements to this baseline that you may have accomplished (IN a header comment in
the .py script). Please push your contributions to your public repo, INCLUDING a screenshot
of the results.

#### List of References for Tutorial 0
- [Drawing in OpenCV](https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html)
- [Bound boxes in video](https://stackoverflow.com/questions/35533538/creating-bounding-box-across-an-object-in-a-video)
- [Contour Features](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features)
- [Background Subtraction](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html#background-subtraction)
- [Changing Colorspace](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces)
- [Detect RGB in image](https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/)