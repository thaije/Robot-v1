# Install Camera
- Enable picamera with sudo raspi-config
- Install python picamera library with sudo apt-get update, followed by sudo apt-get install python-picamera



### Streaming
nc.traditional -l -p 5000 | mplayer -fps 60 -cache 1024 -

