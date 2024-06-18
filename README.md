# MapReduce using Hadoop, Apache Spark, and Python
This application is designed to analyze tweets for the presence of racist language. The primary goal is to identify and quantify tweets containing specific racist keywords over different years. This application leverages Hadoop for distributed storage, Apache Spark for processing, and Python for scripting and automation.

### Dataset
You can get sample data in the [reusable-data/](reusable-data) directory file, or if you want to modify the data yourself, you can use the source code in the ```collecting_data/``` directory file.

### Requirements
1. Python ^3.8.x
2. Hadoop (NameNode, DataNode, YARN)
3. Apache Spark (PySpark)

## Installation
I have explained the steps for installing Hadoop and Spark in the [hadoop_mapred/](hadoop_spark/README.md) file, you can immediately read and follow each step.

## Usage
***Make sure the mapper and reducer files have execute permission***
```bash
sudo chmod -x /home/hadoop/mapper.py
sudo chmod -x /home/hadoop/reducer.py
```
***Run Hadoop Cluster***
```bash
start-all.sh
```
***Prepare input data***\
Here we will use three ebooks from Project Gutenberg as an example, you can get them in the [reusable-data](reusable-data) file or you can download them on the following page: [pg20417](https://www.gutenberg.org/ebooks/20417.txt.utf-8) [pg4300](https://www.gutenberg.org/ebooks/4300.txt.utf-8) [pg5000](https://www.gutenberg.org/ebooks/5000.txt.utf-8)
***create a directory and copy the local instance data to HDFS***
```bash
# this is just an example of a path created in HDFS
hadoop dfs -mkdir -p /home/hadoop/gutenberg
# to see whether the directory we created already exists or not
hadoop dfs -ls /home/hadoop/
# move the input file to the file that has been created in Hadoop
hadoop dfs -copyFromLocal <file_path_local>/{pg20417.txt,pg5000.txt,pg4300.txt} /home/hadoop/gutenberg
```
***run MapReduce job***
```bash
hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-mapper ~/mapper.py\ # path to mapper
-reducer ~/reducer.py\ # path to reducer
-input /home/hadoop/gutenberg/*\ # path of the file that has been uploaded to HDFS
-output /home/hadoop/gutenberg-output # create and path of the output
