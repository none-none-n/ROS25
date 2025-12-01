#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    rospy.loginfo("Overflow Timer: OVERFLOW DETECTED: %s", msg.data)

if __name__ == '__main__':
    rospy.init_node('overflow_timer', anonymous=True)
    
    # Подписываемся на топик с сообщениями о переполнении
    rospy.Subscriber('overflow_signal', String, overflow_callback, queue_size=10)
    
    rospy.loginfo("Overflow Timer node started. Waiting for overflow signals...")
    rospy.spin()
