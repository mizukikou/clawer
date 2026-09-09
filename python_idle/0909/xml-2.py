import xml.etree.cElementTree as ET

xml_string = '''
<news_list>
    <item id="1">
        <title>Python 爬蟲入門</title>
        <author>老師</author>
    </item>
    <item id="2">
        <title>AI 時代來臨</title>
        <author>小助手</author>
    </item>
</news_list>
'''

root = ET.fromstring(xml_string)

for item in root.findall('item'):
    item_id = item.get('id')
    title = item.find('title').text
    author = item.find('author').text
    print(item_id, title, author)
