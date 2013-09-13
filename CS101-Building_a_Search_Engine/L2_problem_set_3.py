#---------------------------------------------------------#
#Thinking hard for two days,finally!					  #	
#Maybe there are better solutions,I'll look for it later! #
#liamlee												  #
#2013-09-02												  #	
#---------------------------------------------------------#


#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################
#观察字符串，由5个‘0’，5个‘*’，3个‘ ’组成，随着数组传入，字符串的结构发生变化
#可以这么认为，三个空格字串按照数字的值往前位移，从而改变原来的结构。


# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    #
    ### Add you code here 
    i = 0
    if value == 0:
        while i < 10:
            print '|00000*****   |'
            i += 1
        return 
    length = len(str(value))
    #print length
    while (10 - length) > 0:
        print '|00000*****   |'
        length += 1
    all_string = []
    #one_string = '|'
    while value > 0:
        one_string = '|'
        val = value % 10
        value /= 10
        first_l = 10 - val  #before the blank
        second_l = 3        #the blank
        last_l = val        #after the blank
        j = 0
        if first_l >= 5:
			#before the blank
            one_string += '00000'
            first_l -= 5
            while first_l>0:
                one_string +='*'
                first_l -= 1
			#the blank
            one_string +='   '
			#after the blank
            while last_l > 0:
                one_string +='*'
                last_l -= 1
            one_string +='|'
        else:
			#before the blank
            while first_l>0:
                one_string +='0'
                first_l -= 1
			#the blank
            one_string +='   '
			#after the blank
            last_l -= 5
            while last_l > 0:
                one_string +='0'
                last_l -= 1
            one_string +='*****'
            one_string +='|'
			
        all_string.append(one_string)
		
    i = len(all_string) -1
    #print len(all_string)
    while i >= 0:
        print all_string[i]
        i -= 1
    return 

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|