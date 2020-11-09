"""
create by khan.hozin {2018/12/13}
"""
__author__ = 'hozin'

from qcloud import client
response = client.upload_file(
    Bucket='test04-123456789',
    LocalFilePath='local.txt',
    Key=file_name,
    PartSize=10,
    MAXThread=10,
    EnableMD5=False
)
print(response['ETag'])