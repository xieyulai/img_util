#!/usr/bin/python
import cv2
import xml.dom.minidom

color_dict = {'person':(255,0,0),'car':(0,188,64),'hat':(0,0,255),'bag':(128,0,128)}

def read_xml(xml_path):
	dom = xml.dom.minidom.parse(xml_path)
	root = dom.documentElement
	itemlist = root.getElementsByTagName('object')
	object_list = []
	object_dict = {}
	for i in itemlist:
        name = i.getElementsByTagName('name')[0].childNodes[0].nodeValue
        box = i.getElementsByTagName('bndbox')[0]
        xmin = box.getElementsByTagName('xmin')[0].childNodes[0].nodeValue
        xmax = box.getElementsByTagName('xmax')[0].childNodes[0].nodeValue
        ymin = box.getElementsByTagName('ymin')[0].childNodes[0].nodeValue
        ymax = box.getElementsByTagName('ymax')[0].childNodes[0].nodeValue
        object_dict = {'name':name,'xmin':xmin,'xmax':xmax,'ymin':ymin,'ymax':ymax}
        object_list.append(object_dict)

	return object_list

def draw_frame(img_path,object_list):
	img = cv2.imread(img_path)
	for i in object_list:
		name = i['name']
		xmin = int(i['xmin'])
		xmax = int(i['xmax'])
		ymin = int(i['ymin'])
		ymax = int(i['ymax'])
		cv2.rectangle(img,(xmin, ymin),(xmax, ymax),color_dict[name],2)
		cv2.rectangle(img, (xmin, ymax - 25), (xmax, ymax), color_dict[name], cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(img, name, (xmin + 6, ymax - 6), font, 0.5, (255, 255, 255), 1)

	cv2.imshow('',img)
	return img

fps = 15
capwidth = 1920
capheight = 1080
print 'fps:',fps,' width:',capwidth,' height:',capheight

out = cv2.VideoWriter('./output.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,(capwidth,capheight))

j=0
for i in range(13368,15164+4):
	if i%4 ==0:
        name = 'src/'+str(i)
        img_path = name + '.jpg'
        xml_path = name + '.xml'
        object_list = read_xml(xml_path)
        img = draw_frame(img_path,object_list)
        out.write(img)
        j+=1
        cv2.imwrite('dst/'+str(j)+'.jpg',img)

out.release()

