# Berkshire Girls Code - Online Workshop

_January 10th, 2015_ - 10am - 2pm PST/1pm - 5pm EST

**NOTE**: Have questions?  Email me directly [lynn@lynnroot.com](mailto://lynn@lynnroot.com)

## Materials

No need to review any of this before the workshop:

* \[INCOMPLETE\] [Workshop](http://nbviewer.ipython.org/gist/econchick/5200d52f9af57cbd040d) - this will be the complete workshop once I've finished the last bit + formatted it better
* [COMING SOON] A live demo will be found [here](https://berkshire-girls-code.herokuapp.com).

## Workshop setup

### For Attendees:

**PLEASE**: Read through all these instructions sometime before the event (at least a couple of hours, preferrably a day or two before) so you understand what needs to happen for the workshop!

1. SOMETIME BEFORE THE EVENT: Create an account and setup your workspace on c9.io.  Follow [these](SETUP.md) instructions!
2. AT THE START OF THE EVENT - I recommend trying to connect to this chatroom beforehand so you're familiar with it.
    - Join our chatroom by 12:45pm EST so we can have a smooth start!
    - Connect to our chatroom [here](http://webchat.freenode.net/?channels=%23berkshire-gc-code)
        - Choose whatever nickname you'd like
        - Do *not* check the box "Auth to services"
        - Enter the reCAPTCHA code
        - Press "Connect"
    - To learn more about this type of chatroom (IRC), check out this [PyLadies Resource](http://www.pyladies.com/blog/irc-resources/)
3. DURING THE EVENT - Once everyone's in the chat room and seemingly setup okay, I will post a link in the chatroom to the broadcast video that I will be using to teach the class.  My username is "roguelynn".
4. DURING THE EVENT - There will be mentors in the chatroom ready to help out with any questions during the workshop.  Just go ahead and ask your question in the chatroom and someone will respond.  Don't be shy!

### For Mentors:

##### Required:

1. I highly suggest using [c9.io](https://c9.io) instead of or along side your own computer environment.  This is so you can understand the issues that the attendees may be having.
    1. Follow the setup for c9.io [here](SETUP.md).
    2. c9.io uses Ubuntu with Python 2.7.6 and virtualenv already installed.  There is a text editor/IDE as well as a Terminal environment that attendees will get familiar with.
    3. I'm using c9.io rather than being bogged down in setting up various different machines remotely :)  I am in no way affiliated with them, though! Just a huge fan :)
2. We will be using IRC.  Note that my nickname on IRC is "roguelynn".
    1. If you already use IRC, we will be in the #berkshire-gc-code channel on Freenode.
    2. If you do not use IRC and/or have not set it up, you can either:
        1. **[EASY]** Use the webchat [here](http://webchat.freenode.net/?channels=%23berkshire-gc-code) - just choose a Nickname, enter the reCAPTCHA code and click 'connect'.  I suggest this if you don't think you'll use IRC again anytime soon, or just don't want to wrestle with the setup.
        2. **[INTERMEDIATE]** Follow the setup steps [here](http://www.pyladies.com/blog/irc-resources/) then connect to the '#berkshire-gc-code' channel.  I suggest this if you plan on using IRC in the future.

##### Optional:
b
If you want to get familiar with the course beforehand, feel free to check out the materials listed below.

In the second half of the workshop, we will be making a micro Flask site.  If you want to try it out, here's how to set it up (on your c9.io account, and/or your local computer).

**Note**: To do this, you will need to [register an application](https://developer.spotify.com/my-applications/) with Spotify (and therefore have an account at Spotify - [create one for free](https://www.spotify.com/us/signup/?forward_url=%2Fus%2Faccount%2Foverview%2F) if you don't have one already) to get a client ID and secret.  For the tutorial, the attendees will be using client IDs & secrets that I will provide for them so they don't have to create accounts and such.


```bash
$ git clone https://github.com/econchick/berkshire-girls-code
$ cd berkshire-girls-code
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
# Edit the `app/config/local.py` file and input your Spotify Client ID & Secret.
# To run the micro site:
$ python run.py  # then navigate to http://localhost:5000
```
