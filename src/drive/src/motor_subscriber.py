#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
from scripts.motor_driver import MotorDriver

def callback(data):
    if(data.data[0] == 0):
        driver.forward(data.data[1])
    elif(data.data[0] == 1):
        driver.forward(data.data[1])

def listener():
    rospy.init_node('motor_receive', anonymous=True)
    rospy.Subscriber("command", Int32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    driver = MotorDriver(22, 17, 23, 24)
    listener()