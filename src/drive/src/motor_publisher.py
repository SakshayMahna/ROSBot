#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32MultiArray

def publisher():
    pub = rospy.Publisher('command', Int32MultiArray, queue_size=10)
    rospy.init_node('motor_command', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        string_arr = raw_input().split(' ')
        int_arr = [int(num) for num in string_arr]

        rospy.loginfo(string_arr)
        print(string_arr)

        cmd = IntList()
        cmd.data = int_arr

        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInteruptException:
        pass
