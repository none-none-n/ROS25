#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

if __name__ == '__main__':
    rospy.init_node('uc_pub', anonymous=True)
    
    # Публикуем в два топика
    pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
    overflow_pub = rospy.Publisher('overflow_signal', String, queue_size=10)
    
    rate = rospy.Rate(10)  # 10 Hz
    counter = 0
    
    rospy.loginfo("UC Publisher node started")
    
    while not rospy.is_shutdown():
        # Публикуем ВСЕ четные числа
        pub.publish(counter)
        rospy.loginfo("Published even number: %d", counter)
        
        # Проверяем переполнение
        if counter >= 100:
            overflow_msg = "Counter overflow at value: %d" % counter
            overflow_pub.publish(overflow_msg)
            rospy.logwarn(overflow_msg)
            counter = 0
        else:
            counter += 2
        
        rate.sleep()
