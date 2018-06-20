import datetime

################################################################
def printTimeStamp(name):									  ##
 print('Автор програми: ' + name)							  ##
 print('Час компіляції: ' + str(datetime.datetime.now()))	  ##
printTimeStamp('Beliaev and Pereviznyk')			          ##
################################################################

word = {2:5, 5:3, 7:4, 10:4, 8:7, 3:2, 0:0, 1:9}     

def magic(dictionary):
    list_sortedF  = [(k, dictionary[k]) for k in sorted(dictionary.keys(), key=dictionary.get, reverse=False)]
    list_sortedT  = [(k, dictionary[k]) for k in sorted(dictionary.keys(), key=dictionary.get, reverse=True)]
    print(list_sortedF)
    print(list_sortedT)
   
print(magic(word))