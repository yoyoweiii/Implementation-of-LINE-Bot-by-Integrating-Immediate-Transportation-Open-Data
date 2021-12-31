import requests
import MySQLdb
import xml.etree.cElementTree as ET

db=MySQLdb.connect(host="localhost",user="root",passwd="0000",db="data",charset="utf8")
c=db.cursor()

res=requests.get("http://e-traffic.taichung.gov.tw/taichungexportxml/roadlevel_value_People.ashx")
res.encoding='utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text,"lxml-xml")
#tag=soup.Info
#print(res.content)
root =ET.fromstring(res.content)
x=0
for row in soup.Infos:
   try:       
#        print(root[0][x].attrib.get('routeid'),root[0][x].attrib.get('level'),root[0][x].attrib.get('value'),root[0][x].attrib.get('datacollecttime'))
#        print(x)
        routeid=root[0][x].attrib.get('routeid')
        level=root[0][x].attrib.get('level')
        value=root[0][x].attrib.get('value')
        datacollecttime=root[0][x].attrib.get('datacollecttime')
        x=x+1
        sql="UPDATE data SET level='%s',value='%s',datacollecttime='%s'  WHERE routeid='%s'" % (level,value,datacollecttime,routeid)
        c.execute(sql)
        db.commit()
   except:
        c.close()
db.close()

