# Beyond_Binary
 
 <h1>Installation <h1>

 <h2>Ubuntu Image</h2>
 <a href="https://www.releases.ubuntu.com/focal/">Ubuntu 20.04 ISO download </a>

 <h2>Virtual Box</h2>
 <a href="https://www.virtualbox.org/wiki/Downloads">Oracle VM box download</a>
 
<h3>Download steps</h3>

 - in the Oracle VM Virtual Box Manager, click on the New option
 - enter the Name of the virtual box by your choice
 - select the ISO image of Ubuntu 20.04 downloaded before; it will appear in the options in the dropdown
 - click Next
 - set the username and password and other inputs then click Next
 - set the Memory to 4000MB and click Next
 - set the Virtual Disk size as 32 GB and click Next
 - click Finish and it will start the setup of Ubuntu in the virtual box

 <h2>ROS NOETIC INSTALLATION</h2>

<h3> setup your sources.list</h3>
 <pre><small><span class="anchor" id="Installation.2FUbuntu.2FSources.line-1-1"></span>sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" &gt; /etc/apt/sources.list.d/ros-latest.list'</small></pre>

 <h3>set up your keys</h3>
 <pre><span class="anchor" id="Installation.2FUbuntu.2FSources.line-1-2"></span>sudo apt install curl # if you haven't already installed curl
<span class="anchor" id="Installation.2FUbuntu.2FSources.line-2-1"></span>curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -</pre>

<h2>installation</h2>
<pre><span class="anchor" id="noetic.2FInstallation.2FDebianMetapackages.line-1-1"></span>sudo apt update</pre>

<pre><span class="anchor" id="noetic.2FInstallation.2FDebianMetapackages.line-1-3"></span>sudo apt install ros-noetic-desktop-full</pre>

<pre><span class="anchor" id="noetic.2FInstallation.2FDebianMetapackages.line-1-5"></span>sudo apt install ros-noetic-PACKAGE</pre>



<h2>environment setup</h2>

<pre><span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-1-1"></span>source /opt/ros/noetic/setup.bash</pre>

<p class="line862">If you have more than one ROS distribution installed, <tt class="backtick">~/.bashrc</tt> must only source the <tt class="backtick">setup.bash</tt> for the version you are currently using. </p>

<pre><span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-1-3"></span>echo "source /opt/ros/noetic/setup.bash" &gt;&gt; ~/.bashrc
<span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-2-1"></span>source ~/.bashrc</pre>

<pre><span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-1-4"></span>echo "source /opt/ros/noetic/setup.zsh" &gt;&gt; ~/.zshrc
<span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-2-2"></span>source ~/.zshrc</pre>

<pre><span class="anchor" id="line-1-2"></span>sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential</pre>

<pre><span class="anchor" id="line-1-4"></span>sudo rosdep init
<span class="anchor" id="line-2-1"></span>rosdep update</pre>

<pre><span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-1-4"></span>echo "source /opt/ros/noetic/setup.zsh" &gt;&gt; ~/.zshrc
<span class="anchor" id="noetic.2FInstallation.2FDebEnvironment.line-2-2"></span>source ~/.zshrc</pre>

<h2>dependencies</h2>
<pre><span class="anchor" id="line-1-2"></span>sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential</pre>

<pre><span class="anchor" id="line-1-3"></span>sudo apt install python3-rosdep</pre>

<pre><span class="anchor" id="line-1-4"></span>sudo rosdep init
<span class="anchor" id="line-2-1"></span>rosdep update</pre>




 <h2>Arduino IDE 1.8.19</h2>
 <a href="https://www.arduino.cc/en/software">Arduino IDE download</a>

 Installation steps
 - extract the files from the zip downloaded
- open terminal on the extracted folder and run <br>
 <code>./install.sh</code>
 - other wise open the extracted file arduino-1.8.19 and right click on arduino-builder and run


 <h2>VS code</h2>
 <a href="https://code.visualstudio.com/download">Visual Studion Code download</a>
 

 <h2>Python Libraries</h2>

- sklearn <br>
<a href="https://drive.google.com/drive/folders/1xrUdVRAyknLZV1iv8jDX5_n14wYF5OlM?usp=sharing">download from this drive link</a>

- pandas<br>
<a href="https://drive.google.com/drive/folders/1xrUdVRAyknLZV1iv8jDX5_n14wYF5OlM?usp=sharing">download from this drive link</a>

- seaborn<br>
    <code>pip install seaborn</code>

- openCV<br>
    <code>pip install opencv</code>

- cvzone<br>
    <code>pip install cvzone</code>

- tensorflow<br>
<a href="https://drive.google.com/drive/folders/1xrUdVRAyknLZV1iv8jDX5_n14wYF5OlM?usp=sharing">download from this drive link</a>

- plotly<br>
    <code>pip install plotly</code>

NOTE: in case your system does not have pip installed, <a href="https://pypi.org/project/pip/">click here</a> to download.

