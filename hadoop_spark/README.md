## Installation Hadoop
Before using Hadoop, we need to prepare several requirements and first install Hadoop and carry out some configurations.

### Requirements
1. Java
2. OpenSSH
3. Apache Hadoop

### Preparation
***Installing Java***
```bash
sudo apt install default-jre
sudo apt install default-jdk
```
or
```bash
sudo apt install openjdk-11-jdk -y
```
***Install OpenSSH server and client***
```bash
sudo apt install openssh-server openssh-client -y
```
***Generate public and private key***
```bash
ssh-keygen -t rsa
# add generate public key from id_rsa.pub to authorized_keys
sudo cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# change the permissions of the authorized_keys file
sudo chmod 640 ~/.ssh/authorized_keys
```
***Install Apache Hadoop***\
You can get the download source at [Apache Hadoop](https://hadoop.apache.org/) and several versions are available
```bash
wget https://dlcdn.apache.org/hadoop/common/<hadoop_version>/<hadoop_version>.tar.gz
# extract the downloaded file
tar -xvzf <hadoop_version>.tar.gz
# variable configuration for Hadoop settings, check the location of the variable "JAVA_HOME"
dirname $(dirname $(readlink -f $(which java)))
```

### Configurations
***.bashrc :*** Configure Hadoop environment variables in the bashrc file then add the following command to the file
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:/usr/lib/jvm/java-11-openjdk-amd64/bin/
export HADOOP_HOME=~/<hadoop_version>/
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar
export HADOOP_LOG_DIR=$HADOOP_HOME/logs
export PDSH_RCMD_TYPE=ssh
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```
***hadoop-env.sh :*** add the path according to the Java installation location on the system
```sh
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```
***core-site.xml :*** add the following configuration to change the temporary directory value and add the HDFS URL
```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
  <property>
    <name>hadoop.proxyuser.dataflair.groups</name>
    <value>*</value>
  </property>
  <property>
    <name>hadoop.proxyuser.dataflair.hosts</name>
    <value>*</value>
  </property>
  <property>
    <name>hadoop.proxyuser.server.hosts</name>
    <value>*</value>
  </property>
  <property>
    <name>hadoop.proxyuser.server.groups</name>
    <value>*</value>
  </property>
</configuration>
```
***hdfs-site.xml :*** add configuration files and customize the NameNode and DataNode directories
```xml
<configuration>
  <property>
    <name>dfs.name.dir</name>
    <value>file:///home/hadoop/pseudo/dfs/name</value>
  </property>
  <property>
    <name>dfs.data.dir</name>
    <value>file:///home/hadoop/pseudo/dfs/data</value>
  </property>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
```
***mapred-site.xml :*** add configuration to change the default value of MapReduce framework name to yarn
```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapreduce.application.classpath</name>
    <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
  </property>
</configuration>
```
***yarn-site.xml :*** Add the following configuration to the file
```xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.env-whitelist</name>
    <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREP END_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
  </property>
</configuration>
```

### Usage
***Enable environment variables***
```bash
source ~/.bashrc
```
***Format HDFS NameNode***
```bash
ssh localhost 
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa 
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
chmod 0600 ~/.ssh/authorized_keys 
<hadoop_version>/bin/hdfs namenode -format
```
***Start Hadoop Cluster***
```bash
start-dfs.sh
start-yarn.sh
jps
```
or
```bash
start-all.sh
jps
```
***Access Hadoop UI from browser***
- The default port number http://localhost:9870/ will access the Hadoop NameNode UI
- The default port http://localhost:9864/ is used to access Individual DataNodes
- YARN Resource Manager can be accessed on port http://localhost:8088/
