from hdfs.client import Client
client=Client("http://192.168.1.119:50070")
client.list("/data")