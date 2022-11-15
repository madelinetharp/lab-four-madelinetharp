#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

def convert(data):
    rospy.loginfo("Data recieved: %s", data.data)


def sub():
    rospy.init_node("subscriber")
    rospy.Subscriber("/lab1/total" , Float32, convert)

try:
    sub()
    rospy.spin()
except rospy.ROSInterruptException:
    pass

