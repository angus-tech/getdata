import re

path = "./data.txt"
with open(path, 'r') as fr:
    buffer = fr.read()
    pattern = re.compile('uart'+'.*?'+r'status = "'+r'(.*?)'+'";'+'.*?'+'};', re.S)
    result_sta = pattern.findall(buffer)
    length = len(result_sta)
    result = [0 for i in range(length)]
    if result_sta != []:
        count = 0
        print('this is baudrate test port:')
        for i in range(0, length):
            #print('uart%d status = %s'%(i,result_sta[i]))
            if result_sta[i] == 'okay':
                result[i] = 'ttyS%d'%count
                print(result[i])
                count += 1
    else:
        print('No find')
    
    pattern = re.compile('uart'+'.*?'+r'hflow = "'+r'(.*?)'+'";'+'.*?'+'};', re.S)
    result_hf = pattern.findall(buffer)
    length = len(result_hf)
    if result_hf != []:
        print('this is hard flow test port:')
        for i in range(0, length):
            #print('uart%d hflow = %s'%(i,result_hf[i]))
            if result_hf[i] == 'support':
                print(result[i])
    else:
        print('No find')

