import os
import json
import glob
from PIL import Image

def get_name(name):
    if len(name.split('+')) == 3:
        name_1, name_2, num = name.split('+')
        return [[name_1, name_2]]
    elif len(name.split('+')) == 4:
        name_1, name_2, name_3, num = name.split('+')
        return [[name_1, name_2], [name_1, name_3], [name_2, name_3]]
    else:
        a = 1

def get_link(pic):
    img_template= "<img style=\'width:WWWpx;height:HHHpx;\' src=/static/picture/links/173/>"
    name_list = get_name(pic)
    for name in name_list:
        link = {}
        num_2 = 10000
        for idol in template_json['nodes']:
            if idol['key'] == name[0]:
                num_1 = idol['category']
            if idol['key'] == name[1]:
                num_2 = idol['category']
        if num_2 == 10000:
            a =0
        img = Image.open("./static/picture/links/" + pic)
        width = str(img.width/10*4)
        height = str(img.height/10*4)
        if max(img.width, img.height) < 700:
            width = str(img.width/10*8)
            height = str(img.height/10*8)
        link['source'] = num_1
        link['target'] = num_2
        link['value'] = img_template.replace('173', pic).replace('WWW', width).replace('HHH', height)
        template_json['links'].append(link)



with open('json/template_2021_json.json', encoding='utf-8') as f:
    template_json = json.load(f)
    f.close()

with open('json/members.json', encoding='utf-8') as f:
    members = json.load(f)
    f.close()

pic_dir = './static/picture/Links'
pic_list = os.listdir(pic_dir)

for pic in pic_list:
    link = get_link(pic)

for idol in template_json['nodes']:
    idol_number = len(os.listdir('./static/' + members[idol['key']]['picture']))
    idol['symbolSize'] = 5 * idol_number

json.dump(template_json, open('./json/data.json', 'w', encoding='utf-8'), ensure_ascii=False)