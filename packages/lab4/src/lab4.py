#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

def convert(value, unit):
    if unit == "meters":
        return value * 0.30478513
    elif unit == "smoots":
        return value * 0.17910555
    else:
        return value

def callback(data):
   value = data.data
   unit = rospy.get_param("units")
   result = convert(value, unit)
   pub = rospy.Publisher("units", Float32, queue_size=10)
   pub.publish(result)

def sub():
    rospy.init_node("subscriber")
    rospy.Subscriber("/lab1/total" , Float32, callback)

try:
    sub()
    rospy.spin()
except rospy.ROSInterruptException:
    pass

