This folder contains the beginning of a migration to ROS (and some ROS tutorials I did), with ROS on the RPI as master and a laptop with ROS as slave for image processing and other computationally expensive tasks.
As of now I have decided to continue with ROS with my next project with a better robot such as a turtlebot.



# Ros
- slave\_pc and master\_rpi each contain a catkin workspace.


## Ros Master Raspberry PI
- Run roscore

## Ros slave PC
- 


## How to ROS
- Topic: node publishes messages, node subscribed to a topic can receive these messages
- Services: A client node sends a request (what is 2+1?) to a Service node, the service node sends a response(2+1=3) back to the client
- Parameters: rosparam can be used to set, get, load, dump, delete and list parameters (e.g. intialization paramters).


## ROS setup
### RPI (master):
Handling hardware:
- speaker: play music
- microphone: record audio / stream audio
- sonar: publish data / set frequency
- servo: publish data / set frequency
- motors: publish data / set speeds
- wheel encoders: publish data / clear
- camera data: record video / stream video / take picture / publish pictures

### Computer (slave)
Handling processing:
- Speech recognition
- Speech synthesis 
- Process camera data
   - vslam
   - object recogntion / tracking
   - face recognition / tracking
   - structure from motion? (create 3d model from camera data)
- Slam / navigation using odometry + sonar data


## Possible improvements
- Add MPU for better odometry / slam
- Add laser pointer for mosquito hunting
- Add manuel controls with xbox controller
