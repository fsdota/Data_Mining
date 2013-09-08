from numpy import *
def loadData(fileName):
    file=open(fileName)
    firstLine=file.readline()
    cols=firstLine.strip().split(",")
    data={}
    for line in file.readlines():
        values=line.strip().split(",");
        name=values[0];
        data[name]={"name":name,"type":values[-1],"attrs":array([float(i) for i in values[1:-1]])}
    return cols,data
def dist(a,b):
    return sqrt(sum((a-b)**2))
def find(item,data,k):
    distances=[]
    for key in data:
        value=data[key]
        d=dist(item["attrs"],value["attrs"])
        distances.append((key,d))
    distances.sort(key=lambda x:x[1],reverse=True)
    distances=distances[0:k]
    typesCount={}
    print distances
    for i in distances:
        type=data[i[0]]["type"]
        typesCount[type]=typesCount.get(type,0)+1
    types=[(type,count) for type,count in typesCount.items()]
    types.sort(key=lambda x:x[1],reverse=True)
    print types
    
if __name__=="__main__":
    cols,data=loadData("data.csv")
    print cols
    print data
    print "begin to find"
    find({"name":"test","attrs":array([18,90])},data,3)
