#!/usr/bin/python
import sys
import os
import re
import redis
#from autocomplete_redis_python import complete
r = redis.StrictRedis(host='localhost', port=6379, db=0)


# this module will ask for options addword or autocomplete


def complete(r,prefix,count):
    results = []
    rangelen = 50 # This is not random, try to get replies < MTU size
    start = r.zrank('redisdb',prefix)
    if not start:
         return []
    while (len(results) != count):
         range = r.zrange('redisdb',start,start+rangelen-1)
         start += rangelen
         if not range or len(range) == 0:
             break
         for entry in range:
             minlen = min(len(entry),len(prefix))
             if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
             if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])

    return results
#
#choice call options
def main():

#	this will read the command line argument 2 passed with program execution

    choice = sys.argv[1]
    res = re.findall(r"[\w']+", choice)


#	if Decision making to add_worrd or auto complete

    if( res[0]== 'add_word'):
        print("\nYou choose to add word option \n")

	# Calling Ruby script to add words to redis  
	## python script havin issue while giving input 
	### zadd requires at least one element/score pair
	#### Using Ruby Script to add data 
        os.system("ruby compl1.rb " + res[2])

    if( res[0] == 'autocomplete'):
        print("You choose autocomplete Option \n")
        key = res[2] 
        print complete(r,key,50)


if __name__ == '__main__':
   main() 

