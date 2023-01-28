import requests

class MyQueue:
    
    def __init__(self,url:str):
        self.url = url
    def createTopic(self,topicName:str):
        try:
            
            res = requests.post(self.url+"/topics",{
                "name":topicName
            })
            if(res.json().get("status")=="success"):
                return self.Topic(self,topicName)
            else:
                return -1

        except Exception as e:
            return -1

    def get_all_topics(self):
        try:
            res = requests.get(self.url+"/topics")
            if(res.json().get("status")=="Success"):
                return res.json().get("topic_string")
            else:
                return -1
        except Exception as e:
            return -1


    def createProducer(self,topicNames:list(str)):
        try:
            ids = {}
            for topicName in topicNames:

                res = requests.post(
                    self.url+"/producer/register",
                    {
                        "topic":topicName
                    })
                if(res.json().get("status")!="Success"):
                    return res.json().get("message")
                else:
                    pid = res.json().get("producer_id")
                    ids[topicName] = pid
            return self.Producer(self,ids)                

        except Exception as e:
            return -1

    def createConsumer(self,topicNames:list(str)):
        try:
            ids = {}
            for topicName in topicNames:

                res = requests.post(
                    self.url+"/consumer/register",
                    {
                        "topic":topicName
                    })
                if(res.json().get("status")!="Success"):
                    return res.json().get("message")
                else:
                    cid = res.json().get("consumer_id")
                    ids[topicName] = cid
            return self.Consumer(self,ids)                

        except Exception as e:
            return -1

    class Topic:
        def __init__(self,outer,topicName:str):
            self.topicName = topicName
            self.outer = outer

    class Producer:

        def __init__(self,outer,pids:dict):
            #self.topicName = topicName
            self.pids = pids
            self.outer = outer

        def enqueue(self,msg:str,topicName:str):
            if(topicName not in self.pids.keys()):
                return "Error: Topic not registered"
            try:
                id = self.pids[topicName]
                res = requests.post(
                    self.outer.url+"/producer/produce",
                    {
                        "topic":topicName,
                        "producer_id":id,
                        "message":msg
                    }
                )
                if(res.json().get("status")=="Success"):
                    return 0
                else:
                    return res.json.get("message")
            except Exception as e:
                return -1

    class Consumer:

        def __init__(self,outer,cids:dict):
            #self.topicName = topicName
            self.cids = cids
            self.outer = outer

        def dequeue(self,topicName:str):
            if(topicName not in self.cids.keys()):
                return "Error: Topic not registered"
            try:
                id = self.cids[topicName]
                res = requests.post(
                    self.outer.url+"/consumer/consume",
                    {
                        "topic":topicName,
                        "consumer_id":id
                    }
                )
                if(res.json().get("status")=="Success"):
                    return 0
                else:
                    return res.json.get("message")
            except Exception as e:
                return -1

        def getSize(self,topicName):
            if(topicName not in self.cids.keys()):
                return "Error: Topic not registered"
            try:
                res = requests.get(
                    self.outer.url+"/size",
                    {
                        "topic":topicName,
                        "consumer_id":self.cids[topicName]
                    }
                )
                if(res.json().get("status")=="Success"):
                    return int(res.json().get("size"))
                else:
                    return str(res.json().get("message"))
                
            except Exception as e:
                return -1


