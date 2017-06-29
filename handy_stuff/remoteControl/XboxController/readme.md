# Install stuff
- Install Xboxdrv according to tutorial: stuffaboutcode raspberry pi xbox360 controller python
- Install RPi / RPi.GPIO


# How to run stuff

- From root (/Fedya), run with python -m path.to.file.
- e.g. python -m controller.test (without py)


##Run Xbox Controller
- run xboxdrv:
- sudo xboxdrv --silent &

- if error:
- sudo xboxdrv --silent --detach-kernel-driver &

###Test controller input
- python XboxController.py 


## Track controls
- Test with Xbox controls:
- start Xbox controller (see Run Xbox controller)
- from root run: python -m motors/tracksControls

- Autonomous mode:

