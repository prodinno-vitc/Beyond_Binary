# ROS node

<pre>
- roscore
- rosrun package_name talker
- rosrun turtlesim_node

- gedit ~/.bashrc

- rosrun package_name listener
- rosrun turtlesim 

- rqt_graph  // shows nodes active

</pre>

# catkin workspace

<pre>
- mkdir catkin_ws
- cd catkin_ws/
- ls
- mkdir src
- ls
- catkin_make   // inside workspace; not src folder
- cd
- source ~/catkin_ws/devel/setup.bash
- gedit ~/.bashrc
- add <i>source ~/catkin_ws/devel/setup.bash</i>after source (last line) and save it
- close the terminals
</pre>



# creating package 

<pre>
- cd catkin_ws/src/
- catkin_create_pkg pkg_name rospy roscpp std_msgs
- cd pkg_name/
- catkin_make
- rosrun pkg_name
- code .    // opens in VS code
</pre>


# file structure

- make app folder under src
- listener.py
- talker.py
    - talker class has <i>Publisher(topic_name, String, queue_size=10)</i> which creates a new publisher
- executable file needs to be made <i>chmod u +x file_path</i> in terminal
- turtle_kinematics.py //Publish to move and Subscribe to fetch
    - move() function has x and y which deal with position; velocity commands are sent by Twist() message 
    - based on forward and backward, message is set
    - Publish message (velocity)
    - in loop, publish velocity and print distance moved calculated 
    - movement is stopped when distance target is reached
    - move(speed, distance, backwards/forward)
    

# more commands

- <i>rostopic list</i> gives a list of ROS topics
- <i>rosrun rqt_graph rqt_graph </i>
- <i>rosnode list</i> gives a list of nodes 
- <i>rostopic info /turtle/cmd_vel</i>
- <i>rosmsg show geometry_msgs/Twist</i> (msg name) gives x, y, z of linear and angular domain; this is to import all the data types. 
- <i>rosmsg echo /turtle1/cmd_vel</i> shows message that was sent 
        


