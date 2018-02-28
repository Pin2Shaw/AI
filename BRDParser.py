# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:56:47 2018

@author: 532395
Pintu Kumar Shaw
"""

# -*- coding: utf-8 -*-



import nltk
from xlrd import open_workbook
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer


class BRD:
    def __init__(self, usrStryID, asa, action, goal):
        self.usrStryID = usrStryID
        self.asa = asa
        self.action = action
        self.goal = goal
        
        #Reads the spreadsheet from the file location
    wb = open_workbook("D:\\AI_Project\\BRD-BankingUserStories-v0.1.xlsx")   
    # Prepares the list of Stop words which can be ignored like the, can , am etc
    stop_words = set(stopwords.words("english"))    
    
    # FOr each sheet in Spreadsheet
    for sheet in wb.sheets():
        numberRows = sheet.nrows
        numberCols = sheet.ncols
        
        items = []
        rows = []
        # For each row in a workbook
        for row in range(1, numberRows):
            values =  []
            filtered_Sentence = []
            verbs = []
            proNouns = []
            # For each columns in the workbook
            for col in range(1, numberCols):
                value = (sheet.cell(row, col).value)
                values.append(value)
                # tokenize the words in the sentence
                print(sent_tokenize(value))
                print("*********************************************")
                words = word_tokenize(value)
                # Words are tagged so, that they can be identified which one is verb/Noun/ Pronoun
                tagged = nltk.pos_tag(words)
                print ("Tagged:",tagged)
                #Retrieves Verb from the Sentence or tokens
                chunkVerb = r"""Chunk: {<VB.?>*} """
                chunkProNoun = r"""Chunk: {<NNP.?>*} """
                
                chunkParser = nltk.RegexpParser(chunkVerb)
                chunked = chunkParser.parse(tagged)
                print ("---->",chunked)
                verbs.append(chunked)
                print ("Grouped VERBS ::", verbs)
                chunkParser = nltk.RegexpParser(chunkProNoun)
                chunked = chunkParser.parse(tagged)
                print("===>",chunked)
                proNouns.append(chunked)
                print ("Chunked Verbs::",verbs)
                print ("Chunked ProNOuns::",proNouns)
                
                #chunked.draw()
                
               
                for w in words:
                    if w not in stop_words:
                        filtered_Sentence.append(w)
            print("Filtered Sentence-->",filtered_Sentence)
                

        break;
        
