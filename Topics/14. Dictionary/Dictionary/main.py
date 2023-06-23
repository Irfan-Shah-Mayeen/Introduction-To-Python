#dictionary = A changeable , unordered collection of unique key: value pairs
# Fast beacuse they are use hashing , allow us to access a value quickly

capital={'Bangladesh':'Dhaka',
          'India':'Dehli',
          'China':'Beijing',
          'Russia':'Moscow'}
print(capital['Russia'])
print(capital['Bangladesh'])
#print(capital['USA'])
print(capital.get('Bangladesh'))
print(capital.get('USA'))
print(capital.keys())
print(capital.values())
print(capital.items())
for key,value in capital.items():
    print(key,value)
capital.update({'Germany':'Berlin'})
for key,value in capital.items():
    print(key,value)
capital.update({'Bangladesh': 'Munshiganj'})
for key,value in capital.items():
    print(key,value)
capital.pop('India')
for key,value in capital.items():
    print(key,value)

