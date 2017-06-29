

# Description:
# Run:
# sudo pigpiod
# sudo python robot.py


import handy_stuff.functions.functions as functions
from motors.servos.servoWirPWM import Servo 
from motors.wheels.sn75SoftwarePwm import Motor
from motors.wheels.pigpio_encoder import decoder
from motors.wheels.pigpio_encoder_functions import *
from proximity_sensors.sonar.srte import sonar



class Robot:

    
    def __init__(self):

        #self.estimated_pose = None
        #self.estimated_pose.scalar_update( 0, 0, 0 )

        # setup wheels
        self.wheel_radius = 45
        self.wheel_base_length = -1
        self.leftWheel = Motor(23, 25, 24, diameter=9.0) 
        self.rightWheel = Motor(11, 10, 9, diameter=9.0) 
        self.wheels = [self.leftWheel, self.rightWheel]

        # setup servos
        # Vertical servo, 55 is down, 120 is up
        # horizontal servo, 30 is left
        self.verticalServo = Servo(pin=18, minPos=55, maxPos=120, centerPosition=62)
        self.horizontalServo = Servo(pin=13, minPos=30, maxPos=115, centerPosition=72)
        self.servos = [self.verticalServo, self.horizontalServo]

        # start pigpio
        pi = pigpio.pi()
        if not pi.connected:
            exit()
        
        # Setup wheel encoders [left, right]
        self.wheel_encoder_ticks_per_revolution = 360
        decoderLeft = decoder(pi, 14, 15, callback_encoder_leftwheel)
        decoderRight = decoder(pi, 5, 6, callback_encoder_rightwheel)
        self.decoders = [decoderLeft, decoderRight]
        self.wheels_ticks_left = 0
        self.wheels_ticks_right = 0
        self.prev_ticks_left = 0
        self.prev_ticks_right = 0

        # setup sonars
        # [Head sonar, right sonar, left sonar]
        self.sonars = []
        self.proximity = []
        # Head sonar
        sonars.append(sonar(pi, None, 21))
        # Front sonars
        sonars.append(sonar(pi, None, 20))
        sonars.append(sonar(pi,   26, 16))



    def set_wheel_drive_rates( self, wheels, speeds):
        if len(wheels) != len(speeds):
            raise ValueError('Number of wheels and speeds is not equal')

        for index, speed in enumerate(speeds):
            # limit the speed to [-99, 99]
            speed = functions.clamp(speed, -99, 99)

            # set the speed of a wheel
            if speed < 0:
                wheels[i].backward(-speed)
            elif speed > 0:
                wheels[i].forward(speed)

    # Transform a unicycle model to a differential drive model
    def uni_to_diff( self, v, omega ):
        # v = translational velocity (m/s)
        # omega = angular velocity (rad/s)

        R = self.wheel_radius
        L = self.wheel_base_length

        v_l = ( (2.0 * v) - (omega*L) ) / (2.0 * self.wheel_radius)
        v_r = ( (2.0 * v) + (omega*L) ) / (2.0 * self.wheel_radius)

        return v_l, v_r

    def callback_encoder_leftwheel(self, way):
        self.wheels_ticks_left += way


    def callback_encoder_rightwheel(self, way):
        self.wheels_ticks_right += way

    # read the proximity sensors 
    def read_proximity_sensors(self):
        # trigger the sonar
        for sonar in self.sonars:
            sonar.trigger()

        time.sleep(0.03)

        # read the sonar results
        for index, sonar in enumerate(self.sonars): 
            self.proximity[index] = sonar.read()

        return self.proximity

    # stop turning of wheels
    def stop_wheels(self, wheels):
        for wheel in wheels:
            wheel.stop()


    # stop servos
    def servo_cleanup(self, servos):
        for servo in servos:
            servos.center()

        # wait for the servo to center
        time.sleep(1)

        for servo in servos:
            servos.stop()

    def decoder_cleanup(self, decoders):
        for decoder in decoders:
             decoder.cancel()

    def sonar_cleanup(self, sonars):
        for sonar in sonars:
            sonar.cancel()

    # stop and cleanup all motors and code
    def cleanup(self):
        self.stop_wheels(self.wheels)
        self.servo_cleanup(self.servos)
        self.decoder_cleanup(self.decoders)
        self.sonar_cleanup(self.sonars)
        GPIO.cleanup()
        pi.stop()


    # update the estimated position of the robot using it's wheel encoder readings
    def update_odometry( self ):
        R = self.wheel_radius
        N = float( self.wheel_encoder_ticks_per_revolution )
        
        # read the wheel encoder values
        ticks_left = self.wheels_ticks_left
        ticks_right = self.wheels_ticks_right
        
        # get the difference in ticks since the last iteration
        d_ticks_left = ticks_left - self.prev_ticks_left
        d_ticks_right = ticks_right - self.prev_ticks_right
        
        # estimate the wheel movements
        d_left_wheel = 2*pi*R*( d_ticks_left / N )
        d_right_wheel = 2*pi*R*( d_ticks_right / N )
        d_center = 0.5 * ( d_left_wheel + d_right_wheel )
        
        # calculate the new pose
        prev_x, prev_y, prev_theta = self.estimated_pose.scalar_unpack()
        new_x = prev_x + ( d_center * cos( prev_theta ) )
        new_y = prev_y + ( d_center * sin( prev_theta ) )
        new_theta = prev_theta + ( ( d_right_wheel - d_left_wheel ) / self.robot_wheel_base_length )
        
        # update the pose estimate with the new values
        self.estimated_pose.scalar_update( new_x, new_y, new_theta )
        
        # save the current tick count for the next iteration
        self.prev_ticks_left = ticks_left
        self.prev_ticks_right = ticks_right



###########################################
# Begin normal code
###########################################


Fedya = Robot()

# get sonar readings
proximity = Fedya.read_proximity_sensors()

# get wheel encoder ticks
Fedya.wheelTicks

# set wheel speed
#Fedya.set_wheel_drive_rates( Fedya.wheels, [v_l, v_r] )

# get servo positions
Fedya.verticalServo.position 
Fedya.verticalServo.minPos
Fedya.verticalServo.centerPosition
Fedya.verticalServo.maxPos
Fedya.horizontalServo.position 
Fedya.horizontalServo.minPos
Fedya.horizontalServo.centerPosition
Fedya.horizontalServo.maxPos

# set servo position
Fedya.verticalServo.setPosition(dt)
Fedya.horizontalServo.setPosition(dt)

# send commands to wheels
v = 0.5
omega = 0.1

v_l, v_r = Fedya.uni_to_diff( v, omega )
Fedya.set_wheel_drive_rates( Fedya.wheels, [v_l, v_r] )


