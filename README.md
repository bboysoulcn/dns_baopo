### 说明

使用python3编写

### 安装

`pip install -r requirements.txt`

### 使用 

编辑`config.ini`中的参数

```bash
[dns]
# dnsserver1
nameserver1 = 114.114.114.114
# dnsserver2
nameserver2 = 223.5.5.5
# 进程数
processes = 200
# 字典名字
wordlist = 20000.txt
# 域名
domain = baidu.com
# 结果文件名
res_file = res.txt
```

之后使用`python main.py`运行

`20000.txt` 是暴力破解字典