# Sound Processing Project
## Glossary:
### 1. Setup
### 2. How To Run
#### a. sound extraction
#### b. sound fragmentation
#### c. sound processing

## 1. Setup
### a. Python and PIP
Most computers come with python version > 3 preinstalled. To verify that you have the proper program, open a terminal and run:<br>
`python3 --version`.<br>
Similarly, you should do the same for pip:<br>
`pip --version`

The output of the previous command should look something like this:<br>
`Python 3.x.y` and `pip 21.1.2 from /path/to/your/pip/package/pip (python 3.x)`, respectively.<br>
Here, `x` and `y` are the minor, and tag versions of your python environment, respectively.

If you dont have python installed, depending on your machine you will need to run one of the following commands:<br>
For Linux/Unix machines, run:<br>
`sudo apt-get update && sudo apt-get install python3.x && apt-get install `

For Mac, run:<br>
`brew update && brew install python3.x`

Obviously, you will need to replace the `x` by the version you are interested in, e.g. <br>
`brew install python3.9` for the 3.9 version of python

For Windows, run:<br>
`I dont know how to do that, you'll have to do some research`

For pip, simply re-run the above command depending on your environment, and replace `python3.x` by `pip`

### a. Virtual environment
It is not necessary to create a virtual environment but is highly recommended to not have the libraries installed by this program interfere with your current environment. If you choose to opt out of this step, make sure to use `python3` instead of `python` in the rest of the insctructions. I will mention this once more in a <b>NOTE</b> section.<br>

To create a virtual environment, run:<br>
`python3 -m venv .venv`<br>
To activate it, run:<br>
`source .venv/bin/activate`<br>
Your virtual environment is ready.
### b. Requirements
This step is necessary and the program will most likely not work if you do not run this step
To install the necessary python libraries, run:<br>
`pip install -r requirements.txt`<br>
If there are no errors from the output, you should be ready to run the script. Proceed to the next step.

## 2. How To Run
### a. Sound Extraction
The first script `sound_extraction.py` extracts sound from a movie file that the user introduces to the script. For now, only 3 movie formats are allowed: `mov`, `mp4`, and `avi`. If the extension of your media file doesn't match any of the ones mentioned, please ensure to convert it to one of the allowed formats.<br>
The output will be a `wav` file of the same name. e.g. if your movie is called `test1.mov`, the resulting sound file will be `test1.wav`.<br>
While other sound formats can be be handled by the python library used in the program, only `wav`are considered since signal processing makes it easier.<br> 
A draw-back from this is that it takes up more local disk space.<br>
For short files (1-2 minutes), it shouldn't be an issue.<br>
To run the sound extraction script, simply run:<br>
`python sound_extraction.py [filename]`

<b>NOTE</b>: If you are <b>NOT</b> using a virtual environment, you will need to run this instead:<br>
`python3 sound_extraction.py [filename]`<br>
If the script ran properly, you should see a new file in your direction with a `wav` extension.

### b. Signal Fragmentation
The second script takes the output of the first script and uses it as its input. It requires 2 more arguments, a start time and a end time.<br>
These parameters instruct the script to splice the wav file between that time window.<br>
To run:<br>
`python sound_fragmentation.py [wav-output-from-previous-job][start-time][end-time]`<br>
This assumes the user knows exactly what portion of the file they are interested in, of course.<br>
If the script ran properly, you should a new wav file with the time fragment specified in the name.

### c. Signal Processing
This third and last script does a frequency analysis of the fragment from the previous step.<br>
To run:<br>
`python sound_processing.py [wav-fragment-from-previous-job]`<br>
If the script ran properly, you should see a new window open with plots and metrics in the console.