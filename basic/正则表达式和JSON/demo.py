import re
#
# str1 = '''<div data-v-191d6a08="" class="room-anchor card-text p-relative"><span data-v-191d6a08="" title="小霖QL">小霖QL</span>
#   <div data-v-191d6a08="" class="popular-ctnr p-absolute">
#       < i data-v-191d6a08="" class="icon-font icon-popular v-middle dp-i-block"></i>
#       <span data-v-191d6a08="" class="v-middle">13.2 万</span>
#   </div>
# </div><div data-v-191d6a08="" class="room-anchor card-text p-relative">
#   <span data-v-191d6a08="" title="小霖QL">小霖QL</span>
#   <div data-v-191d6a08="" class="popular-ctnr p-absolute">
#       < i data-v-191d6a08="" class="icon-font icon-popular v-middle dp-i-block"></i>
#       <span data-v-191d6a08="" class="v-middle">13.2 万</span>
#   </div>
# </div>
# '''
#
#
# pattern = '<div data-v-191d6a08="" class="room-anchor card-text p-relative">([\s\S]*?)</div>'
#
# origin = re.findall(pattern,str1)
# print(origin)
#
#
#
# # s = "师资力量学校现有教职工近4000余人，其中专任教师1800余人，教授、副教授1100余人，中国科学院院士3名，中国工程院院士3名，" \
# #     "双聘两院院士2名，加拿大工程院院士1名，发展中国家科学院院士1名，“千人计划”53人，“万人计划”学者13人、“长江学者”15人，" \
# #     "国家杰出青年基金获得者21人，国务院学位委员会学科评议组成员6人，入选国家百千万人才工程（“百千万人才工程”一二层次人选、" \
# #     "新世纪百千万人才工程国家级人选）23人、国家创新人才推进计划中青年创新领军人才2人，教育部新世纪优秀人才支持计划入选者134人，" \
# #     "湖南省“百人计划”学者64人，湖南省“芙蓉学者奖励计划”特聘教授、讲座教授17人，享受政府特殊津贴专家201人，国家教学名师4人，" \
# #     "国家自然科学基金创新研究群体3个，教育部“长江学者与创新团队发展计划”创新团队8个，湖南省自然科学基金创新研究群体11个" \
# #     "。（数据截止日期：2017年01月） [31] "  # 由于字符串过长，在编译器中会要求换行，字符“\”为换行后自动添加的，不影响字符串本身
# #
# # # n = re.findall("长江学者(.+?)人", s)  # 正则表达式匹配长江学者人数  提取“长江学者”和其后的“人”之间的字符，返回一个列表
# # # print(n)    # ['"15']
# # # num = re.findall('\d+', str(n))  # 正则表达式提取数字，返回一个列表
# # # print(num)
# # # num = '长江学者:'+num[0]+'人'  # 重新构建一个字符串
# # # print(num)
#

s = "['八阵图名成卧龙，六韬书功在飞熊。']['—— 查德卿「蟾宫曲·怀古」']"
print(type(s))
print(s)

s1 = re.findall(r"(.*)\[([^\[\]]*)\](.*)",s)
print(str(s1))






















