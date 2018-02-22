from sys import argv

script,filename = argv

print 'We are going to erase %r' %filename
print 'If you dont want that hit CTRL-C'
print 'If you do want that, hit RETURN'

raw_input('?')


print 'Opening the file...'
target = open(filename,'w')


print 'Truncating the file. Goodbye!'
target.truncate()


print 'Now I am going to ask you for three lines'

line1 = raw_input('line1:')
line2 = raw_input('line2:')
line3 = raw_input('line3:')

print 'Im going to write these to a file'

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print 'Finally we close it'
target.close()
