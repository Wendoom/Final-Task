#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\n%s", data.linear_acceleration)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('imu/data', Imu, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
