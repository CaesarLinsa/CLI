# CLI

使用argparse的一个命令行工具，`<https://github.com/CaesarLinsa/PyExcel>` 是具体使用的例子。

安装

```
git clone https://github.com/CaesarLinsa/CLI.git
cd CLI
python setup.py install
```

使用以下引入cli

```python
from cli.shell import main
def get_main(argv=None):
    main("PyExcel.PyExcel","pyexcel",argv) 
    # main第一个参数命令行使用的模块，模块中"from cli.util import args"定义命令行传入参数。PyExcel.py中所有方法使用do_xxx命名，第二个参数为命令行名称
   
```

例子如下，使用pyexcel create-execl -f xxx  -sn xxx 调用到如下方法：

```python
@args('-f', '--file', metavar='<FILE>', required=True, help="Excel file name")
@args('-sn', '--sheetname', metavar='<SHEETNAME>', required=True, help="Excel file sheet name")
def do_create_excel(args):
    """create a excel file"""
    cc = Client(args.file, args.sheetname)
    cc.save(args.file)
```

