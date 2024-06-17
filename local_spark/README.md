## Installation Apache Spark
Before using Spark, we need to prepare several requirements and first install Spark and carry out some configurations.

### Requirements
1. Java
2. Scala
3. Apache Spark

### Preparation
***Install Java Development Kit (JDK)***
```bash
sudo apt install default-jre
sudo apt install default-jdk
```
or
```bash
sudo apt install openjdk-11-jdk -y
```
***Install Scala Programming language***
You can get the download source at [Scala](https://www.scala-lang.org/download/) and several versions are available
```bash
sudo apt install git scala -y
```
***Install Apache Spark***
You can get the download source at [Apache Spark](https://spark.apache.org/downloads.html) and several versions are available
```bash
sudo wget https://dlcdn.apache.org/spark/<spark_version>/<spark_version>-bin-hadoop3.tgz
# extract the downloaded file
sudo tar xvf <spark_version>-bin-hadoop3.tgz
# Move Spark directory move the extracted Spark Directory
sudo mv <spark_version>-bin-hadoop3 /opt/spark
```

### Configurations
***.bashrc :*** Configure Hadoop environment variables in the bashrc file then add the following command to the file
```bash
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

### Usage
***Enable environment variables***
```bash
source ~/.bashrc
```
***Start Spark Shell***
```bash
spark-shell
```
alternatively, if you want to start the PySpark shell
```bash
pyspark
```
