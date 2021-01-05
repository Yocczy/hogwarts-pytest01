# yield 生成器
def provider():
    # 循环读取数据列表
    for i in range(5):
        yield i


p = provider()
print(p)

print(next(p))
print(next(p))
print(type(p))
for i in p:
    print(i)


def provide():
    # 循环读取数据列表
    for i in range(10):
        return i


q = provide()
print(q)
print(type(q))


def provid():
    # 循环读取数据列表
    for i in range(5):
        print(i)


provid()
