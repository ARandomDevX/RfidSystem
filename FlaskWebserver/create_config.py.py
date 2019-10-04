Config_file = open('schule.configcode','w')

Config_file.write('''

schlusszeiten ...

mo= 17:30

di= 17:30

mi= 17:30

do= 17:30

fr= 17:30

### nicht ausfullen

time.maxtime=24:59
time.mintime=0:0
time.chars=num(),char(:)


''')