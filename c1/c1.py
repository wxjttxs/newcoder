import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'xiaojing')
    strb = '\n\rhello xiaojing\r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('w')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')
    print 9, strc.find('ello')


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5 | 3, 5 & 3, 5 ^ 3
    x = 2
    y = 3.3
    print 6, x, y, type(x), type(y)


def demo_buildinfunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x+3')
    print 7, chr(65), ord('a')
    print 8, divmod(8, 3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do special
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break


            # continur,break,pass


#
def demo_list():
    lista = [1, 2, 3]  # vector Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb

    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 3  # memset(src,0,len)
    tuplea = (1, 2.3)
    listaa = [1, 2, 3]
    listaa.append(4)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b;


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value:', key, value
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](1, 2)
    print 5, dictb.get('-')(15, 3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)
    print 6, dicta
    del dicta[1]
    print 7, dicta


def demo_set():
    lista = [1, 2, 3]
    seta = set((1, 2, 3))
    setb = set((2, 3, 4))
    print 1, seta
    #   seta.add(4)
    #  print 2, seta
    print 3, seta.intersection(setb), seta & setb
    print 4, seta | setb, seta.union(setb)
    print 5, seta - setb
    #
    seta.add('x')
    print 6, seta
    print 7, len(seta)
    print 8, seta.isdisjoint(set((1, 2)))


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group


def demo_exception():
    try:
        print 2 / 1
        #  print 2/0
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print 'error:', e
    finally:
        print 'clean up'


def demo_random():
    # 1-100
    # random.seed(1)
    # x=prex*10007%xxx
    # prex=x
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 100)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print 5, a


def demo_re():
    str = 'abc123def456gh78'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)

    stra = 'a@163.com,b@126.com,c@gmail.com,d@qq.com,e@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(stra)

    str = '<html><h>title</h><body>xxxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(str)
    p5 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5, p5.findall(str)

    str = 'xx2016-06-19yy'
    p6 = re.compile('\d\d\d\d-\d\d-\d\d')
    print 6, p6.findall(str)
    p7 = re.compile('\d{4}-\d{2}-\d{2}')
    print 7, p7.findall(str)


if __name__ == '__main__':
    qiushibaike()
    # print 'hello world'
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    '''
    user1 = User('u1', 1)
    print user1
    admin1 = Admin('a1', 101, 'a')
    print admin1
'''
    # demo_exception()
    # demo_random()
    # demo_re()
