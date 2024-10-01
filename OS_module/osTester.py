import os
import  time


# print(dir(os))
# cwd - current working directory
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())
# print(os.listdir())
# os.mkdir('new_folder/one/two')

# os.makedirs(r'new_folder\one\two\three')
# time.sleep(5)
# os.rmdir(r'new_folder\one\two')
# os.remove(r'new_folder\one\two\three\music.mp3')
# os.removedirs(r'new_folder\one\two\three')
# os.rename('sample.mp3', 'new_folder/one/tester.mp3')
# print(os.stat('osTester.py').st_size)
#
# info = os.walk(os.getcwd())
#
# for dirpath, dirnames, filenames in info:
#     print('*' * 20)
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files', filenames)
#
# print(os.environ.get('database_password'))
# print(os.environ.get('HOMEPATH'))
# print(os.path.join(os.environ.get('HOMEPATH'), 'text.py')

print(os.path.basename('/somedir/dir2/text.txt'))
print(os.path.dirname('/somedir/dir2/text.txt'))
print(os.path.split('/somedir/dir2/text.txt'))
print(os.path.splitext('/somedir/dir2/text.txt'))

print(os.path.exists('osTester.py'))
print(os.path.isfile('tester.py'))
print(os.path.isdir('new_folder1'))
