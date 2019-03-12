#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler



roll = pitch = yaw = 0.0

def get_rotation (msg):
    global roll, pitch, yaw
#    print msg.pose.pose.orientation
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    yaw_degrees = yaw * 180.0 / math.pi
    if( yaw_degrees < 0 ):
         yaw_degrees += 360.0
    print yaw_degrees

rospy.init_node('droneYaw')

sub = rospy.Subscriber ('/mavros/local_position/odom', Odometry, get_rotation)

r = rospy.Rate(1)
while not rospy.is_shutdown():    
    quat = quaternion_from_euler (roll, pitch,yaw)
    print quat
    r.sleep()
