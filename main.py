import dns.resolver
from multiprocessing.dummy import Pool as ThreadPool
import configparser

cf = configparser.ConfigParser()
cf.read('./config.ini')
# dnsserver1
nameserver1 = cf.get('dns', 'nameserver1')
# dnsserver2
nameserver2 = cf.get('dns', 'nameserver2')
# 进程数
processes = cf.get('dns', 'processes')
# 字典名字
wordlist = cf.get('dns', 'wordlist')
# 域名
domain_name = cf.get('dns', 'domain')
# 结果文件名
res_file = cf.get('dns', 'res_file')



i = 0
# 查询dns
def query_dns(domain):
    res_file_name = res_file
    nameserver = []
    nameserver.append(nameserver1)
    nameserver.append(nameserver2)
    try:
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = nameserver
        answers = my_resolver.query(domain, lifetime=5)
        if answers.response.answer:
            with open(res_file_name, "a") as f:
                f.write(domain + "\n")
                print("有解析\t" + domain)

    except Exception as e:
        pass


# 读取字典
def read_wordlist(filename):
    with open(filename, "r") as f:
        word = []
        for i in f:
            word.append(i.strip("\n"))
    return word


if __name__ == '__main__':
    # 读取字典
    word = read_wordlist(wordlist)
    domain = []
    for i in word:
        domain.append(i + "." + domain_name)
    # 多进程
    pool = ThreadPool(processes=int(processes))
    print("开始查询")
    pool.map(query_dns, domain)
    pool.close()
    pool.join()
