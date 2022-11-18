#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

#inside convert value there are rospy.loginfo which print the value
def convertValue(value, unit):
    if unit == "meters":
        #multiply by conversion factor
        return value * 0.3048
        rospy.loginfo("Value in meters: %s", value)
    elif unit == "smoots":
        #multiply by conversion factor
        return value * 0.1791
        rospy.loginfo("Value in smoots: %s", value)
    else:
        #return unchanged value, feet is assumed as default
        return value
        rospy.loginfo("Value in feet: %s", value)

#callback function takes value and unit and publishes it
def callback(data):
   value = data.data
   unit = rospy.get_param("units")
   result = convertValue(value, unit)
   pub = rospy.Publisher("units", Float32, queue_size=10)
   pub.publish(result)

#subscriber subscribes to /lab1/total
def sub():
    rospy.init_node("subscriber")
    rospy.Subscriber("/lab1/total" , Float32, callback)

try:
    sub()
    rospy.spin()
except rospy.ROSInterruptException:
    pass

