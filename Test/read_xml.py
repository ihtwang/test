#coding=utf-8
import xml.dom.minidom
#打开xml 文档
dom = xml.dom.minidom.parse('info.xml')
#得到文档元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

tagname = root.getElementsByTagName('maxid')
print(tagname[0].tagName)
tagname = root.getElementsByTagName('caption')
print(tagname[2].tagName)
tagname = root.getElementsByTagName('item')
print(tagname[1].tagName)

logins = root.getElementsByTagName('login')
#获得login 标签的username 属性值
username=logins[0].getAttribute("username")
print(username)
#获得login 标签的passwd 属性值
password=logins[0].getAttribute("passwd")
print(password)
items = root.getElementsByTagName('item')
#获得第一个item 标签有id 属性值
id1=items[0].getAttribute("id")
print(id1)
#获得第二个item 标签有id 属性值
id2=items[1].getAttribute("id")
print(id2)

captions=root.getElementsByTagName('caption')
#captions=dom.getElementsByTagName('caption')
#获得第一个标签对的值
c1=captions[0].firstChild.data
print(c1)
#获得第二个标签对的值
c2=captions[1].firstChild.data
print(c2)
#获得第三个标签对的值
c3=captions[2].firstChild.data
print(c3)

