# EduCast - HackMIT 2020
Code base for 4 Idiots HackMIT Team - Ritik, Himanshu, Bhavik, and Dhyey - **Click on Logo for Youtube Demo**

[![EduCast Logo](/EduBox/flaskApp/static/EduCastLogo.png)](https://youtu.be/0qiRfVlCKN8)

EduCast is a remote learning platform targeted for students living in under resourced-communities to use online educational media offline on their TVs.

It supplements online learning management systems by eliminating the need for students to have a reliable internet connection and mobile access over many hours. The EduCast's EduStick enables the user to view their class content on a conventional television screen.

1. The student downloads the lecture content from any LMS (a short duration when internet connection will be required)

![IBM EdX Classroom using Skills Network Portal](/img/IBM-edXclassroom.jpeg)

2. The EduStick hosts a wireless LAN which can be used to upload files from the smartphone to the EduStick.

![Flask App for Uploading Files to EduStick](/img/EduBoxFileUpload.jpeg)

3. The Edustick plays back the contents on the TV screen using an AV/Composite or HDMI cable.

  * File Browser for Media Selection:
  
  ![Kivy File Browser](/img/KivyFileBrowser.jpg)
  
  * PDF Document Viewer:
  
  ![Evince PDF](/img/EvincePDF.jpg)
  
  * [Example Lecture](/img/https://youtu.be/la17Z0k_A2s)

The tools we have used in the development of this product:

1. A Raspberry-Pi Single-Board Computer (the EduStick)
  * Kivy (TV user interface for browsing media)
  * LIRC (ir remote for navigating the TV user interface)
  * VLC (video player)
  * Evince (pdf viewer)
  * Flask (for deploying a web app on the Raspberry-Pi)
2. [IBM Skills Network and Open edX](https://hackmit.skillsnetwork.site/home/) (as a learning management platform)
3. Django (to develop an optional customised learning management platform)
