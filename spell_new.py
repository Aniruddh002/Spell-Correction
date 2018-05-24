# -*- coding: utf-8 -*-
c="""
Created on Tue May 22 14:05:25 2018
@author: Aniruddh Nathani
"""
import re
import inflection
import itertools
from collections import Counter
import nltk
from nltk.corpus import stopwords
stoplist=set(stopwords.words('english'))
import sys
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

def cleaning_data_function(text):
    text=text.lower()
    words = re.split('\t', text)
    for word in words:
        text1 = ProgRoman.sub(' ', word)
        split= re.split(r' ', text1)
        for text2 in split :
            if (text2 not in stoplist) and (len(text2)> 2):
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
    flag=0
    if(obtained_text not in dictionary_correct_names.keys()):
        print("Not in dictionary")
        for i in obtained_text:
            flag=0
            if(i.isdigit()):
                flag=1
                list_main.append(count)
                list_main.append(i)
                break
            count=count+1
        if(flag==0):
            print("NOTE: Input should have only one digit error")
            #sys.exit(0)
            list_main.append(0)
            list_main.append(0)
    else:
        print("Matched in the dictionary. Correct Detection") 
    return list_main 

def find_correction_function(k,count_new,list_main,obtained_text,obtained_text_corrected):
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


file = open(r'C:\Users\nathani_n\Desktop\SpellCorrection\dict.txt', 'r',encoding="utf-8-sig")
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

data_xls = pd.read_excel(r'C:\Users\nathani_n\Desktop\SpellCorrection\corrections.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv(r'C:\Users\nathani_n\Desktop\SpellCorrection\new_csv.csv', index=False, encoding='utf-8')
df=pd.read_csv(r'C:\Users\nathani_n\Desktop\SpellCorrection\new_csv.csv')
saved_column = df['Error_By_OCR_Reader']
new1=[]
text_new = str(saved_column)
print(text_new)
new1= cleaning_data_function_new(text_new)
dictionary_correct_names_new= dict(Counter([element for sub in new1 for element in sub]))
print(dictionary_correct_names_new)
for k in new1:
    count_new=0
    for j in k:
        obtained_text=j
        print('\n \n')
        print(obtained_text)
        obtained_text=obtained_text.lower()
        list_main=[obtained_text]
        check_obtained_text_function(obtained_text)
        print(list_main)
        obtained_text_corrected=0
        if(obtained_text not in dictionary_correct_names.keys()):
            find_correction_function(k,count_new,list_main,obtained_text,obtained_text_corrected)
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

csv_input = pd.read_csv(r'C:\Users\nathani_n\Desktop\SpellCorrection\new_csv.csv')
csv_input['Corrected_Names'] = pd.DataFrame(Corrected_Names)
csv_input.to_csv(r'C:\Users\nathani_n\Desktop\SpellCorrection\output.csv', index=False)
