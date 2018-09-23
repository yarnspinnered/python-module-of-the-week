import io
import motw_shutil

output =  io.StringIO()
output.write("first line")
output.write("second line")

with open ('/home/j/testio', 'r+') as fd, open('/home/j/testio2', 'w') as fd2:
    l = fd.readlines()

    for i in range(len(l)):
        l[i] = l[i].strip()
    print(l)
print("___")

to_write = ["a",'bb','ccc','dddd']
with open('/home/j/testio2', 'r+') as fd:
    fd.write('\n'.join(to_write))
    fd.seek(0)
    print(fd.read())

res = []
with open('/home/j/testio2', 'r+') as fd:
    for line in fd:
        res.append(line)

print(res)