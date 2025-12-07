#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

rospy.init_node('tf_turtle')

# приватный параметр ~turtle_tf_name, задаёт имя фрейма черепахи
turtlename = rospy.get_param('~turtle_tf_name')

def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform(
        (msg.x, msg.y, 0.0),
        quaternion_from_euler(0.0, 0.0, msg.theta),
        rospy.Time.now(),
        turtlename,
        "world"
    )

# ПОДПИСЫВАЕМСЯ НА ПРАВИЛЬНЫЙ ТОПИК!
rospy.Subscriber(f'/{turtlename}/pose', Pose, handle_turtle_pose)
rospy.spin()
