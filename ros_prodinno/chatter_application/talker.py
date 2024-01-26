#! /usr/bin/env python3

'''please note that this is an example of sycronus
 command we can create a service for asncronus chatting 
 but that is out of the scope for this event '''


import rospy
from std_msgs.msg import String


node_name = 'talker'
topic_name1 = 'chat_1'
topic_name2 = 'chat_2'

def callback(message):
    print(f"\n[Chatter][received]: {message.data}",end='\n-------------\n[Chatter][send]:')


def talker():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher(topic_name2,String,queue_size=10)
    rospy.Subscriber(topic_name1,String,callback)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node(node_name, anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1)
    #keep publishing until a Ctrl-C is pressed
    i=0
    while not rospy.is_shutdown():
        msg = input("\n[Chatter][send]: ")
        pub.publish(msg)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
