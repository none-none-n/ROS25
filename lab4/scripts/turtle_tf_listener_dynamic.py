#!/usr/bin/env python3
import rospy
import math
import tf
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener_dynamic')
    
    listener = tf.TransformListener()
    
    # Создаем вторую черепаху если нужно
    try:
        rospy.wait_for_service('spawn', timeout=5)
        spawner = rospy.ServiceProxy('spawn', Spawn)
        spawner(4.0, 2.0, 0.0, 'turtle2')
        rospy.loginfo("Turtle2 spawned")
    except rospy.ServiceException:
        rospy.loginfo("Turtle2 already exists or spawn service unavailable")
    
    turtle_vel = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
        try:
            # turtle2 следует за carrot (которая вращается вокруг turtle1)
            (trans, rot) = listener.lookupTransform('/turtle2', '/carrot', rospy.Time(0))
            
            # Вычисляем управление
            distance = math.sqrt(trans[0]**2 + trans[1]**2)
            angle = math.atan2(trans[1], trans[0])
            
            msg = Twist()
            msg.linear.x = 0.5 * distance
            msg.angular.z = 4.0 * angle
            
            turtle_vel.publish(msg)
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            # Ждем пока TF станет доступен
            pass
        
        rate.sleep()
