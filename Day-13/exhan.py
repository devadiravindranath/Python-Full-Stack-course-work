"""try:
   
        a=[1,2,3]
        print(a[6])

except NameError:
    print('a is not defined')

    
except ValueError:
    print('enter requested data type')

    
except TypeError:
    print('data type are different')

except ZeroDivisionError:
    print("can't divide with zero")

except IndexError:
    print('index is not present')

except KeyError:
    print('in dict this key is not present')
else:
    print("no error")

finally:
    print("end of the block")"""

"""try:
   
        a=[1,2,3]
        print(a[6])

except (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) as e:
    print(f'Error occured: {e}')

else:
    print("no error")

finally:
    print("end of the block")"""

#exception is a easy to use for all error handling methods

"""try:
   
        ""a=[1,2,3]
        print(a[6])""
        "a='abcd'+123"
        12/0

except Exception as e:
    print(f'Error occured: {e}')

else:
    print("no error")

finally:
    print("end of the block")"""
#raise exception 
try:
    a=int(input())
    if a<0:
        raise Exception("Enter the positive value")
except Exception as e:
    print(f'Error occured: {e}')

else:
    print("no error")

finally:
    print("end of the block")











