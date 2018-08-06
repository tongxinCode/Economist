# -*- coding: utf-8 -*-

import requests  
import string  
import time  
import hashlib  
import json  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"  
my_appid = '20180806000191911'  
cyber = 'Y4Wta5XdxuL_dxDtSeud'
lower_case = list(string.ascii_lowercase)  
upper_case = list(string.ascii_uppercase)
case = lower_case+upper_case

def requests_for_dst(word):  
    #init salt and calculate sign
    salt = str(time.time())[:10]  
    final_sign = str(my_appid)+word+salt+cyber
    final_sign_unicode=final_sign.decode('gbk')
    final_sign_utf8=final_sign_unicode.encode('utf-8')
    final_sign = hashlib.md5(final_sign_utf8).hexdigest()  
    #区别en,zh翻译请求  
    if list(word)[0] in case:  
        paramas = {  
            'q':word,  
            'from':'en',  
            'to':'zh',  
            'appid':'%s'%my_appid,  
            'salt':'%s'%salt,  
            'sign':'%s'%final_sign  
            }  
        my_url = api_url+'?appid='+str(my_appid)+'&q='+word.decode('gbk')+'&from='+'en'+'&to='+'zh'+'&salt='+salt+'&sign='+final_sign  
    else:  
        paramas = {  
            'q':word,  
            'from':'zh',  
            'to':'en',  
            'appid':'%s'%my_appid,  
            'salt':'%s'%salt,  
            'sign':'%s'%final_sign  
            }  
        my_url = api_url+'?appid='+str(my_appid)+'&q='+word.decode('gbk')+'&from='+'zh'+'&to='+'en'+'&salt='+salt+'&sign='+final_sign  
    response = requests.get(str(my_url)).content  
    content = str(response)  
    json_reads = json.loads(content)  
    return(json_reads['trans_result'][0]['dst'])  
