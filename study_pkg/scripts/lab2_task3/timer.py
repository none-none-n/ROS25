#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("Timer: Received number: %d", msg.data)

if __name__ == '__main__':
    rospy.init_node('timer', anonymous=True)
    
    # Подписываемся на топик с четными числами
    rospy.Subscriber('even_numbers', Int32, callback, queue_size=10)
    
    rospy.loginfo("Timer node started. Waiting for even numbers...")
    rospy.spin()
