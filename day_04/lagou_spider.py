import requests
import json
import re
from time import sleep
import random


# url = "https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput="

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
#     "Referer":"https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96?oquery=%E6%B5%8B%E8%AF%95&fromSearch=true&labelWords=relative&city=%E5%8C%97%E4%BA%AC",
#     "Host":"www.lagou.com",
#     "Content-type":"application/json;charset=utf-8"
# }
'''
def get_page_info():
    r = requests.get(url = url, headers = headers)
    return r.text

print(get_page_info())
'''

# sum = 0
# for i in range(0, 10):

#     r = requests.get(url = url, headers = headers)
#     print(r.status_code)
#     r.encoding = r.apparent_encoding 
#     result = r.text
#     print(type(result))
#     r.encoding = r.apparent_encoding
#     html = r.text  
#     print(html)

#     data = re.findall('.*Words=relative">(.*)</a></li>.*', html)
#     print(data)
#     if(data == []):
#         sum += 1
#     for i in data:
#         print(i)   # 打印出招聘职位名称
#     sleep(random.randint(3, 10))  # 设置随机3-10s请求一次，发现有时候请求不到结果
#     sleep(10) # 设置10s请求一次，看看结果如何？
# print("失败次数：" + str(sum))

# url = 'https://www.lagou.com/jobs/positionAjax.json'
# params = {
#     'city': '北京',
#     'needAddtionalResult': False
# }
# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#     'Connection': 'keep-alive',
#     'Content-Length': '37',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     # 'Cookie': '_ga=GA1.2.78702461.1548165004; user_trace_token=20190122214959-9bbf2d9e-1e4c-11e9-b735-5254005c3644; LGUID=20190122214959-9bbf32af-1e4c-11e9-b735-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221688cb8cf7ab53-06408f34bc41fa-b781636-2073600-1688cb8cf7ba4f%22%2C%22%24device_id%22%3A%221688cb8cf7ab53-06408f34bc41fa-b781636-2073600-1688cb8cf7ba4f%22%7D; LG_LOGIN_USER_ID=aaab52205b98a0f60aa07b721ddf66d8ad0b40b778f4f634; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAABEEAAJA5C71DB52D74354171BEC203A180A3BFF; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1556298683,1556298717,1556329270,1556690951; _gat=1; LGSID=20190501140858-9b71e4a1-6bd7-11e9-9dba-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%25B5%258B%25E8%25AF%2595%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; _gid=GA1.2.156984551.1556690951; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=4f46124540852c08103196655109d8d21b0dd219cc; LGRID=20190501141501-73e45af4-6bd8-11e9-9dba-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1556691314; SEARCH_ID=766e89a4d52846939659087d26a8cc5a',
#     'Host': 'www.lagou.com',
#     'Origin': 'https://www.lagou.com',
#     'Referer': 'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput=',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
#     'X-Anit-Forge-Code': '0',
#     'X-Anit-Forge-Token': None,
#     'X-Requested-With': 'XMLHttpRequest'
# }
# data = {
#     'first': True,
#     'pn': 1,
#     'kd': '测试'
# }
# requests.urllib3.disable_warnings()
# res = requests.request('POST', url, params = params, headers = headers, data = data, verify=False)
# res.raise_for_status()
# res.encoding = res.apparent_encoding




msg = '{"requestId":null,"msg":null,"resubmitToken":null,"success":true,"content":{"hrInfoMap":{"5748599":{"userId":11860554,"phone":null,"positionName":"人力资源 HR","receiveEmail":null,"portrait":"i/image2/M01/9C/90/CgotOVvIOVuAaTMHAABpvDuK50s664.jpg","canTalk":true,"userLevel":"G1","realName":"卢文婧"},"5879002":{"userId":8173826,"phone":null,"positionName":"联合创始人","receiveEmail":null,"portrait":"i/image2/M01/B7/A1/CgoB5lwQmr6AM5ecAAFRYgo5bfU803.jpg","canTalk":true,"userLevel":"G1","realName":"姜文"},"5823868":{"userId":8167385,"phone":null,"positionName":"","receiveEmail":null,"portrait":null,"canTalk":true,"userLevel":"G1","realName":"HR"},"4801421":{"userId":4813524,"phone":null,"positionName":"人力资源部","receiveEmail":null,"portrait":"i/image2/M01/B8/8D/CgoB5lwTBluAf7FfAABT9wEwSnc923.jpg","canTalk":true,"userLevel":"G1","realName":"侯娇"},"5866079":{"userId":2060980,"phone":null,"positionName":"HR","receiveEmail":null,"portrait":"i/image2/M01/BA/CD/CgotOVwZrmGAbxNyAAAXnRDrGc4214.jpg","canTalk":true,"userLevel":"G1","realName":"ymt"},"5331769":{"userId":12033907,"phone":null,"positionName":"HR","receiveEmail":null,"portrait":"i/image2/M01/D2/4F/CgotOVxBcOOAHLWvAAAyg_Jf43w599.png","canTalk":true,"userLevel":"G1","realName":"HR"},"5885360":{"userId":8148123,"phone":null,"positionName":"招聘主管","receiveEmail":null,"portrait":"i/image2/M01/22/A2/CgotOVzAIP-AYIv_AAAw40FnLJ0230.png","canTalk":true,"userLevel":"G1","realName":"吴明岐"},"5884117":{"userId":105405,"phone":null,"positionName":"","receiveEmail":null,"portrait":null,"canTalk":true,"userLevel":"G1","realName":"Elsa"},"5884008":{"userId":4934721,"phone":null,"positionName":"瓜子二手车","receiveEmail":null,"portrait":"i/image/M00/54/1F/CgpEMll4WZuAdwPiAAHh9ZiwbyA826.jpg","canTalk":true,"userLevel":"G1","realName":"Annie wang"},"5364738":{"userId":8715243,"phone":null,"positionName":"HR","receiveEmail":null,"portrait":"i/image/M00/8D/36/CgpEMlrfFXeAMtCeAAGxnYzrS2w097.jpg","canTalk":true,"userLevel":"G1","realName":"爽微"},"5863502":{"userId":11159776,"phone":null,"positionName":"亿刻HR","receiveEmail":null,"portrait":"i/image2/M01/64/8A/CgotOVs9veWAOypvAAomqZDVRVU224.png","canTalk":true,"userLevel":"G1","realName":"Amy"},"5655181":{"userId":12259614,"phone":null,"positionName":"招聘","receiveEmail":null,"portrait":"i/image2/M01/F0/39/CgoB5lx-D-uAY9G0AAA2aZnRkno472.png","canTalk":true,"userLevel":"G1","realName":"唐成演"},"5885700":{"userId":10133446,"phone":null,"positionName":"软件研发中心总监","receiveEmail":null,"portrait":"i/image3/M00/30/07/CgpOIFqhNT6AeJmHAACcg1jwAco762.png","canTalk":true,"userLevel":"G1","realName":"唐皓"},"5886951":{"userId":7945468,"phone":null,"positionName":null,"receiveEmail":null,"portrait":null,"canTalk":true,"userLevel":"G1","realName":"wangdewei"},"5828871":{"userId":3694500,"phone":null,"positionName":"招聘经理","receiveEmail":null,"portrait":"i/image2/M01/25/C9/CgoB5lzGruyAbl3wAAAYC0SUpsg192.png","canTalk":true,"userLevel":"G1","realName":"Purple"}},"pageNo":1,"positionResult":{"positionName":null,"totalCount":4505,"industryField":null,"companySize":null,"resultSize":15,"strategyProperty":{"name":"dm-csearch-useLayeredDisplay","id":1},"queryAnalysisInfo":{"companyName":null,"positionName":"测试","jobNature":null,"industryName":null,"usefulCompany":false},"hotLabels":null,"hiTags":null,"locationInfo":{"city":"北京","district":null,"queryByGisCode":false,"businessZone":null,"locationCode":null,"isAllhotBusinessZone":false},"result":[{"companyId":62,"score":0,"positionId":5331769,"positionName":"测试（高级）工程师","createTime":"2019-04-30 19:55:45","workYear":"1-3年","education":"本科","city":"北京","companyLogo":"i/image2/M01/79/0A/CgoB5ltr2A-AM5SFAADbT9jQCn841.jpeg","jobNature":"全职","salary":"15k-30k","approve":1,"industryField":"移动互联网,数据服务","companyShortName":"字节跳动","financeStage":"C轮","positionAdvantage":"六险一金，高薪期权，免费三餐，租房补贴","companySize":"2000人以上","companyLabelList":["扁平管理","弹性工作","大厨定制三餐","就近租房补贴"],"publisherId":12033907,"district":"海淀区","positionLables":["测试"],"industryLables":[],"businessZones":null,"formatCreateTime":"1天前发布","longitude":"39.963365","latitude":"39.963365","companyFullName":"北京字节跳动科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":4,"resumeProcessDay":1,"imState":"today","lastLogin":1556621507000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":null,"stationname":null,"linestaion":null,"thirdType":"测试工程师","skillLables":["测试"]},{"companyId":23039,"score":0,"positionId":5655181,"positionName":"测试工程师","createTime":"2019-04-28 09:04:45","workYear":"不限","education":"本科","city":"北京","companyLogo":"i/image/M00/73/BB/CgpEMlozoTuAdljKAABA2QMgfo4109.jpg","jobNature":"全职","salary":"15k-30k","approve":1,"industryField":"医疗健康","companyShortName":"好大夫在线","financeStage":"D轮及以上","positionAdvantage":"定期体检 带薪休假 发展好","companySize":"500-2000人","companyLabelList":["五险一金","带薪年假","绩效奖金","专项奖金"],"publisherId":12259614,"district":"朝阳区","positionLables":["测试"],"industryLables":[],"businessZones":["定福庄","管庄"],"formatCreateTime":"3天前发布","longitude":"116.569059","latitude":"39.912551","companyFullName":"互动峰科技（北京）有限公司","adWord":0,"hitags":["免费班车","一年调薪2次","免费体检"],"resumeProcessRate":100,"resumeProcessDay":1,"imState":"threeDays","lastLogin":1556606017000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"八通线","stationname":"褡裢坡","linestaion":"6号线_褡裢坡;八通线_传媒大学;八通线_双桥","thirdType":"测试工程师","skillLables":["测试"]},{"companyId":7835,"score":0,"positionId":5884117,"positionName":"※测试工程师（北京）","createTime":"2019-04-30 16:17:29","workYear":"3-5年","education":"本科","city":"北京","companyLogo":"i/image/M00/46/E3/Cgp3O1eN2JaAESTsAABXU_egeWg508.png","jobNature":"全职","salary":"15k-25k","approve":1,"industryField":"移动互联网","companyShortName":"金山办公软件","financeStage":"上市公司","positionAdvantage":"团队优秀 业务前景好 六险一金 年度旅行","companySize":"2000人以上","companyLabelList":["年底双薪","节日礼物","技能培训","绩效奖金"],"publisherId":105405,"district":"海淀区","positionLables":["互联网金融","借贷","性能测试","app测试","自动化测试","功能测试"],"industryLables":["互联网金融","借贷","性能测试","app测试","自动化测试","功能测试"],"businessZones":["西三旗","上地","清河"],"formatCreateTime":"1天前发布","longitude":"116.337595","latitude":"40.03325","companyFullName":"北京金山软件有限公司","adWord":0,"hitags":null,"resumeProcessRate":5,"resumeProcessDay":2,"imState":"today","lastLogin":1556693568000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"13号线","stationname":"上地","linestaion":"13号线_上地","thirdType":"测试工程师","skillLables":["性能测试","app测试","自动化测试","功能测试"]},{"companyId":205367,"score":0,"positionId":5823868,"positionName":"测试和问题管理工程师（ticket manager","createTime":"2019-04-24 17:17:47","workYear":"3-5年","education":"本科","city":"北京","companyLogo":"i/image/M00/2E/7C/CgpFT1k2WFiAZNX1AAAK8hOpGrQ559.jpg","jobNature":"全职","salary":"15k-30k","approve":1,"industryField":"移动互联网,硬件","companyShortName":"问众智能","financeStage":"不需要融资","positionAdvantage":"晋升空间，带薪年假，","companySize":"50-150人","companyLabelList":["绩效奖金","午餐补助","健身房福利"],"publisherId":8167385,"district":"海淀区","positionLables":["Jmeter","测试"],"industryLables":[],"businessZones":["中关村","知春路","双榆树"],"formatCreateTime":"2019-04-24","longitude":"116.338245","latitude":"39.970975","companyFullName":"问众智能信息科技（北京）有限公司","adWord":0,"hitags":null,"resumeProcessRate":40,"resumeProcessDay":1,"imState":"disabled","lastLogin":1556526816000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"10号线","stationname":"知春路","linestaion":"10号线_知春里;10号线_知春路;10号线_西土城;13号线_大钟寺;13号线_知春路","thirdType":"测试工程师","skillLables":["Jmeter","测试"]},{"companyId":394190,"score":0,"positionId":5863502,"positionName":"测试工程师","createTime":"2019-04-28 11:37:31","workYear":"1-3年","education":"本科","city":"北京","companyLogo":"i/image2/M01/64/84/CgotOVs9t9uAHY-wAAomqZDVRVU364.png","jobNature":"全职","salary":"15k-25k","approve":1,"industryField":"移动互联网","companyShortName":"区块节点","financeStage":"不需要融资","positionAdvantage":"期权激励,年底多薪,绩效奖金,弹性工时","companySize":"50-150人","companyLabelList":[],"publisherId":11159776,"district":"朝阳区","positionLables":["测试","性能测试","自动化"],"industryLables":[],"businessZones":["望京","来广营"],"formatCreateTime":"3天前发布","longitude":"116.469948","latitude":"40.013008","companyFullName":"北京区块节点科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":1,"imState":"threeDays","lastLogin":1556508546000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"14号线东段","stationname":"东湖渠","linestaion":"14号线东段_来广营;14号线东段_东湖渠","thirdType":"测试工程师","skillLables":["测试","性能测试","自动化"]},{"companyId":302345,"score":0,"positionId":5828871,"positionName":"测试开发工程师","createTime":"2019-04-30 10:55:10","workYear":"1-3年","education":"本科","city":"北京","companyLogo":"i/image3/M00/21/0F/Cgq2xlqTnRuATonBAAA7CV_wFDU472.png","jobNature":"全职","salary":"15k-30k","approve":1,"industryField":"移动互联网","companyShortName":"顺丰同城科技","financeStage":"不需要融资","positionAdvantage":"成长快；七险一金；产品形态多样","companySize":"500-2000人","companyLabelList":[],"publisherId":3694500,"district":"海淀区","positionLables":["企业服务","物流","测试","测试开发"],"industryLables":["企业服务","物流","测试","测试开发"],"businessZones":["学院路","清河"],"formatCreateTime":"1天前发布","longitude":"116.352569","latitude":"40.014838","companyFullName":"北京顺丰同城科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":1,"imState":"today","lastLogin":1556622652000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":null,"stationname":null,"linestaion":null,"thirdType":"测试工程师","skillLables":["测试","测试开发"]},{"companyId":393510,"score":0,"positionId":5748599,"positionName":"测试工程师","createTime":"2019-04-28 19:57:40","workYear":"3-5年","education":"本科","city":"北京","companyLogo":"i/image2/M01/19/84/CgotOVyxjp2AADr5AAIWoBHmdVw796.png","jobNature":"全职","salary":"17k-25k","approve":1,"industryField":"移动互联网","companyShortName":"右划","financeStage":"B轮","positionAdvantage":"大牛云集,工程师文化,一年15薪","companySize":"150-500人","companyLabelList":["股票期权","带薪年假","午餐补助","定期体检"],"publisherId":11860554,"district":"朝阳区","positionLables":["测试","app测试","自动化测试"],"industryLables":[],"businessZones":["望京","来广营"],"formatCreateTime":"3天前发布","longitude":"116.48233","latitude":"39.997316","companyFullName":"北京右划网络科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":1,"imState":"threeDays","lastLogin":1556594848000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"15号线","stationname":"望京东","linestaion":"14号线东段_望京;14号线东段_阜通;14号线东段_望京南;15号线_望京东;15号线_望京","thirdType":"测试工程师","skillLables":["测试","app测试","自动化测试"]},{"companyId":212785,"score":0,"positionId":5879002,"positionName":"测试工程师","createTime":"2019-04-30 16:59:31","workYear":"3-5年","education":"大专","city":"北京","companyLogo":"i/image2/M01/CC/6A/CgoB5lw1pKCAKKsnAAICiWXX8jg91.jpeg","jobNature":"全职","salary":"10k-20k","approve":1,"industryField":"硬件","companyShortName":"INDEMIND","financeStage":"不需要融资","positionAdvantage":"期权、技术领先、学习氛围浓厚、前沿领域","companySize":"15-50人","companyLabelList":["带薪年假","定期体检","扁平管理","节日礼物"],"publisherId":8173826,"district":"朝阳区","positionLables":["智能硬件","性能测试","自动化测试","app测试","硬件测试"],"industryLables":["智能硬件","性能测试","自动化测试","app测试","硬件测试"],"businessZones":null,"formatCreateTime":"1天前发布","longitude":"116.481901","latitude":"39.990758","companyFullName":"北京盈迪曼德科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":80,"resumeProcessDay":1,"imState":"today","lastLogin":1556622957000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"15号线","stationname":"望京东","linestaion":"14号线东段_望京;14号线东段_阜通;14号线东段_望京南;15号线_望京东;15号线_望京","thirdType":"测试工程师","skillLables":["性能测试","自动化测试","app测试","硬件测试"]},{"companyId":50702,"score":0,"positionId":5886951,"positionName":"QA-无人配送","createTime":"2019-04-30 14:58:34","workYear":"3-5年","education":"本科","city":"北京","companyLogo":"i/image/M00/6A/05/Cgp3O1gW8zSAUwUsAABMptH-XY087.jpeg","jobNature":"全职","salary":"20k-35k","approve":1,"industryField":"移动互联网,O2O","companyShortName":"美团点评","financeStage":"上市公司","positionAdvantage":"技术大牛","companySize":"2000人以上","companyLabelList":["技能培训","绩效奖金","岗位晋升","领导好"],"publisherId":7945468,"district":"朝阳区","positionLables":["测试"],"industryLables":[],"businessZones":null,"formatCreateTime":"1天前发布","longitude":"116.486622","latitude":"40.008142","companyFullName":"北京三快在线科技有限公司","adWord":0,"hitags":["早九晚六","学习机会","免费体检","bat背景","定期团建","生日聚会","免费休闲游","带薪病假","交通补助","生子红包","弹性工作","地铁周边","5险1金","晋升机制","6险1金"],"resumeProcessRate":83,"resumeProcessDay":1,"imState":"disabled","lastLogin":1556612988000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"15号线","stationname":"望京东","linestaion":"15号线_望京东","thirdType":"其他测试","skillLables":["测试"]},{"companyId":32867,"score":0,"positionId":5885700,"positionName":"测试架构师","createTime":"2019-04-30 10:52:43","workYear":"5-10年","education":"本科","city":"北京","companyLogo":"i/image2/M00/1A/A4/CgotOVoBUjOAdGneAAASkYAEg3Q532.png","jobNature":"全职","salary":"15k-30k","approve":1,"industryField":"硬件","companyShortName":"云丁","financeStage":"D轮及以上","positionAdvantage":"小米生态链，智能家居","companySize":"500-2000人","companyLabelList":["股票期权","弹性工作","年度旅游","六险一金"],"publisherId":10133446,"district":"昌平区","positionLables":["智能硬件","白盒测试","app测试","产品测试","性能测试"],"industryLables":["智能硬件","白盒测试","app测试","产品测试","性能测试"],"businessZones":null,"formatCreateTime":"1天前发布","longitude":"116.348162","latitude":"40.080092","companyFullName":"云丁网络技术（北京）有限公司","adWord":0,"hitags":null,"resumeProcessRate":0,"resumeProcessDay":0,"imState":"today","lastLogin":1556693055000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"8号线北段","stationname":"平西府","linestaion":"8号线北段_霍营;8号线北段_回龙观东大街;8号线北段_平西府;13号线_回龙观;13号线_霍营","thirdType":"软件测试","skillLables":["白盒测试","app测试","产品测试","性能测试"]},{"companyId":125447,"score":0,"positionId":4801421,"positionName":"测试工程师","createTime":"2019-04-29 10:52:05","workYear":"3-5年","education":"本科","city":"北京","companyLogo":"i/image/M00/22/43/CgqKkVcUhd-ABbaPAAAes7vzK_w201.png","jobNature":"全职","salary":"15k-20k","approve":1,"industryField":"金融,数据服务","companyShortName":"大象慧云","financeStage":"不需要融资","positionAdvantage":"五险一金,补充医疗,周末双休,弹性工作","companySize":"150-500人","companyLabelList":["带薪年假","定期体检","午餐补助","股票期权"],"publisherId":4813524,"district":"海淀区","positionLables":["硬件制造","测试","脚本","自动化","功能测试"],"industryLables":["硬件制造","测试","脚本","自动化","功能测试"],"businessZones":null,"formatCreateTime":"2天前发布","longitude":"0.0","latitude":"0.0","companyFullName":"大象慧云信息技术有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":1,"imState":"threeDays","lastLogin":1556586130000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":null,"stationname":null,"linestaion":null,"thirdType":"测试工程师","skillLables":["测试","脚本","自动化","功能测试"]},{"companyId":107423,"score":0,"positionId":5884008,"positionName":"资深测试开发","createTime":"2019-04-30 18:58:20","workYear":"5-10年","education":"本科","city":"北京","companyLogo":"i/image2/M01/DB/4A/CgotOVxmWR6AHajrAAAPTaxGj4w370.jpg","jobNature":"全职","salary":"20k-40k","approve":1,"industryField":"O2O","companyShortName":"车好多集团","financeStage":"D轮及以上","positionAdvantage":"测试开发","companySize":"2000人以上","companyLabelList":["带薪年假","弹性工作","免费班车","美女多"],"publisherId":4934721,"district":"朝阳区","positionLables":["新零售","汽车","测试","Web测试"],"industryLables":["新零售","汽车","测试","Web测试"],"businessZones":["望京","酒仙桥","花家地"],"formatCreateTime":"1天前发布","longitude":"116.48086","latitude":"39.97686","companyFullName":"车好多旧机动车经纪（北京）有限公司","adWord":0,"hitags":["一年调薪2次","15薪","mac办公","定期团建"],"resumeProcessRate":100,"resumeProcessDay":4,"imState":"threeDays","lastLogin":1556593889000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"14号线东段","stationname":"将台","linestaion":"14号线东段_望京南;14号线东段_将台","thirdType":"测试工程师","skillLables":["测试","Web测试"]},{"companyId":146407,"score":0,"positionId":5364738,"positionName":"测试工程师 (MJ000081)","createTime":"2019-04-30 15:35:20","workYear":"3-5年","education":"不限","city":"北京","companyLogo":"i/image3/M00/46/B5/CgpOIFrDMNKAIbIoAABTKiA237w110.png","jobNature":"全职","salary":"8k-16k","approve":1,"industryField":"移动互联网,教育","companyShortName":"火花思维","financeStage":"C轮","positionAdvantage":"七险一金，弹性工作，试用期全薪","companySize":"500-2000人","companyLabelList":["在线教育","数学思维","带薪年假","定期体检"],"publisherId":8715243,"district":"朝阳区","positionLables":["测试","自动化测试","黑盒测试"],"industryLables":[],"businessZones":["望京","来广营"],"formatCreateTime":"1天前发布","longitude":"116.474778","latitude":"40.012649","companyFullName":"北京心更远科技发展有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":1,"imState":"today","lastLogin":1556684402000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"15号线","stationname":"东湖渠","linestaion":"14号线东段_来广营;14号线东段_东湖渠;15号线_望京东","thirdType":"测试工程师","skillLables":["测试","自动化测试","黑盒测试"]},{"companyId":48452,"score":0,"positionId":5885360,"positionName":"高级测试工程师","createTime":"2019-04-30 10:07:12","workYear":"3-5年","education":"不限","city":"北京","companyLogo":"i/image2/M00/55/A2/CgoB5lsc3euAGtt2AAAQjiRomc8519.jpg","jobNature":"全职","salary":"18k-35k","approve":1,"industryField":"移动互联网,金融","companyShortName":"小帮规划","financeStage":"B轮","positionAdvantage":"团队氛围好，大牛","companySize":"150-500人","companyLabelList":["年底双薪","五险一金","午餐补助","交通补助"],"publisherId":8148123,"district":"朝阳区","positionLables":["测试","测试开发"],"industryLables":[],"businessZones":["望京","大山子"],"formatCreateTime":"1天前发布","longitude":"116.488885","latitude":"39.999056","companyFullName":"北京积沙成塔科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":3,"imState":"disabled","lastLogin":1556608471000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"15号线","stationname":"望京东","linestaion":"15号线_望京东","thirdType":"测试工程师","skillLables":["测试","测试开发"]},{"companyId":81107,"score":0,"positionId":5866079,"positionName":"测试工程师","createTime":"2019-04-28 17:13:46","workYear":"1-3年","education":"本科","city":"北京","companyLogo":"i/image3/M00/54/18/CgpOIFsPxgKAQ_YbAAC603sdDhs222.png","jobNature":"全职","salary":"10k-18k","approve":1,"industryField":"移动互联网,电子商务","companyShortName":"一亩田","financeStage":"C轮","positionAdvantage":"六险一金，弹性工作，Mac办公，","companySize":"150-500人","companyLabelList":["节日礼物","年底双薪","专项奖金","股票期权"],"publisherId":2060980,"district":"海淀区","positionLables":["测试","测试开发"],"industryLables":[],"businessZones":["清河","西三旗"],"formatCreateTime":"3天前发布","longitude":"116.359972","latitude":"40.039972","companyFullName":"北京一人一亩田网络科技有限公司","adWord":0,"hitags":null,"resumeProcessRate":100,"resumeProcessDay":1,"imState":"today","lastLogin":1556694462000,"explain":null,"plus":null,"pcShow":0,"appShow":0,"deliver":0,"gradeDescription":null,"promotionScoreExplain":null,"firstType":"开发|测试|运维类","secondType":"测试","isSchoolJob":0,"subwayline":"8号线北段","stationname":"西小口","linestaion":"8号线北段_永泰庄;8号线北段_西小口","thirdType":"测试工程师","skillLables":["测试","测试开发"]}]},"pageSize":15},"code":0}'

class PositionInfo(object):
    def __init__(self, companyFullName, salary, city, education, workYear):
        self.companyFullName = companyFullName
        self.salary = salary
        self.education = education
        self.workYear = workYear
        self.city = city

    def showInfo(self):
        print(self.companyFullName)
        print(self.salary)
        print(self.city)
        print('/'.join([self.education, self.workYear]))         # 用 / 连接学历和工作经验
        print('*******************************************') 

positionInfo = json.loads(msg) # 字符串转成字典
# print(positionInfo, type(positionInfo))
content = positionInfo['content']['positionResult']['result'] # 获取职位信息
print(type(content)) # content是列表
# print(content)
result =  [] # 初始化职位结果
for value in content:
    result.append(PositionInfo(value['companyFullName'], value['salary'], value['city'], value['education'], value['workYear']))
# print(len(result))
for v in result:
    v.showInfo()





