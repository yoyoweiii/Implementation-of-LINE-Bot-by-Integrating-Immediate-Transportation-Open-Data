#vim: set filecoding:utf-8
import requests
import re
import random
import MySQLdb
import time
from flask import Flask, request, abort
encoding='utf8'

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
line_bot_api = LineBotApi('xC9zGfkF1b7X/OzZbJ0K/KMm8eUiteN228ueV3qM6rzLNzF7p+Vqu3jt3S7/i+lhuSZdwWD/T4xLGQNnAx2V+snfnzoURXrZCLcQpGZ02XH9mmFWxOrb8EMmbEk6OxelHkiBNeDv49r+kYDscnLiqgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('01f4b53c8733e2c66005b99c7266c290')
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info(" Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 200

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    print("event.source.userId:", event.source.user_id)
    if event.message.text == "Highway":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/vMKfsEo.jpg', text='起點', title='北北基', actions=[
                PostbackTemplateAction(label='台北市',data='2&begin', text='start from 台北市' ),
                PostbackTemplateAction(label='新北市',data='3&begin', text='start from 新北市' ),
                PostbackTemplateAction(label='基隆市',data='1&begin', text='start from 基隆市' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/vFZNJPn.jpg', text='起點', title='桃竹苗', actions=[
                PostbackTemplateAction(label='桃園市',data='4&begin', text='start from 桃園市' ),
                PostbackTemplateAction(label='新竹市',data='5&begin', text='start from 新竹市' ),
                PostbackTemplateAction(label='苗栗縣',data='6&begin', text='start from 苗栗縣' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/VPwzRAS.jpg', text='起點', title='中彰投', actions=[
                PostbackTemplateAction(label='台中市',data='7&begin', text='start from 台中市' ),
                PostbackTemplateAction(label='彰化縣',data='8&begin', text='start from 彰化縣' ),
                PostbackTemplateAction(label='南投縣',data='9&begin', text='start from 南投縣' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/5cz9Z6N.jpg',text='起點', title='雲嘉南', actions=[
                PostbackTemplateAction(label='雲林縣',data='10&begin', text='start from 雲林縣' ),
                PostbackTemplateAction(label='嘉義縣',data='11&begin', text='start from 嘉義縣' ),
                PostbackTemplateAction(label='台南市',data='12&begin', text='start from 台南市' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/eHpkqbC.jpg',text='起點', title='南部區域', actions=[
                PostbackTemplateAction(label='高雄縣', data='13&begin', text='start from 高雄縣' ),
                PostbackTemplateAction(label='屏東縣', data='14&begin', text='start from 屏東縣' ),       
                PostbackTemplateAction(label='台東縣', data='15&begin', text='別開玩笑了 東部？根本不會塞車好嗎～')
            ])
#            CarouselColumn(text='起點', title='東部地區', actions=[
#                PostbackTemplateAction(
#                    label='宜蘭縣', data='宜蘭縣', text='宜蘭縣'),  
#                PostbackTemplateAction(label='花蓮縣', data='花蓮縣', text='花蓮縣'),
#                PostbackTemplateAction(label='台東縣', data='台東縣', text='台東縣')
#            ])
        ])     
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#-----------------------------------------------------------------         
	imagemap_message = ImagemapSendMessage(
   	    base_url='https://i.imgur.com/MOSbhaD.jpg',
    	    alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='http://120.109.150.136/map.php',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='map',
            	    area=ImagemapArea(
                	x=520, y=0, width=520, height=1040
           	    )
                )  
            ]
        )
#	line_bot_api.reply_message(event.reply_token, imagemap_message)
	message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Are you sure?',
                actions=[
                    PostbackTemplateAction(
                        label='Single',
                        text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='Not',
                        text='message text'
                    )
                ]
            )
        )
        return 0
    if 'start from' in event.message.text:
#	print(event.message.text)
	carousel_template = CarouselTemplate(columns=[
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/vMKfsEo.jpg',text='終點', title='北北基', actions=[
                PostbackTemplateAction(label='台北市', data='2&end'),
                PostbackTemplateAction(label='新北市', data='3&end'),
                PostbackTemplateAction(label='基隆市', data='1&end')
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/8rA2jhq.jpg',text='終點', title='桃竹苗', actions=[
                PostbackTemplateAction(label='桃園市', data='4&end'),
                PostbackTemplateAction(label='新竹市', data='5&end'),
                PostbackTemplateAction(label='苗栗縣', data='6&end')
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/tGuUTcM.jpg',text='終點', title='中彰投', actions=[
                PostbackTemplateAction(label='台中市', data='7&end'),
                PostbackTemplateAction(label='彰化縣', data='8&end'),
                PostbackTemplateAction(label='南投縣', data='9&end')
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/5cz9Z6N.jpg',text='終點', title='雲嘉南', actions=[
                PostbackTemplateAction(label='雲林縣', data='10&end'),
                PostbackTemplateAction(label='嘉義縣', data='11&end'),
                PostbackTemplateAction(label='台南市', data='12&end')
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/eOueVe8.jpg',text='終點', title='南部區域', actions=[
                PostbackTemplateAction(label='高雄縣', data='13&end'),
                PostbackTemplateAction(label='屏東縣', data='14&end'),
                PostbackTemplateAction(label='台東縣', data='15&end', text='別開玩笑了 東部？根本不會塞車好嗎～')
            ])
	])
 	template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#        line_bot_api.push_message(
#            'Ua4ac720a3d0f48e77dda9d7c912cb5ad',TextSendMessage(text='Hi'))
#        return 0
    if event.message.text == "Taichung City":
       	line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://i.imgur.com/bnBXU2v.png',
            preview_image_url='https://i.imgur.com/bnBXU2v.png'
            )
        )
	line_bot_api.push_message(
            event.source.user_id,
            ImageSendMessage(
            original_content_url='https://i.imgur.com/mdpIlXT.png',
            preview_image_url='https://i.imgur.com/mdpIlXT.png'
            )
        )
	line_bot_api.push_message(
            event.source.user_id,
            ImageSendMessage(
            original_content_url='https://i.imgur.com/LGVY72G.png',
            preview_image_url='https://i.imgur.com/LGVY72G.png'
            )
        )
	line_bot_api.push_message(event.source.user_id,
            TextSendMessage(text='請按照上面教學操作，傳送位置資訊'))
    	return 0
    if event.message.text == "Camera":
        buttons_template = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='Select service',
                text='Select service',
                actions=[
                    PostbackTemplateAction(
                        label='北上', text='北上',
                        data='camera&north'
                    ),
                    PostbackTemplateAction(
                        label='南下', text='南下',
                        data='camera&south'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text == "test" or event.message.text == "Test":
        buttons_template = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='Select service',
                text='Select service',
                actions=[
                    MessageTemplateAction(
                        label='高速公路',
                        text='highway'
                    ),
                    MessageTemplateAction(
                        label='台中市',
                        text='Taichung City'
                    )
                ]
            )
        )	
        line_bot_api.reply_message(event.reply_token, buttons_template)
    	return 0
    
    sticker = StickerSendMessage(
                package_id='1',
                sticker_id='1'
        )
    line_bot_api.reply_message(event.reply_token, sticker)
    return 0
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
        db = MySQLdb.connect(host="localhost", user="root", passwd="0000", db="data", charset="utf8")
        content=''
        cursor = db.cursor()
        cursor.execute("SELECT * FROM data")
        results = cursor.fetchall()
        a=0
        for record in results:
             col0 = record[0]
             col1 = record[1]
             col2 = record[2]
             col3 = record[3]
             col4 = record[4]
             col5 = record[5]
             strlist = col2.split(',')
             longitude = float(strlist[0])
             latitude = float(strlist[1])
             long_distance = abs(event.message.longitude - longitude)
             lat_distance = abs(event.message.latitude - latitude)
             if(long_distance<0.015 and lat_distance<0.015 and a<9):
                 print "%s" % (col2)
                 if int(col4) < 4 and col4 > 1 :
                   degree='有一些車輛'
                   a=a+1
                 elif int(col4) > 4 :
                   degree='路很塞'
                   a=a+1
                 content = content + col1 + u", 車速:" + col5 + u", " + degree + u"\n\n"
        if a == 0:
            content = '您附近1.5公里內並無塞車路段'
        db.close()
#        print "%s" % (content)
        line_bot_api.reply_message(
                     event.reply_token,TextSendMessage(text=content)
        )
@handler.add(PostbackEvent)
def handle_postback(event):
    print("userId:", event.source.user_id)
    print("data:", event.postback.data)
  
   # print("--------test----------",occured_time,user_id,event.postback.data)
    if "begin" in event.postback.data:
	db = MySQLdb.connect(host="localhost", user="root", passwd="0000", db="1968", charset="utf8")
        cursor = db.cursor()
        occured_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
        user_id = event.source.user_id       
        begin = event.postback.data
        sql="SELECT * FROM notification WHERE user_id='%s'" % (user_id)       
        cursor.execute(sql)
        results = cursor.fetchone()
        print results
        if results == None:
               sql="INSERT INTO notification (user_id,begin,occured_time) VALUES ('%s','%s','%s')" % (user_id,begin,occured_time,)
               cursor.execute(sql)
               db.commit()
               print("insert completed==========================================")
        else:
               sql="UPDATE notification SET begin='%s', occured_time='%s' WHERE user_id='%s'" % (begin,occured_time,user_id)
               cursor.execute(sql)
               db.commit()
               print("update completed==========================================")
        print(sql)
	db.commit()
	db.close()
    if "end" in event.postback.data:
	db = MySQLdb.connect(host="localhost", user="root", passwd="0000", db="1968", charset="utf8")
        cursor = db.cursor()
        occured_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
        user_id = event.source.user_id
        destination = event.postback.data
        sql="UPDATE notification SET destination='%s' WHERE user_id='%s'" % (destination, user_id)
        cursor.execute(sql)

	cursor.execute("SELECT * FROM notification")
	results = cursor.fetchall()

	for record in results:
		user_col0 = record[0]  #使用者id
        	user_col1 = record[1]  #使用者起點
        	user_col2 = record[2]  #使用者終點
		if user_col0 == user_id:
		    strlist1 = user_col1.split('&')  #1&begin 切1出來
		    strlist2 = user_col2.split('&')  #3&end   切3出來
		    st = int(strlist1[0])
		    ed = int(strlist2[0])
		#else :
		   # print("eeeeeerror")
	print("--------test----------",st,ed) 
	name=['基隆市','台北市','新北市','桃園縣','新竹縣','苗栗縣','台中縣','彰化縣','南投縣','雲林縣','嘉義縣','台南縣','高雄縣','屏東縣']
        
	test_text = ('Search ' + name[st-1] + ' to ' + name[ed-1]+ '？')
	print(test_text)  
	message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text=test_text,
                actions=[
                    PostbackTemplateAction(
                        label='是',
                        data='highway_search_comfirm'
                    ),
                    PostbackTemplateAction(
                        label='否',
                        data='highway_search_cancel'
                    )
                ]
            )
        )
	line_bot_api.reply_message(event.reply_token, message)
	db.commit()
	db.close()



    if event.postback.data == "highway_search_comfirm" or "moreinfo_confirm":
	db = MySQLdb.connect(host="localhost", user="root", passwd="0000", db="1968", charset="utf8")
        cursor = db.cursor()
        occured_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
        user_id = event.source.user_id
        cursor.execute("SELECT *  FROM notification")
	results = cursor.fetchall()

	for record in results:
	    user_col0 = record[0]  #使用者id
    	    user_col1 = record[1]  #使用者起點
    	    user_col2 = record[2]  #使用者終點
	    if user_col0 == event.source.user_id:
		strlist1 = user_col1.split('&')  #1&begin 切1出來
		strlist2 = user_col2.split('&')  #3&end   切3出來
		st = int(strlist1[0])
		ed = int(strlist2[0])

	db2=MySQLdb.connect(host="localhost", user="root", passwd="0000", db="highway", charset="utf8")
	cursor2 = db2.cursor()
	cursor2.execute("SELECT * FROM highway")
	results2 = cursor2.fetchall()

	speedlist=list()
	countlist=list()
	for i in range(0,24):
    	    speedlist.append(0)
    	    countlist.append(0)

	for record2 in results2:
	    highway_col2 = record2[2]  #名稱
	    highway_col11 = int(record2[11])  #車速
    	    highway_col14 = int(record2[14])  #高速公路地區
    	    highway_col15 = record2[15]  #高速公路南北向
#	print (highway_col2)
#	print (highway_col15)  
#        if u'快速公路' in highway_col2 :
#    	    print("name success")
#	if highway_col15 == 'N':
#    	    print("direction success")
        
        #南下
	    if st < ed:		
		if highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道1' in highway_col2:
		    speedlist[0]=speedlist[0]+highway_col11
		    countlist[0]=countlist[0]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'汐五高架' in highway_col2:
			speedlist[1]=speedlist[1]+highway_col11
			countlist[1]=countlist[1]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道2' in highway_col2:
			speedlist[2]=speedlist[2]+highway_col11
			countlist[2]=countlist[2]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道3' in highway_col2:
			speedlist[3]=speedlist[3]+highway_col11
			countlist[3]=countlist[3]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國3甲' in highway_col2:
			speedlist[4]=speedlist[4]+highway_col11
			countlist[4]=countlist[4]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'台2己' in highway_col2:
			speedlist[5]=speedlist[5]+highway_col11
			countlist[5]=countlist[5]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'南港聯絡' in highway_col2:
			speedlist[6]=speedlist[6]+highway_col11
			countlist[6]=countlist[6]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道4' in highway_col2:
			speedlist[7]=speedlist[7]+highway_col11
			countlist[7]=countlist[7]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道5' in highway_col2:
                 	speedlist[8]=speedlist[8]+highway_col11
			countlist[8]=countlist[8]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道6' in highway_col2:
			speedlist[9]=speedlist[9]+highway_col11
			countlist[9]=countlist[9]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道8' in highway_col2:
			speedlist[10]=speedlist[10]+highway_col11
			countlist[10]=countlist[10]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'國道10' in highway_col2:
			speedlist[11]=speedlist[11]+highway_col11
			countlist[11]=countlist[11]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路62號' in highway_col2:
			speedlist[12]=speedlist[12]+highway_col11
			countlist[12]=countlist[12]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路64號' in highway_col2:
			speedlist[13]=speedlist[13]+highway_col11
			countlist[13]=countlist[13]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路66號' in highway_col2:
			speedlist[14]=speedlist[14]+highway_col11
			countlist[14]=countlist[14]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路68號' in highway_col2:
			speedlist[15]=speedlist[15]+highway_col11
			countlist[15]=countlist[15]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路72號' in highway_col2:
			speedlist[16]=speedlist[16]+highway_col11
			countlist[16]=countlist[16]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路74號' in highway_col2:
			speedlist[17]=speedlist[17]+highway_col11
			countlist[17]=countlist[17]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路76號' in highway_col2:
			speedlist[18]=speedlist[18]+highway_col11
			countlist[18]=countlist[18]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路78號' in highway_col2:
			speedlist[19]=speedlist[19]+highway_col11
			countlist[19]=countlist[19]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路82號' in highway_col2:
			speedlist[20]=speedlist[20]+highway_col11
			countlist[20]=countlist[20]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路84號' in highway_col2:
			speedlist[21]=speedlist[21]+highway_col11
			countlist[21]=countlist[21]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路86號' in highway_col2:
			speedlist[22]=speedlist[22]+highway_col11
			countlist[22]=countlist[22]+1
		elif highway_col14>=st and highway_col14<=ed and highway_col15=='S' and u'快速公路88號' in highway_col2:
			speedlist[23]=speedlist[23]+highway_col11
			countlist[23]=countlist[23]+1	
		
			
	    elif st > ed:
		if highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道1' in highway_col2:
			speedlist[0]=speedlist[0]+highway_col11
			countlist[0]=countlist[0]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'汐五高架' in highway_col2:
			speedlist[1]=speedlist[1]+highway_col11
			countlist[1]=countlist[1]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道2' in highway_col2:
			speedlist[2]=speedlist[2]+highway_col11
			countlist[2]=countlist[2]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道3' in highway_col2:
			speedlist[3]=speedlist[3]+highway_col11
			countlist[3]=countlist[3]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國3甲' in highway_col2:
			speedlist[4]=speedlist[4]+highway_col11
			countlist[4]=countlist[4]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'台2己' in highway_col2:
			speedlist[5]=speedlist[5]+highway_col11
			countlist[5]=countlist[5]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'南港聯絡' in highway_col2:
			speedlist[6]=speedlist[6]+highway_col11
			countlist[6]=countlist[6]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道4' in highway_col2:
			speedlist[7]=speedlist[7]+highway_col11
			countlist[7]=countlist[7]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道5' in highway_col2:
			speedlist[8]=speedlist[8]+highway_col11
			countlist[8]=countlist[8]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道6' in highway_col2:
			speedlist[9]=speedlist[9]+highway_col11
			countlist[9]=countlist[9]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道8' in highway_col2:
			speedlist[10]=speedlist[10]+highway_col11
			countlist[10]=countlist[10]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'國道10' in highway_col2:
			speedlist[11]=speedlist[11]+highway_col11
			countlist[11]=countlist[11]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路62號' in highway_col2:
			speedlist[12]=speedlist[12]+highway_col11
			countlist[12]=countlist[12]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路64號' in highway_col2:
			speedlist[13]=speedlist[13]+highway_col11
			countlist[13]=countlist[13]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路66號' in highway_col2:
			speedlist[14]=speedlist[14]+highway_col11
			countlist[14]=countlist[14]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路68號' in highway_col2:
			speedlist[15]=speedlist[15]+highway_col11
			countlist[15]=countlist[15]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路72號' in highway_col2:
			speedlist[16]=speedlist[16]+highway_col11
			countlist[16]=countlist[16]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路74號' in highway_col2:
			speedlist[17]=speedlist[17]+highway_col11
			countlist[17]=countlist[17]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路76號' in highway_col2:
			speedlist[18]=speedlist[18]+highway_col11
			countlist[18]=countlist[18]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路78號' in highway_col2:
			speedlist[19]=speedlist[19]+highway_col11
			countlist[19]=countlist[19]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路82號' in highway_col2:
			speedlist[20]=speedlist[20]+highway_col11
			countlist[20]=countlist[20]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路84號' in highway_col2:
			speedlist[21]=speedlist[21]+highway_col11
			countlist[21]=countlist[21]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路86號' in highway_col2:
			speedlist[22]=speedlist[22]+highway_col11
			countlist[22]=countlist[22]+1
		elif highway_col14<=st and highway_col14>=ed and highway_col15=='N' and u'快速公路88號' in highway_col2:
			speedlist[23]=speedlist[23]+highway_col11
			countlist[23]=countlist[23]+1
	value=list()
	for i in range(0,24):
	    value.append(0)
	    if countlist[i] != 0:
                value[i] = speedlist[i] / countlist[i]
	name = ['國道1號','汐五高架','國道2號','國道3號','國3甲','台2己','南港聯絡道路','國道4號','國道5號','國道6號','國道8號','國道10號','快速公路62號','快速公路64號','快速公路66號','快速公路68號','快速公路72號','快速公路74號','快速公路76號','快速公路78號','快速公路82號','快速公路84號','快速公路86號','快速公路88號']
#        print value
#	print ('max value =============================', max(value)) #平均車速
#	print  name[value.index(max(value))] #該道路名稱

	if event.postback.data == "highway_search_comfirm":
	    highway_info = '行車推薦：\n'+ name[value.index(max(value))] + '\n平均車速：\n' + str(max(value))
	    line_bot_api.reply_message(
                event.reply_token,TextSendMessage(text=highway_info))
	    message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='是否查看更多數據',
                    actions=[
                        PostbackTemplateAction(
                            label='是',
                            data='moreinfo_confirm'
                        ),
                        PostbackTemplateAction(
                            label='否',
                            data='moreinfo_cancel'
                        )
                    ]
                )
            )
            line_bot_api.push_message(event.source.user_id, message)
	if event.postback.data == "moreinfo_confirm":
	    moreinfo = '車速資訊：\n'
	    for i in range(0,24):
    	        if(value[i]!=0):
		    moreinfo = moreinfo + name[i] + '：' + str(value[i]) + '\n'
	    line_bot_api.push_message(event.source.user_id, TextSendMessage(text=moreinfo))
	db.close()
	db2.close()
    if event.postback.data == "highway_search_cancel":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/vMKfsEo.jpg', text='起點', title='北北基', actions=[
                PostbackTemplateAction(label='台北市',data='2&begin', text='start from 台北市' ),
                PostbackTemplateAction(label='新北市',data='3&begin', text='start from 新北市' ),
                PostbackTemplateAction(label='基隆市',data='1&begin', text='start from 基隆市' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/vFZNJPn.jpg', text='起點', title='桃竹苗', actions=[
                PostbackTemplateAction(label='桃園市',data='4&begin', text='start from 桃園市' ),
                PostbackTemplateAction(label='新竹市',data='5&begin', text='start from 新竹市' ),
                PostbackTemplateAction(label='苗栗縣',data='6&begin', text='start from 苗栗縣' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/VPwzRAS.jpg', text='起點', title='中彰投', actions=[
                PostbackTemplateAction(label='台中市',data='7&begin', text='start from 台中市' ),
                PostbackTemplateAction(label='彰化縣',data='8&begin', text='start from 彰化縣' ),
                PostbackTemplateAction(label='南投縣',data='9&begin', text='start from 南投縣' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/5cz9Z6N.jpg',text='起點', title='雲嘉南', actions=[
		PostbackTemplateAction(label='雲林縣',data='10&begin', text='start from 雲林縣' ),
                PostbackTemplateAction(label='嘉義縣',data='11&begin', text='start from 嘉義縣' ),
                PostbackTemplateAction(label='台南市',data='12&begin', text='start from 台南市' )
            ]),
            CarouselColumn(thumbnail_image_url='https://i.imgur.com/eHpkqbC.jpg',text='起點', title='南部區域', actions=[
                PostbackTemplateAction(label='高雄縣',data='13&begin', text='start from 高雄縣' ),
                PostbackTemplateAction(label='屏東縣',data='14&begin', text='start from 屏東縣' ),
                PostbackTemplateAction(label='台東縣', data='15&begin', text='別開玩笑了 東部？根本不會塞車好嗎～')
            ])
	])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    if event.postback.data == "camera&south":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='南下', title='1', actions=[
		PostbackTemplateAction(label='北部地區',data='S&1&camera', text='北部地區'),
                PostbackTemplateAction(label='台北→桃園', data='S&2&camera', text='台北→桃園'),
                PostbackTemplateAction(label='桃園→新竹', data='S&4&camera', text='桃園→新竹')
            ]),
            CarouselColumn(text='南下', title='2', actions=[
		PostbackTemplateAction(label='新竹→苗栗', data='S&5&camera', text='新竹→苗栗'),
		PostbackTemplateAction(label='苗栗→台中',data='S&6&camera', text='苗栗→台中'),
                PostbackTemplateAction(label='台中→彰化',data='S&7&camera', text='台中→彰化')
            ]),
	    CarouselColumn(text='南下', title='3', actions=[
		PostbackTemplateAction(label='台中→南投',data='S&9&camera', text='台中→南投'),
		PostbackTemplateAction(label='彰化→雲林',data='S&8&camera', text='彰化→雲林'),
		PostbackTemplateAction(label='雲林→嘉義',data='S&10&camera', text='雲林→嘉義')
            ]),
            CarouselColumn(text='南下', title='4', actions=[
		PostbackTemplateAction(label='嘉義→台南',data='S&11&camera', text='嘉義→台南'),
                PostbackTemplateAction(label='台南→高雄',data='S&12&camera', text='台南→高雄'),
		PostbackTemplateAction(label='高雄→屏東',data='S&13&camera', text='高雄→屏東')
            ])
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    
    if event.postback.data == "camera&north":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='北上', title='1', actions=[
		PostbackTemplateAction(label='北部地區',data='N&1&camera', text='北部地區'),
                PostbackTemplateAction(label='桃園→台北', data='N&4&camera', text='桃園→台北'),
                PostbackTemplateAction(label='新竹→桃園', data='N&5&camera', text='新竹→桃園')
            ]),
            CarouselColumn(text='北上', title='2', actions=[
		PostbackTemplateAction(label='苗栗→新竹', data='N&6&camera', text='苗栗→新竹'),
		PostbackTemplateAction(label='台中→苗栗',data='N&7&camera', text='台中→苗栗'),
                PostbackTemplateAction(label='彰化→台中',data='N&8&camera', text='彰化→台中')
            ]),
	    CarouselColumn(text='北上', title='3', actions=[
		PostbackTemplateAction(label='南投→台中',data='N&9&camera', text='南投→台中'),
		PostbackTemplateAction(label='雲林→彰化',data='N&10&camera', text='雲林→彰化'),
		PostbackTemplateAction(label='嘉義→雲林',data='N&11&camera', text='嘉義→雲林')
            ]),
            CarouselColumn(text='北上', title='3', actions=[
		PostbackTemplateAction(label='台南→嘉義',data='N&12&camera', text='台南→嘉義'),
                PostbackTemplateAction(label='高雄→台南',data='N&13&camera', text='高雄→台南'),
		PostbackTemplateAction(label='屏東→高雄',data='N&14&camera', text='屏東→台南')
            ])
        ])
	template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if "&camera" in event.postback.data:
	strlist = event.postback.data.split('&')  # S&1&camera
	position = strlist[0]
	area = int(strlist[1])
	db=MySQLdb.connect(host="localhost", user="root", passwd="0000", db="highway", charset="utf8")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM highway")
	results = cursor.fetchall()
	location = ['嘿嘿嘿','北部地區','台北→桃園','嘿嘿嘿','桃園→新竹','新竹→苗栗','苗栗→台中','台中→彰化','台中→南投','彰化→雲林','雲林→嘉義','嘉義→台南','台南→高雄','高雄→屏東']
	location2 = ['嘿嘿嘿','北部地區','嘿嘿嘿','嘿嘿嘿','桃園→台北','新竹→桃園','苗栗→新竹','台中→苗栗','彰化→台中','南投→台中','雲林→彰化','嘉義→雲林','台南→嘉義','高雄→台南','屏東→高雄']
	if position =='S':
	    content =  u'監視器URL如下：\n'
	if position =='N':
	    content =  u'監視器URL如下：\n'
        for record in results:
            highway_col14 = int(record[14])  #高速公路地區
            highway_coll2 = record[2]
            highway_col15 = record[15]  #高速公路南北向
	    highway_col16 = record[16]  #URL
	    if area == highway_col14 and position == highway_col15 and highway_col16!=None:
	        content = content +highway_coll2+':'+ highway_col16 + '\n'
	if strlist[2] == "camera":
	    line_bot_api.reply_message(
	        event.reply_token,TextSendMessage(text=content)
	    )
	db.close()





if __name__ == '__main__':
    app.run()

