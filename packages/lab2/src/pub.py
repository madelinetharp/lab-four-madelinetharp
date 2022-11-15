#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32


def pub():
    rospy.init_node("publisher")
    pub = rospy.Publisher("/lab1/delta" ,Float32, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rand = random.randint(0,99)
        pub.publish(rand)
        rate.sleep()

try:
    pub()
except rospy.ROSInterruptException:
    pass

