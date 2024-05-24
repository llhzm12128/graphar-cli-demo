import json
import pandas as pd

def transform(data):
    """
    csv转换示例: 删除空值并替换列

    Args:
        data (DataFrame): 提取后的数据

    Returns:
        str: 转换后的数据
    """
    json_data = data.to_json(orient = 'records', lines = False, force_ascii = False)
    print(type(json_data))
    return json_data
