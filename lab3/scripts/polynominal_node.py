#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

a = b = c = None

def a_cb(msg):
    global a
    a = msg.data

def b_cb(msg):
    global b
    b = msg.data

def c_cb(msg):
    global c
    c = msg.data

if __name__ == "__main__":
    rospy.init_node("polynominal")

    rospy.Subscriber("input/a", Float64, a_cb)
    rospy.Subscriber("input/b", Float64, b_cb)
    rospy.Subscriber("input/c", Float64, c_cb)

    pub_a = rospy.Publisher("poly/a", Float64, queue_size=10)
    pub_b = rospy.Publisher("poly/b", Float64, queue_size=10)
    pub_c = rospy.Publisher("poly/c", Float64, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if a is not None and b is not None and c is not None:
            pub_a.publish(Float64(a))        # степень 1
            pub_b.publish(Float64(b**2))     # степень 2
            pub_c.publish(Float64(c**3))     # степень 3
        rate.sleep()
