# HCI-and-Language-Learning

This is a minimum-viable-prototype of a virtual agent named Ana who can help users learn Spanish by conversing with them.

### Presentation Video

https://youtu.be/1AHTaJ58oM4

### Video Demo

https://youtu.be/Rg6j9ergem8

### Installation Instructions

Requires python3 and pip.
The following instructions have only been tested on Windows 10.

After forking/cloning, run `pip install -r requirements.txt`

To generate the voicelines, run `py generateVoice.py`

To begin program, run `py main.py`

The soundboard is programmed into your keyboard as follows:
* keys 1-6 ask questions
* keys q-y offer canned responses to the user's answer
* keys a-h is Ana's answer to the question.
* key 0 tells the user 'I did not understand that'
