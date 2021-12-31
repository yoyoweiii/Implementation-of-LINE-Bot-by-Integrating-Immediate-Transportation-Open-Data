import urllib
import os
import gzip
import MySQLdb
import xml.etree.ElementTree as ET
db=MySQLdb.connect(host="localhost",user="root",passwd="0000",db="highway",charset="utf8")
c=db.cursor()

encoding='utf-8'
path=r'/home/hpcuser/test_data.gz'
url='http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
urllib.urlretrieve(url,path)

g=gzip.GzipFile(mode="rb",fileobj=open('/home/hpcuser/test_data.gz','rb'))

open(r"/home/hpcuser/roadlevel_info_0000","wb").write(g.read())

tree=ET.parse('/home/hpcuser/roadlevel_info_0000')
root=tree.getroot()

#print (file.text)
x=0
for Info in root.iter('Info'):
     try:          
           routeid=root[0][x].attrib.get('routeid')
           sourceid=root[0][x].attrib.get('sourceid')
           roadsection=root[0][x].attrib.get('roadsection')
           locationpath=root[0][x].attrib.get('locationpath')
           startlocationpoint=root[0][x].attrib.get('startlocationpoint')
           endlocationpoint=root[0][x].attrib.get('endlocationpoint')
           roadtype=root[0][x].attrib.get('roadtype')
           fromkm=root[0][x].attrib.get('fromkm')
           tokm=root[0][x].attrib.get('tokm')
           speedlimit=root[0][x].attrib.get('speedlimit')
#           print routeid,sourceid,roadsection,locationpath,startlocationpoint,endlocationpoint,roadtype,fromkm,tokm,speedlimit
           x=x+1

           sql = "INSERT INTO highway (routeid,sourceid,roadsection,locationpath,startlocationpoint,endlocationpoint,roadtype,fromkm,tokm,speedlimit) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (routeid,sourceid,roadsection,locationpath,startlocationpoint,endlocationpoint,roadtype,fromkm,tokm,speedlimit,)

 #          print(sql)
           c.execute(sql)
           db.commit()
     except:
         
           c.close()
db.close()

