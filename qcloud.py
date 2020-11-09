"""
create by khan.hozin {2018/12/13}
"""
__author__ = 'hozin'

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = '1400170906'      # 替换为用户的 secretId
secret_key = 'dec50314532efaab8202ff76423da52a'      # 替换为用户的 secretKey
region = 'ap-beijing-1'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)


