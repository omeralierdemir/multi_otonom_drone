#!/usr/bin/env python

import rospy 
import math
import time
#from geometry_msgs.msg import Twist
from mavros_msgs.msg import PositionTarget
from mavros_msgs.srv import *
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler

msg = PositionTarget()

lastErrorX = 0
def call_back2 (msg2):
    
    global roll 
    global pitch 
    global yaw 
    global yaw_degrees 
    
   
#    print msg.pose.pose.orientation
    orientation_q = msg2.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    yaw_degrees = yaw * 180.0 / math.pi
    if( yaw_degrees < 0 ):
         yaw_degrees += 360.0
    

def call_back(data):
	
	global lastErrorX
	global msg
	
	

	

	XY = data.data
	XY = XY.split(" ")

	x= float(XY[0])
	y= float(XY[1])

	errorX = 300 - x # sebebi artis ters yonlu

	kp = 0.006
	kd = 0.009

	turevX = (-1)*(errorX-lastErrorX)
	P_cont = errorX*kp 
	D_cont = turevX*kd
	donmeEksen = (yaw_degrees)*(6.28/360) + P_cont
	
	
	if donmeEksen < 0:
	    donmeEksen = 6.28 + donmeEksen

	    
	msg.yaw = donmeEksen

	print "sonuc:" , donmeEksen, "error:",errorX,"P_cont:",P_cont,"yawIste:",(yaw_degrees)*(6.28/360),"D_cont:",D_cont
	
	lastErrorX = errorX



if  __name__ == '__main__':

	
		
	
	try:
		rospy.init_node('eksen',anonymous=True)
		
		

		global msg
		
		pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget,queue_size=10)
		rospy.Subscriber('/mavros/local_position/odom', Odometry, call_back2)
		rospy.Subscriber('konum', String, call_back) 

        
        
        
        
		msg.header.stamp = rospy.Time.now()
		msg.header.frame_id= "world"
		msg.coordinate_frame = 8
		msg.type_mask=2503

		msg.velocity.x = 0.0
		msg.velocity.y = 0.0
		msg.velocity.z = 0.0
		msg.yaw = 0.0


		while not rospy.is_shutdown():

			pub.publish(msg)

			
		
		
		

	except rospy.ROSInterruptException:
		pass

