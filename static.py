import requests
import MySQLdb
import xml.etree.cElementTree as ET
db=MySQLdb.connect(host="localhost",user="root",passwd="0000",db="data",charset="utf8")
c=db.cursor()
#c.execute("SET names utf8")
res=requests.get("http://e-traffic.taichung.gov.tw/taichungexportxml/roadlevel_info_People.ashx")
res.encoding='utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text,"lxml-xml")

root =ET.fromstring(res.content)
x=0
for row in soup.Infos:
     try:
         routeid=root[0][x].attrib.get('routeid') #.encoding('utf-8')
         tokm=root[0][x].attrib.get('tokm') #.encoding('utf-8')
         fromkm=root[0][x].attrib.get('fromkm') #.encoding('utf-8')
         roadsection=root[0][x].attrib.get('roadsection') #.encoding('utf-8')
         col=tokm
         col2=fromkm
         strlist = col.split(',')
         strlist2 = col2.split(',')
         to_lng=strlist[0]
         to_lat=strlist[1]
         from_lng=strlist2[0]
         from_lat=strlist2[1]
#         print(col,col2,to_lng,to_lat,from_lng,from_lat)
         sql = "UPDATE data SET to_lat='%s', to_lng='%s',from_lat='%s',from_lng='%s' WHERE tokm='%s'" % (to_lat,to_lng,from_lat,from_lng,col)
         x=x+1         
#         print(sql)
         c.execute(sql)
         db.commit()
     except:
        
         c.close()
db.close()

