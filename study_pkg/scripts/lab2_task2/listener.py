#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32  # Изменили String на Int32!

def callback(msg):
    rospy.loginfo("Received number: %d", msg.data)  # Выводим число

rospy.init_node('listener')
rospy.Subscriber('even_numbers', Int32, callback, queue_size=10)  # Подписываемся на even_numbers
rospy.loginfo("Number listener started. Waiting for even numbers...")
rospy.spin()
