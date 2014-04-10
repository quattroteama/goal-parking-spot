#!/usr/bin/env python
import rospy
import roslib
import tf
import sys
from std_msgs.msg import Float32



def server_side():
    carname = sys.argv[1]
    publisher_topic = carname + '/Park'
    pub = rospy.Publisher(publisher_topic, Float32)
    rospy.init_node('server_side')
    

    current_time = rospy.get_rostime();
    
    while not rospy.is_shutdown():
        command = input('To Park press 1, to Unpark press 0: ')
        rospy.loginfo(command)
        pub.publish(command)         
        rospy.sleep(5.0);

if __name__ == '__main__':
    try:
        server_side()
    except rospy.ROSInterruptException:
        pass

