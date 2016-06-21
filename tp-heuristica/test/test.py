'''
Created on Jun 20, 2016

@author: gaston
'''
def func(a, lst):
    a += 1
    del lst[-1]


a = 1
lst = [1,2,3]
func(a, lst)


print a
print lst