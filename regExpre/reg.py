import  re


# Sample string
text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
hall, ball, mall, tall, wall
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'\b\d{3}[-.]\d{3}[-.]\d{3,4}\b')
# pattern = re.compile(r'M(r|rs|s)\.? ?[A-Z][a-z]*\b')


# matches = pattern.finditer(text_to_search)
# print(pattern)
# print(list(matches))
#
# for match in matches:
#     print(match)

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''


pattern= re.compile(r'(https?://)?(www\.)?([a-zA-Z0-9-]+)([.a-zA-Z0-9]+)')

matches = pattern.finditer(urls)
for m in matches:
    print(m.group(3) + m.group(4))