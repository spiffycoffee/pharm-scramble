# pharm-scramble
A command-line tool to help pharmacy students sanely navigate the ASHP Post-Match Scramble

## Features
* Quickly get a nationwide listing of all available positions
* Know at a glance when new programs have opened (or closed)
* Run straight from the terminal, avoid having to dig through the PhorCAS website

## Screenshots
First run:

![First Run](/assets/1st.png?raw=true "First Run")


Subsequent runs:

![Subsequent Runs](/assets/2nd.png?raw=true "Subsequent Runs")

## Requirements
* bash shell - standard on Mac OS X & Linux. Windows users will need Bash for Windows (or MinGW or Cygwin)
* python 2.6+
* wget

## Background (for non-Pharmacists)
After pharmacy school, pharmacy graduates interested in working in hospitals or clinical settings need to complete
a year (or two) of residency. Just like medical students, admission to residency programs is done via computer matching provided by 
the National Matching Services (NMS) - students provide a list of their preferred programs, programs provide a list of their preferred
candidates, and NMS then runs a variation of Gale-Shapley / "The Stable Marriage Problem" on the data to match student and program.

If a student is not matched however, then they are thrust into the highly stressful "Scramble". This is an extremely short period
where candidates must race against the clock to find programs, apply, and interview in hopes of securing a second chance at a 
residency. 

**NOTE:** As of 2016, ASHP has decided to replace the Post-Match Scramble with a second round of matching. That makes this program
obsolete, but I applaud it for being the saner and kinder solution to unmatched candidates. 

## Usage
* ```git clone``` this repo down to your machine
* Edit grab_data.sh using a text editor of your choice, replace username and password with the username and password you use to log
into the PhorCAS website.
* Run ```./grab_data.sh``` repeatedly to check the PhorCAS site.

(To run a demo, copy the sample data (input.json & previous.json) into the folder with the scripts. Run the python script directly
```python parse.py```)
