# demo说明
该demo搭建一个ETL工具代码框架，由于目前尚未深入了解graphar中的数据结构，所以demo中实现了一个csv数据到json数据的转换示例。

1. **提取（Extract）**：`extract.py` 中的 `extract` 函数读取输入 CSV 文件并返回数据。

2. **转换（Transform）**：`transform.py` 中的 `transform` 函数对数据进行清洗和转换。

3. **加载（Load）**：`load.py` 中的 `load` 函数将转换后的数据保存。

4. **主脚本**：

   **导入 `cmd` 模块**：

   - `cmd` 模块提供了用于创建交互式命令行界面的基础类 `Cmd`。

   **定义 `CLI` 类**：

   - 继承 `cmd.Cmd` 并重写其方法来定义命令行工具的行为。
   - `intro` 属性定义启动时显示的欢迎信息。
   - `prompt` 属性定义命令提示符。
   - `do_etl`实现串联提取、转换和加载函数。
   - `do_exit` 方法实现退出命令行工具。

   **运行命令行界面**：

   - 在 `__main__` 模块中，创建 `CLI` 类的实例并调用 `cmdloop` 方法启动命令行界面。

# 步骤

1.在终端运行以下命令：

```bash
python cli.py
```

上述命令启动一个交互式命令行界面，提示符显示‘（ETL）’，输入以下命令开启ETL过程：

```
(ETL)etl data\data.csv data\data1.json
```

