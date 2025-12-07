#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math

# Глобальные переменные
turtlename = None
start_time = None
last_pose = None

def handle_turtle_pose(msg):
    global last_pose
    last_pose = msg

if __name__ == "__main__":
    rospy.init_node('tf_turtle_with_carrot')

    # Получаем имя черепахи из параметра
    turtlename = rospy.get_param('~turtle_tf_name', 'turtle1')
    
    # Подписываемся на правильный топик
    rospy.Subscriber(f'/{turtlename}/pose', Pose, handle_turtle_pose)
    
    br = tf.TransformBroadcaster()
    start_time = rospy.Time.now()

    rospy.loginfo(f"TF broadcaster with carrot started for {turtlename}")
    
    rate = rospy.Rate(30.0)
    while not rospy.is_shutdown():
        if last_pose is not None:
            # world -> turtle1
            br.sendTransform(
                (last_pose.x, last_pose.y, 0.0),
                quaternion_from_euler(0.0, 0.0, last_pose.theta),
                rospy.Time.now(),
                turtlename,
                "world"
            )

            # вращающаяся морковка вокруг черепахи
            t = (rospy.Time.now() - start_time).to_sec()
            radius = 0.5
            omega = 0.5
            height = 0.0

            carrot_x = radius * math.cos(omega * t)
            carrot_y = radius * math.sin(omega * t)
            carrot_z = height

            # turtle1 -> carrot
            br.sendTransform(
                (carrot_x, carrot_y, carrot_z),
                quaternion_from_euler(0.0, 0.0, 0.0),
                rospy.Time.now(),
                "carrot",
                turtlename
            )

        rate.sleep()
