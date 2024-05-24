import pandas as pd

def extract(file_path):
    """
    数据提取

    Args:
        file_path (str): 待提取数据文件路径

    Returns:
        DataFrame: 读取后的数据
    """
    data = pd.read_csv(file_path)
    print(type(data))
    return data
