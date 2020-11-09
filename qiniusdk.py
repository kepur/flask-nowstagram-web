"""
create by khan.hozin {2018/12/13}
"""
__author__ = 'hozin'
from runserver import instrgram
from qiniu import Auth,put_data,put_file
import os
#需要填写你的 Access Key 和 Secret Key
access_key = instrgram.config['QINIU_ACCESS_KEY']
secret_key = instrgram.config['QINIU_SECRET_KEY']
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = instrgram.config['QINIU_BUCKET_NAME']

domain_prefix = instrgram.config['QINIU_DOMAIN']

bucket_name=instrgram.config['QINIU_BUCKET_NAME']

#上传七牛保存的文件名  save_file_name
def qiniu_upload_file(source_file,save_file_name):
    token=q.upload_token(bucket_name,save_file_name,3600)
    res,info=put_data(token,save_file_name,source_file.stream)
    print (type(info.status_code), info)
    if info.status_code == 200:
        return domain_prefix + save_file_name
    return None


def qiuniu_test(save_file_name,local_file_path):
    token = q.upload_token(bucket_name, save_file_name, 3600)
    res, info = put_file(token, save_file_name, local_file_path)
    print(type(info.status_code), info)
    if info.status_code == 200:
        return domain_prefix + save_file_name
    return None

import os
print(os.getcwd())