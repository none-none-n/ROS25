#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

a1 = b2 = c3 = None

def a1_cb(msg):
    global a1
    a1 = msg.data

def b2_cb(msg):
    global b2
    b2 = msg.data

def c3_cb(msg):
    global c3
    c3 = msg.data

if __name__ == "__main__":
    rospy.init_node("summing")

    rospy.Subscriber("poly/a", Float64, a1_cb)
    rospy.Subscriber("poly/b", Float64, b2_cb)
    rospy.Subscriber("poly/c", Float64, c3_cb)

    sum_pub = rospy.Publisher("result", Float64, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if a1 is not None and b2 is not None and c3 is not None:
            s = a1 + b2 + c3
            sum_pub.publish(Float64(s))
        rate.sleep()
