# -*- coding: utf-8 -*-
"""
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

dictionary_num={'1':['i','l','j','t'],
            '2':['z'],
            '3':[],
            '4':[],
            '5':['s'],
            '6':['o','c','b'],
            '7':['i','l','j','t','a'],
            '8':['b'],
            '9':['q','o','c','g'],
            '0':['o','q','u','v','c','e']}

def cleaning_data_function(text):
    text=text.lower()
    words = re.split(r'\t', text) 
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
            sys.exit(0)

    else:
        print("Matched in the dictionary. Correct Detection") 
    return list_main 

def find_correction_function(list_main,obtained_text):
        index=list_main[1]
        num=list_main[2]
        list_get=dictionary_num.get(num)
        print("Number", num, "Could have replaced alphabets ",list_get," wrongly")
        flag=0
        for temp in list_get:
            #obtained_text[index]=temp
            temp_string=list(obtained_text)
            temp_string[index]=temp
            obtained_text="".join(temp_string)
            if(obtained_text not in dictionary_correct_names.keys()):
                continue
            else:
                flag=1
                print("Number ",num," was replaced by ",temp)
                print("CORRECT LETTER ", obtained_text, " MATCHED IN DICTIONARY")
                break
        if(flag==0):
            print("NOTE: Corrected word not be available in the dictionary")

file = open(r'C:\Users\nathani_n\Desktop\SpellCorrection\dict.txt', 'r',encoding="utf8")
ProgRoman = re.compile(u'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
new=[]
text = file.read().lower()
file.close()

# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
#text = re.sub('[^a-z+\&+\(+\)+\ \']+', " ", text)
new= cleaning_data_function(text)
print(new)
dictionary_correct_names= dict(Counter([element for sub in new for element in sub]))
print(dictionary_correct_names)

obtained_text=input("Enter a text:  ")
obtained_text=obtained_text.lower()
list_main=[obtained_text]

check_obtained_text_function(obtained_text)
print(list_main)


if(obtained_text not in dictionary_correct_names.keys()):
    find_correction_function(list_main,obtained_text)