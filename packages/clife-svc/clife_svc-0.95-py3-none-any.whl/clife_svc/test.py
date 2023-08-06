import asyncio
import datetime
import os.path
import random
import re
import threading
from typing import Optional

import requests
import uvicorn

from clife_svc.application import App
#from rocketmq.client import Producer, Message
from clife_svc.errors.error_code import ParameterException, ContentException, DecodeImageException

app = App('clife-svc-test', './logs')
#producer = Producer('PID-XXX')
#producer.set_namesrv_addr('10.6.14.3:9876')
#producer.start()


async def detect(client_params: Optional[dict] = None) -> dict:
    res = {'code': 0, 'msg': 'success'}
    # res1 = await app.download_file('http://skintest.hetyj.com/ai/2R0FUj3S1630052673_28444.png')
    # print(res1)
    # await asyncio.sleep(3)
    # raise ParameterException()
    # url = await app.upload_file('D:\\abc.xlsx')
    with open('D:\\abc.txt', 'rb') as f:
        url = await app.upload_file_from_buffer('.txt', f)
    print(url)
    data = await app.download_file(url)
    print(data)
    #msg = Message('ANDY_TEST')
    #msg.set_keys('XXX')
    #msg.set_tags('XXX')
    #msg.set_body('hello,andy!')
    #ret = producer.send_sync(msg)
    # raise ParameterException(data='app_name can only be letters, numbers, or strike-through!')
    # raise DecodeImageException
    return res


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    await say_after(5, 'hello')
    await say_after(5, 'world')


def file_name_val():
    print(os.path.splitext('abs.xlsx')[1])
    # print(re.match(r'[\w|-]+$', 'as-_'))
    print(re.match(r'^(\w+-\w+)+$', 'sa-aa-bb-c'))
    print('sa-aa-bb_c'.count('_'))
    if re.match(r'^(\w+-?\w+)+$', 'saa--vvv'):
        print('true')


def asyncio_download():
    loop = asyncio.get_event_loop()
    get_future = asyncio.ensure_future(app.download_file('http://skintest.hetyj.com/ai/WHbtvzo91630315253_abc.xlsx'))
    # get_future = asyncio.ensure_future(app.download_file('http://skintest.hetyj.com/ai/2R0FUj3S1630052673_28444.png'))
    # get_future = asyncio.ensure_future(app.download_file('http://cos.clife.net/ai/9tBplEV21635758985_video_data.mp4',timeout=30))
    loop.run_until_complete(get_future)
    print(get_future.result())


def tid_maker_2():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join(
        [str(random.randint(1, 10)) for i in range(5)])


def skin_analysis_test():
    img = 'https://skinsecret.clife.cn/16231997161161096435932379963.png'
    # url = 'http://clife-ai-cv-skin-analysis.coding.clife.net:30000/'  # V4.6.4旧版
    url = 'http://skin-analysis.coding.clife.net:30000/'  # V4.6.5 新版
    line = img
    # "faceIdTime":0,
    params = {"imageUrl": line,
              'environmentParams':'{"appType":66,"light":null,"distance":null,"sex":null,"birthday":null,"dimensions":[11],"maskFlag":2}',
              'versions': 3}
    u = url + 'getSkinResult'
    res = requests.post(u, data=params, verify=False,timeout=30)
    # result = json.loads(re.text)
    print(res.text)


if __name__ == '__main__':
    app.add_api(path='/detect', endpoint=detect, methods=['POST'])
    # print(app.get_all_conf())
    # print(tid_maker_2())
    uvicorn.run(app.init_api(), host='0.0.0.0', port=30000, debug=True)
