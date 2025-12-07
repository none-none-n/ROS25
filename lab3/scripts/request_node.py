#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import Float64

result_value = None

def result_cb(msg):
    global result_value
    result_value = msg.data

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: request_node.py a b c")
        sys.exit(1)

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    rospy.init_node("request", anonymous=True)

    pub_a = rospy.Publisher("input/a", Float64, queue_size=10, latch=True)
    pub_b = rospy.Publisher("input/b", Float64, queue_size=10, latch=True)
    pub_c = rospy.Publisher("input/c", Float64, queue_size=10, latch=True)

    sub_res = rospy.Subscriber("result", Float64, result_cb)

    # подождём, пока поднимутся подписчики/паблишеры
    rospy.sleep(0.5)

    pub_a.publish(Float64(a))
    pub_b.publish(Float64(b))
    pub_c.publish(Float64(c))

    rospy.loginfo("Sent: a=%s, b=%s, c=%s", a, b, c)

    timeout = rospy.Time.now() + rospy.Duration(5.0)
    while not rospy.is_shutdown() and result_value is None and rospy.Time.now() < timeout:
        rospy.sleep(0.1)

    if result_value is not None:
        rospy.loginfo("Result = %s", result_value)
        print("Result =", result_value)
    else:
        rospy.logwarn("No result received")
