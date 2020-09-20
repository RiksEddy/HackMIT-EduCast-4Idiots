# HackMIT
Code base for 4 Idiots HackMIT team

![EduCast Logo](/EduBox/flaskApp/static/logo.png)

EduCast is a device to supplement online learning management systems on the student side by eliminating the requirement of reliable internet connectivity and mobile access for an extended period of time. The EduCast's EduStick allows the user to view their class content content on a regular television screen, completely phone and internet independent.

1. The student downloads the lecture content from any LMS (a short duration when internet connection will be required)

2. The EduStick hosts a wireless LAN which can be used to upload files from the smartphone to the EduStick.

3. The Edustick telecasts the contents on the TV screen using an AV/TV or HDMI cable.

The tools we have used in the development of this product:

1. A Raspberry-Pi Microcontroller (the EduStick)
  * Kivy (TV user interface for browsing media)
  * LIRC (ir remote for navigating the TV user interface)
  * VLC (video player)
  * Evince (pdf viewer)
  * Flask (for deploying a web app on the Raspberry-Pi)
2. IBM open edX (as a learning management platform)
3. Django (to develop an optional customised learning management platform)
