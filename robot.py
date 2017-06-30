

# Description:
# Run:
# sudo pigpiod
# sudo python robot.py

import time
import pigpio
import RPi.GPIO as GPIO


from handy_stuff.functions.functions import * 
import motors.servos.servoWirPWM as servo_controller 
import motors.wheels.sn75SoftwarePwm as wheels_controller
import motors.wheels.pigpio_encoder as wheel_encoder_controller
import proximity_sensors.sonar.srte as sonar_controller



class Robot:

    
    def __init__(self):

        #self.estimated_pose = None
        #self.estimated_pose.scalar_update( 0, 0, 0 )

        # setup wheels
        self.wheel_radius = 4.5
        self.wheel_base_length = -1
        self.wheels = wheels_controller.initialize_default_motors()
        self.leftWheel = self.wheels[0]
        self.rightWheel = self.wheels[1]

        # setup servos
        # Vertical servo, 55 is down, 120 is up
        # horizontal servo, 30 is left
        self.servos = servo_controller.initialize_default_servos()
        self.verticalServo = self.servos[0]
        self.horizontalServo = self.servos[1]
        
        # Turn servos of during debugging to save battery
        self.verticalServo.stop()
        self.horizontalServo.stop()        

        # start pigpio
        self.pi = pigpio.pi()
        if not self.pi.connected:
            exit()
        
        # Setup wheel encoders [left, right]
        self.wheel_encoder_ticks_per_revolution = 360
        self.wheel_encoders = wheel_encoder_controller.initialize_default_encoders(self.pi)
        self.wheels_ticks_left = 0
        self.wheels_ticks_right = 0
        self.prev_ticks_left = 0
        self.prev_ticks_right = 0

        # setup sonars
        # [Head sonar, right sonar, left sonar]
        self.sonars = sonar_controller.initialize_default_sonars(self.pi)
        self.proximity = [999.9, 999.9, 999.9]


    # Fetch the current tick count of the wheel encoders and save it in the robot object
    def update_wheel_encoder_values(self):
        self.wheels_ticks_left = wheel_encoder_controller.wheels_ticks_left
        self.wheels_ticks_right = wheel_encoder_controller.wheels_ticks_right

    # stop and cleanup all motors and code
    def cleanup(self):
        print "Cleaning up"
        wheels_controller.stop_wheels(self.wheels)
        servo_controller.cleanup_servos(self.servos)
        wheel_encoder_controller.cleanup_wheel_encoders(self.wheel_encoders)
        sonar_controller.cleanup_sonars(self.sonars)
        GPIO.cleanup()
        self.pi.stop()


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


print "Setting up robot"
Fedya = Robot()

# Execute some tests
#sonar_controller.test_sonars_external(Fedya.sonars)

# skipped to not damage robot
#servo_controller.test_servos_external(Fedya.servos)

wheels_controller.test_wheels_external(Fedya.wheels)


Fedya.update_wheel_encoder_values()
print "Encoder values in robot.py: %d en %d" % (Fedya.wheels_ticks_left, Fedya.wheels_ticks_right)

wheel_encoder_controller.test_encoders_external(Fedya.pi, Fedya.wheel_encoders)

Fedya.update_wheel_encoder_values()
print "Encoder values in robot.py: %d en %d" % (Fedya.wheels_ticks_left, Fedya.wheels_ticks_right)


# get sonar readings
# proximity = sonar_controller.read_proximity_sensors(Fedya.sonars)

# get wheel encoder ticks
#Fedya.wheels_ticks_left
#Fedya.wheels_ticks_right

# set wheel speed
#wheels_controller.set_wheel_drive_rates( Fedya.wheels, [80, 80] )
#time.sleep(2.0)
#wheels_controller.stop_wheels( Fedya.wheels )

#print "Left: %d Right: %d" % (Fedya.wheels_ticks_left, Fedya.wheels_ticks_right)

# get servo positions
#Fedya.verticalServo.position 
#Fedya.verticalServo.minPos
#Fedya.verticalServo.centerPosition
#Fedya.verticalServo.maxPos
#Fedya.horizontalServo.position 
#Fedya.horizontalServo.minPos
#Fedya.horizontalServo.centerPosition
#Fedya.horizontalServo.maxPos

# set servo position
#Fedya.verticalServo.setPosition(dt)
#Fedya.horizontalServo.setPosition(dt)

# send commands to wheels
# v = 0.5
# omega = 0.1

#v_l, v_r = Fedya.uni_to_diff( v, omega )
#Fedya.set_wheel_drive_rates( Fedya.wheels, [v_l, v_r] )


Fedya.cleanup()
