import cmd
from extract import extract
from transform import transform
from load import load
class CLI(cmd.Cmd):
    intro = '欢迎使用简单的ETL命令行工具。输入 help 或 ? 查看帮助。\n'
    prompt = '(ETL) '
    ''


    def do_etl(self, args):
        """
        完成数据提取、转换和保存

        Args:
            args (str): 待提取数据路径和转换后数据保存路径
        """
        try:
            input_file_path, output_file_path = args.split()
            if not input_file_path:
                print('输入文件为空')
            if not output_file_path:
                print('输出文件为空')
            data = transform(extract(input_file_path))
            load(data, output_file_path)
        except ValueError:
            print('处理失败。')


    def do_exit(self, args):
        """
        退出程序

        Args:
            args (str): exit

        Returns:
            bool: True
        """
        print('再见！')
        return True

if __name__ == '__main__':
    CLI().cmdloop()
