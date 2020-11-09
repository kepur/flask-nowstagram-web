"""
create by khan.hozin {2018/12/13}
"""
__author__ = 'hozin'

# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = 'SulJFeeiywD44q0goJn1JeE60qX08sDSzi2McDLE'
secret_key = '83FYPOAEtJK4LolJ_m4Dgq3OjJctNyDfLlX2R3U_'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = '7dupub'
# #上传到七牛后保存的文件名
# key = 'my-python-logo.png'
# #生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
# localfile = './sync/bbb.jpg'
# ret, info = put_file(token, key, localfile)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

domain_prefix='static.prettycool.cn'

def qiuniu_test(save_file_name,local_file_path):
    token = q.upload_token(bucket_name, save_file_name, 3600)
    res, info = put_file(token, save_file_name, local_file_path)
    print(type(info.status_code), info)
    if info.status_code == 200:
        return domain_prefix + save_file_name
    return None

if __name__ == '__main__':
    import os
    save_file_name='111222.png'
    local_filename="H:\Dev\PycharmProjects\Flask_Ins\photo_2018-12-01_02-21-47.jpg"
    print(local_filename)
    qiuniu_test(save_file_name,local_filename)