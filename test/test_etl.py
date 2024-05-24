import sys
import os
current_dir = os.path.dirname(__file__)
relative_path = os.path.join(current_dir, '..')
absolute_path = os.path.abspath(relative_path)
sys.path.append(absolute_path)
import cli
import csv
from extract import extract
from transform import transform
from load import load



def test_save_csv():
    data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"]
    ]

    # 将数据写入 CSV 文件
    with open('./data/data1.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV 文件保存成功！")

def test_etl():
    input_file_path = './data/data.csv'
    output_file_path = './data/data1.json'
    data = transform(extract(input_file_path))
    load(data, output_file_path)
    