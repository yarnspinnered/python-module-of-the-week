import pathlib
from pathlib import *
# Pure means working with strings. Concrete actually interacts with the underlying FS

#Create a path
usr = pathlib.PurePosixPath('/usr')
print(usr)

#Add to the path with the / operator
usr_local = usr / 'local'
print(usr_local)

#Add to the path with another posix path
usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

# Doesn't normalize but actually goes to root
root = usr / '..'
print(root)

# When composing with another posix path, it normalizes
etc = root / '/etc/'
print(etc)

# Concrete path classes can normalize
root = pathlib.Path("/usr/a/b") / ".."
print("Before normalizing ",root)
root = root.resolve()
print("After normalizing ",root)

#can use Path for opening
testio = Path("/home/j/testio")
with open(testio) as f:
    print(f.read())

print('=======using a path directly to open file ==========')
with testio.open('r') as fd:
    print(fd.read())
# Joining paths

root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath('usr','local')
print("What happens when joining: ", usr_local)

#Accessing parts of a path
print(usr_local.parts)

#Going towards the root
print("Direct parent: ", usr_local.parent)
print("All ancestors: ", list(usr_local.parents))

# Useful standard paths
print("Home: ", Path.home())
print("Home: ", Path.cwd())

#List directory contents #1
for f in Path('.').iterdir():
    print(f)

#List directory contents with a globbing iterator
#

# * -- Any amount of any characters, or nothing at all
#
# ? -- One of any character
#
# [abc] -- Just one of the characters "a", "b", or "c".
#
# [^abc] -- Any one character except "a", "b", or "c".
print('==========GLOBBING=============')
for f in Path('.').glob(r'*.py'):
    print(f)

print('==========RECURSIVE GLOBBING=============')
for f in Path('.').rglob(r'*.py'):
    if f.parts[0] == 'venv':
        continue
    print(type(f), f)

print('==========TESTING FILE EQUALITY METHODS==========')
print((Path.cwd()/'motw_io.py').is_dir())
print((Path.cwd()/'motw_io.py').is_file())
print((Path.cwd()/'motw_io.py').is_symlink())
print(Path('venv').is_dir())

print('=======GETTING IFNO===================')
print(Path('motw_io.py').stat())

