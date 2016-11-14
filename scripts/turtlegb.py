#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist

def callback(data):
	global pub
	rospy.loginfo(" Linear : %s ,\n angular : %s\n" % (data.linear, data.angular))
	data = editData(data)
	pub.publish(data)

def editData(data):
	data.linear.y = data.linear.x
        data.linear.x = tmpsave
        data.linear.z = 6.0
	return data
		
def init():
	global pub
	rospy.init_node('listenerTurtleGB')
	pub = rospy.Publisher('cmd_GB', Twist, queue_size=1)
	rospy.Subscriber("turtle1/cmd_vel", Twist, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		init()
	except rospy.ROSInterruptException:
		pass
