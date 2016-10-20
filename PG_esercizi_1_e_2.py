
#Exercise link 1

def match_ends(x):
    
    count=0
    i=0
    while i <=len(x)-1:
        y=x[i]
        if len(y)>=2:        
            if y[0] in (y[len(y)-1]):
                count=count+1
                print y     
        i=i+1        
    return count
    





def front_x(x):
    z=''
    z1=''    
    i=0
    j=0
    while i <=len(x)-1:
        y=x[i]
        if y[0] in ('x'):
            z=z+' '+y
        i=i+1
    
    import string
    start_x=string.split(z)    
    start_x=sorted(start_x)

    while j <=len(x)-1:
        y1=x[j]
        if y1[0] not in ('x'):
            z1=z1+' '+y1
        j=j+1
    
    import string
    start_not_x=string.split(z1)    
    start_not_x=sorted(start_not_x)


    my_list=start_x+start_not_x
    
    return my_list




def sort_last(x):

    j=0
    while j<len(x)-1:
        i=0        
        while i <=len(x)-2:
            y=x[i]
            y1=x[i+1]
            last_y=y[len(y)-1]
            last_y1=y1[len(y1)-1]
            if last_y>last_y1:
                x[i]=x[i+1]
                x[i+1]=y
            i=i+1 
        j=j+1
    return x




def remove_adjacent (x):
   if len(x)>0:    
      i=0    
      while i<=len(x)-2:
          if x[i+1]==x[i]:
              del x[i+1]
          i=i+1
      if x[len(x)-1] == x[len(x)-2]:
          del x[len(x)-1]
   return x



def linear_merge(list1, list2):
    my_list=list1+list2
    final_list=sorted(my_list)
    return final_list



print '***************output Match_ends************************'
matchends1=match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print matchends1

matchends2=match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print matchends2
    
matchends3=match_ends(['aaa', 'be', 'abc', 'hello'])
print matchends3


print '***************output Front_X************************'
front_x1=front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
print front_x1

front_x2=front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x2

front_x3=front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x3


print '***************output Sort_last************************'
sort_last1=sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
output1=[(2, 2), (1, 3), (3, 4, 5), (1, 7)]
if sort_last1 == output1:
    test1='OK'
else:
    test1='KO'    
print sort_last1, test1

sort_last2=sort_last([(1, 3), (3, 2), (2, 1)])
output2=[(2, 1), (3, 2), (1, 3)]
if sort_last2 == output2:
    test2='OK'
else:
    test2='KO'    
print sort_last2, test2

sort_last3=sort_last([(2, 3), (1, 2), (3, 1)])
output3=[(3, 1), (1, 2), (2, 3)]
if sort_last3 == output3:
    test3='OK'
else:
    test3='KO'    
print sort_last3, test3



print '***************output remove_adjacent************************'
remove_adiacent1=remove_adjacent([1, 2, 2, 3])
print remove_adiacent1

remove_adiacent2=remove_adjacent([2, 2, 3, 3, 3])
print remove_adiacent2

remove_adiacent3=remove_adjacent([])
print remove_adiacent3


print '***************output linear_merge************************'
linear_merge1=linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print linear_merge1

linear_merge2=linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print linear_merge2

linear_merge3=linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
print linear_merge3








#Exercise link 2


def donuts (x):
    if x<10:
        (my_string,count)=('Number of donuts: ',x)
    else:
        (my_string,count)=('Number of donuts: ','many')
    return (my_string,count)
    
    
    
    
def both_ends(x):
    if len(x)<2:
        my_string="''"
    else:
        my_string=x[0]+x[1]+x[len(x)-2]+x[len(x)-1]
    return my_string



def fix_start(x):
    i=1
    y=x[0]
    while i<=len(x)-1:
        y=y+' '+x[i]+' '
        i=i+1
            
    import string
    z=string.split(y)
        
    i=1
    while i<=len(z)-1:
        if z[i] in (z[0]):
            z[i]='*'
        i=i+1 
       
    j=1
    k=z[0]
    while j<=len(z)-1:
        k=k+z[j]
        j=j+1
    return k   




def mix_up(a, b):
    my_string=b[0]+b[1]+a[2:]+' '+a[0]+a[1]+b[2:]
    return my_string
    
    
    
def verbing(s):
    if len(s) >=3:
        if s[len(s)-3:] == 'ing':        
            my_string=s+'ly'
        else:
            my_string=s+'ing'
    else:
        my_string=s
   
    return my_string
    
    
    
def not_bad(s):
    import string
    list=string.split(s)
   

    i=0    
    j=0
   
    while i <=len(list)-1:
        
        if list[i] in ('not'):
            j=i+1
            while j<=len(list)-1:
                if list[j] in ('bad','bad!','bad.','bad;','bad:','bad?'):
                    del list [i+1:]
                    list[i]='good'                
                j=j+1 
                 
        i=i+1 
    
    k=1
    my_string=list[0]
    while k <=len(list)-1:  
        my_string= my_string + ' ' + list[k] 
        k=k+1          
        

    return my_string
    
    
    
def front_back(a, b):
    (lena, lenb) = (len(a) + 1)/2, (len(b) + 1)/2
    return a[:lena] + b[:lenb] + a[lena:] + b[lenb:]
    







print '***************output Donuts************************'
donuts1=donuts(5)
print donuts1[0],donuts1[1]

donuts2=donuts(23)
print donuts2[0],donuts2[1]

donuts3=donuts(4)
print donuts3[0],donuts3[1]

donuts4=donuts(9)
print donuts4[0],donuts4[1]

donuts5=donuts(10)
print donuts5[0],donuts5[1]

donuts6=donuts(99)
print donuts6[0],donuts6[1]



print '***************output Both_ends************************'
both_ends1=both_ends('spring')
print both_ends1

both_ends2=both_ends('Hello')
print both_ends2

both_ends3=both_ends('a')
print both_ends3

both_ends4=both_ends('xyz')
print both_ends4



print '***************output Fix_star************************'
fix_start1=fix_start('babble')
print fix_start1

fix_start2=fix_start('aardvark')
print fix_start2

fix_start3=fix_start('google')
print fix_start3

fix_start4=fix_start('donut')
print fix_start4



print '***************output Mix_up************************'
mix_up1=mix_up('mix','pod')   
print mix_up1

mix_up2=mix_up('dog', 'dinner')   
print mix_up2

mix_up3=mix_up('gnash', 'sport')
print mix_up3

mix_up4=mix_up('pezzy', 'firm')
print mix_up4



print '***************output verbing************************'
verbing1=verbing('do')
print verbing1

verbing1=verbing('hail')
print verbing1

verbing1=verbing('swiming')
print verbing1



print '***************output not bad************************'
not_bad1=not_bad('This movie is not so bad')
print 'This movie is not so bad'
print not_bad1

not_bad2=not_bad('This dinner is not that bad!')
print 'This dinner is not that bad!'
print not_bad2

not_bad3=not_bad('This tea is not hot')
print 'This tea is not hot'
print not_bad3

not_bad4=not_bad("It's bad yet not")
print "It's bad yet not"
print not_bad4



print '***************output Front Back************************'
front_back1=front_back('abcd', 'xy')
print front_back1

front_back2=front_back('abcde', 'xyz')
print front_back2

front_back3=front_back('Kitten', 'Donut')
print front_back3