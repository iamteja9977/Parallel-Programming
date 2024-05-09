'''
    Importing all symbols(functions/classes/data) directly
'''



from moduleIntro import funOne, dataOne 
import moduleIntro

funOne()
print(dataOne)

moduleIntro.funTwo() #error
# NameError: name 'dataTwo' is not defined
print(dataTwo)
