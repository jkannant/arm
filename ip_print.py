#! python

import sys
import json

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    innermost = {}
    try:
        if filename == 'input2.json':        
            with open('input2.json') as fd:
                json_data = json.load(fd)
                data1 = json_data['vm_private_ips']['value']
                #print(data1)
                datasplit2 = json_data['network']['vms']
                for i in datasplit2:
                    data2 = i['attributes']
                    #print(data2)
                    j = data2['access_ip_v4']
                    k = data2['name']
                    innermost[k] = j
                return compare2(data1,innermost)
        
        elif  filename == 'input1.json':        
            with open('input1.json') as fd:
                json_data = json.load(fd)
                data1 = json_data['vm_private_ips']['value']
                for i in data1.values():
                    print(i)
    
    except FileNotFoundError:
        pass

def compare2(dictOne,dictTwo):
    for key in dictOne:
        valueOne = dictOne[key]
        if key in dictTwo:
            print(valueOne, dictTwo[key])
                  

if __name__ == '__main__':
   main()
