# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:22:38 2018

@author: Aniruddh Nathani
"""

import re
import inflection
#import itertools
from collections import Counter
from nltk.corpus import stopwords
stoplist=set(stopwords.words('english'))
#import sys
import pandas as pd
import operator

dictionary_num={'1':['i','l','j','t','h'],
                '2':['z'],
                '3':[],
                '4':[],
                '5':['s'],
                '6':['o','c','b'],
                '7':['i','l','j','t','a'],
                '8':['b','e',],
                '9':['q','o','c','g'],
                '0':['o','q','u','v','c','e']
                }
'''
dictionary_num={'1':['i','l','j','t','h','a','b','c','d','e','f','g','k','m','n','o','p',
                     'q','r','s','u','v','w','x','y','z'],
                '2':['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                     'q','r','s','t','u','v','w','x','y'],
                '3':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                     'r','s','t','u','v','w','x','y','z'],
                '4':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                     'r','s','t','u','v','w','x','y','z'],
                '5':['s','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                     'q','r','t','u','v','w','x','y','z'],
                '6':['o','c','b','a','d','e','f','g','h','i','j','k','l','m','n','p','q',
                     'r','s','t','u','v','w','x','y','z'],
                '7':['i','l','j','t','a','b','c','d','e','f','g','h','k','m','n','o','p',
                     'q','r','s','u','v','w','x','y','z'],
                '8':['b','e','a','c','d','f','g','h','i','j','k','l','m','n','o','p','q',
                     'r','s','t','u','v','w','x','y','z'],
                '9':['q','o','c','g','a','b','d','e','f','h','i','j','k','l','m','n','p',
                     'r','s','t','u','v','w','x','y','z'],
                '0':['o','q','u','v','c','e','a','b','d','f','g','h','i','j','k','l','m',
                     'n','p','r','s','t','w','x','y','z']
                }
'''
def cleaning_data_function(text):
    text=text.lower()
    words = re.split('\t', text)
    for word in words:
        text1 = ProgRoman.sub(' ', word)
        split= re.split(r' ', text1)
        for text2 in split :
            if (text2 not in stoplist) and (len(text2)> 2):
                '''
                temp_string=list(text2)
                if (temp_string[-1]==','):
                    temp_string.pop()
                    obtained_text="".join(temp_string)
                elif (temp_string[0]=='\('):
                    temp_string.pop()
                    temp_string.popleft()
                    obtained_text="".join(temp_string)
                elif (temp_string[0]=='\)'):
                    temp_string.pop()
                    obtained_text="".join(temp_string)
                '''
                msg=[inflection.singularize(text2)]
                new.append(msg)
    return new 

def cleaning_data_function_new(text):
    text=text.lower()
    words = re.split(r'\n', text) 
    for word in words:
        text1 = ProgRoman.sub(' ', word)
        split= re.split(r' ', text1)
        msg=[inflection.singularize(text2) for text2 in split if (text2 not in stoplist) and (len(text2)> 2)]
        new1.append(msg)
    return new1     

def check_obtained_text_function(obtained_text):
    count=0
    times=0
    if(obtained_text not in dictionary_correct_names.keys()):
        print("Not in dictionary")
        for i in obtained_text:
            if(i.isdigit()):
                times=times+1
                
        if(times==1):       
            for i in obtained_text:
                if(i.isdigit()):
                    list_main.append(count)
                    list_main.append(i)
                    break
                count=count+1
                
        elif(times==2):       
            for i in obtained_text:
                if(i.isdigit()):
                    list_main.append(count)
                    list_main.append(i)
                count=count+1
                
        else:
            print("NOTE: Input should have atleast one or maximum two DIGIT error")
            #sys.exit(0)
            list_main.append(0)
            list_main.append(0)
    else:
        print("Matched in the dictionary. Correct Detection")
        list_main.append(0)
        list_main.append(0)
    return list_main 


def find_correction_function(k,count_new,list_main,obtained_text):
    index=list_main[1]
    num=list_main[2]
    list_get=dictionary_num.get(num)
    if(list_get==None):
        return 0
    print("Number", num, "Could have replaced alphabets ",list_get," wrongly")
    flag=0
    length=0
    sorted_check_max_key_data=[]
    check_max_key_data={}
    for temp in list_get:
        #obtained_text[index]=temp
        length=length+1     
        temp_string=list(obtained_text)
        temp_string[index]=temp
        obtained_text="".join(temp_string)
        if(obtained_text not in dictionary_correct_names.keys() and length==len(list_get)):
            sorted_check_max_key_data = sorted(check_max_key_data.items(), key=operator.itemgetter(1),reverse=True)                   
            n=1
            print(sorted_check_max_key_data)
            for seq in sorted_check_max_key_data:
                if(n==1):
                    k[count_new]=seq[0]
                    print(k[count_new])
                    n=n-1            
        elif(obtained_text not in dictionary_correct_names.keys()):
            continue
        else:
            check_max_key_data[obtained_text] = dictionary_correct_names.get(obtained_text)
            print(check_max_key_data)
            
            flag=1
            print("Number ",num," was replaced by ",temp)
            print("CORRECT LETTER ", obtained_text, " MATCHED IN DICTIONARY")
            #k[count_new]=obtained_text
            
            if(length==len(list_get)):
                sorted_check_max_key_data = sorted(check_max_key_data.items(), key=operator.itemgetter(1),reverse=True)                   
                n=1
                print(sorted_check_max_key_data)
                for seq in sorted_check_max_key_data:
                        if(n==1):
                            k[count_new]=seq[0]
                            print(k[count_new])
                            n=n-1
            continue
    if(flag==0):
        print("NOTE: Corrected word not be available in the dictionary")
        print('\n \n')

def find_correction_function_new(k,count_new,list_main,obtained_text):
    index1=list_main[1]
    index2=list_main[3]
    num1=list_main[2]
    num2=list_main[4]
    list_get1=dictionary_num.get(num1)
    list_get2=dictionary_num.get(num2)
    if(list_get1==None):
        return 0
    print("Number", num1, "Could have replaced alphabets ",list_get1," wrongly")
    print("Number", num2, "Could have replaced alphabets ",list_get2," wrongly")

    flag=0
    length1=0
    length2=0
    sorted_check_max_key_data=[]
    check_max_key_data={}
    for temp1 in list_get1:
        length1=length1+1     
        temp_string1=list(obtained_text)
        temp_string1[index1]=temp1
        obtained_text="".join(temp_string1)
        
        for temp2 in list_get2:
            length2=length2+1     
            temp_string2=list(obtained_text)
            temp_string2[index2]=temp2
            obtained_text="".join(temp_string2)           
        #obtained_text[index]=temp
            if(obtained_text not in dictionary_correct_names.keys() and length1==len(list_get1)):
                sorted_check_max_key_data = sorted(check_max_key_data.items(), key=operator.itemgetter(1),reverse=True)                   
                n=1
                print(sorted_check_max_key_data)
                for seq in sorted_check_max_key_data:
                    if(n==1):
                        k[count_new]=seq[0]
                        print(k[count_new])
                        n=n-1            
            elif(obtained_text not in dictionary_correct_names.keys()):
                continue
            else:
                check_max_key_data[obtained_text] = dictionary_correct_names.get(obtained_text)
                print(check_max_key_data)
                
                flag=1
                print("Number ",num1," was replaced by ",temp1)
                print("Number ",num2," was replaced by ",temp2)
                print("CORRECT LETTER ", obtained_text, " MATCHED IN DICTIONARY")
                #k[count_new]=obtained_text
                
                if(length1==len(list_get1)):
                    sorted_check_max_key_data = sorted(check_max_key_data.items(), key=operator.itemgetter(1),reverse=True)                   
                    n=1
                    print(sorted_check_max_key_data)
                    for seq in sorted_check_max_key_data:
                            if(n==1):
                                k[count_new]=seq[0]
                                print(k[count_new])
                                n=n-1
                continue
    if(flag==0):
        print("NOTE: Corrected word not be available in the dictionary")
        print('\n \n')
        



file = open(r'C:\Users\nathani_n\Desktop\SpellCorrectionTwoDigit\dict.txt', 'r',encoding="utf-8-sig")
ProgRoman = re.compile(u'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
new=[]
text = file.read().lower()
file.close()

# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
#text = re.sub('[^a-z+\&+\(+\)+\ \']+', " ", text)
new= cleaning_data_function(text)
dictionary_correct_names= dict(Counter([element for sub in new for element in sub]))
print(dictionary_correct_names)

####################
print('\n \n'+' INCORRECT DATA DICTIONARY' + '\n \n')
#################################

data_xls = pd.read_excel(r'C:\Users\nathani_n\Desktop\SpellCorrectionTwoDigit\corrections_one_plus_two_digit_error.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv(r'C:\Users\nathani_n\Desktop\SpellCorrectionTwoDigit\new_csv_one_plus_two_digit_error.csv', index=False, encoding='utf-8')
df=pd.read_csv(r'C:\Users\nathani_n\Desktop\SpellCorrectionTwoDigit\new_csv_one_plus_two_digit_error.csv')
saved_column = df['Error_By_OCR_Reader']
new1=[]
text_new = str(saved_column)
print(text_new)

new1= cleaning_data_function_new(text_new)
print(new1)
dictionary_correct_names_new= dict(Counter([element for sub in new1 for element in sub]))
print(dictionary_correct_names_new)
for k in new1:
    count_new=0 #Variable for updating in k[count_new]
    for obtained_text in k: 
        print('\n \n')
        print(obtained_text)
        obtained_text=obtained_text.lower()
        list_main=[obtained_text]
        check_obtained_text_function(obtained_text)
        print(list_main)
        
        if(len(list_main)==3):
        #CORRECTION LOGIC STARTS HERE
            if(obtained_text not in dictionary_correct_names.keys()):
                    find_correction_function(k,count_new,list_main,obtained_text)
            count_new=count_new+1

        if(len(list_main)==5):
            if(obtained_text not in dictionary_correct_names.keys()):
                    find_correction_function_new(k,count_new,list_main,obtained_text)
            count_new=count_new+1           
        
    print('\n \n'+'NEW COMPANY NAME CHEKING')
    
#Updating the list and appendin it into the csv file
print('\n \n'+"UPDATED LIST")
print('\n \n')
Corrected_Names=[]
for k in new1:
    k=" ".join(k)
    Corrected_Names.append(k)
print(Corrected_Names)

csv_input = pd.read_csv(r'C:\Users\nathani_n\Desktop\SpellCorrectionTwoDigit\new_csv_one_plus_two_digit_error.csv')
csv_input['Corrected_Names'] = pd.DataFrame(Corrected_Names)
csv_input.to_csv(r'C:\Users\nathani_n\Desktop\SpellCorrectionTwoDigit\output_one_plus_two_digit_corrected.csv', index=False)
