import json
import requests

headers = {
    "X-LC-Id": "Oi7gN8vwwMSroqpMrT5O2Dmo-gzGzoHsz",
    "X-LC-Key": "isKyelscfYjdtS6FmyVuHsyY",
    "Content-Type": "application/json",
}

# 请求发送验证码 API
REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'


def send_message(phone):
    """
    phone: 通过网页表单获取的电话号 
    """
    data = {
        "mobilePhoneNumber": phone,
    }

    # post 方法参数包含三部分，如我们之前分析 API 所述
    # REQUEST_SMS_CODE_URL: 请求的 URL
    # data: 请求的内容，另外要将内容编码成 JSON 格式
    # headers: 请求的头部，包含 Id 与 Key 等信息
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)

    if r.status_code == 200:
        return True
    else:
        return False


def verify(phone, code):
    # 使用传进的参数 code 与 phone 拼接出完整的 URL
    target_url = VERIFY_SMS_CODE_URL + "%s?mobilePhoneNumber=%s" % (code, phone)

    r = requests.post(target_url, headers=headers)

    if r.status_code == 200:
        return True
    else:
        return False
    
    
    
    
    
    
