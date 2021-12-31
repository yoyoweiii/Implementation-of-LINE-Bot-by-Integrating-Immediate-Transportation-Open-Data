import urllib
import os
import gzip
import MySQLdb
import xml.etree.ElementTree as ET
db=MySQLdb.connect(host="localhost",user="root",passwd="0000",db="highway",charset="utf8")
c=db.cursor()

encoding='utf-8'
path=r'/home/hpcuser/hdynamic_data.gz'
url='http://tisvcloud.freeway.gov.tw/roadlevel_value5.xml.gz'
urllib.urlretrieve(url,path)

g=gzip.GzipFile(mode="rb",fileobj=open('/home/hpcuser/hdynamic_data.gz','rb'))

open(r"/home/hpcuser/roadlevel_value5_1735","wb").write(g.read())

tree=ET.parse('/home/hpcuser/roadlevel_value5_1735')
root=tree.getroot()


x=0
for Info in root.iter('Info'):
     try:
            routeid=root[0][x].attrib.get('routeid')
            level=root[0][x].attrib.get('level')
            value=root[0][x].attrib.get('value')
            traveltime=root[0][x].attrib.get('traveltime')
            datacollecttime=root[0][x].attrib.get('datacollecttime')

            x=x+1

            sql="UPDATE highway SET level='%s',value='%s',traveltime='%s',datacollecttime='%s' WHERE routeid='%s'" %(level,value,traveltime,datacollecttime,routeid)

            c.execute(sql)
            db.commit()
     except:

            c.close()
db.close()

