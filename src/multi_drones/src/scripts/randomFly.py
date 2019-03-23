#!/usr/bin/env python

import rospy 
import math
import time
import random
#from geometry_msgs.msg import Twist
from mavros_msgs.msg import PositionTarget
from mavros_msgs.srv import *
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler

msg = PositionTarget()


def randomFly():
    rate = rospy.Rate(1) # 1000hz
    xPos = round(random.uniform(-10.0, 11.0),2)
    yPos = round(random.uniform(-10.0, 11.0),2)
    zPos = round(random.uniform(0.0, 11.0), 2)
    
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id= "world"
    msg.coordinate_frame = 8
    msg.type_mask=1984

    msg.position.x = xPos
    msg.position.y = yPos
    msg.position.z = zPos
    
    msg.velocity.x = 1.0
    msg.velocity.y = 1.0
    msg.velocity.z = 1.0
    msg.yaw = 0.0
    yaw_rate=1
	
	
    while not rospy.is_shutdown():
        xPos = round(random.uniform(-10.0, 11.0),2)
        yPos = round(random.uniform(-10.0, 11.0),2)
        zPos = round(random.uniform(0.0, 11.0), 2)
        msg.position.x = xPos
        msg.position.y = yPos
        msg.position.z = zPos
        
      
        pub.publish(msg)
        rate.sleep()
        print(xPos,yPos,zPos)


    
    
    
if  __name__ == '__main__':

    try:
	    rospy.init_node('eksen',anonymous=True)
	
	    
	    pub = rospy.Publisher('/uav1/mavros/setpoint_raw/local', PositionTarget,queue_size=10)
	    randomFly()
        

    except rospy.ROSInterruptException:
	    pass

