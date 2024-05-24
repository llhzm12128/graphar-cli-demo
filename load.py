def load(json_data, output_file_path):
    """
    保存数据

    Args:
        json_data (str): 转换后的数据
        output_file_path (str): 数据的保存路径
    """
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)
