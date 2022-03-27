# -*- coding: utf-8 -*-
import numpy as np

#Created by Fayarretype (Fatih AYAR)
#Fayarretype (Fatih AYAR) tarafından oluşturuldu
#Date 22.12.2018

class Lists:
    @staticmethod
    def getNumberOfElementTypes(data):
        data = list(data).copy()
        numberOfElementTypes = []
        
        for i in range(len(data)):
            if not(data[i] in numberOfElementTypes):
                numberOfElementTypes.append(data[i])
        
        return numberOfElementTypes

class Encoder:
    @staticmethod
    def label(data):
        data = list(data).copy()
        numberOfElementTypes = Lists.getNumberOfElementTypes(data)
        
        for j in range(len(numberOfElementTypes)):
            for k in range(len(data)):
                if data[k] == numberOfElementTypes[j]:
                    data[k] = j
        
        return np.array(data)
    
    @staticmethod
    def oneHot(data):
        data = Encoder.label(list(data).copy())
        numberOfElementTypes = Lists.getNumberOfElementTypes(data)
        
        dataList = np.zeros((len(data), len(numberOfElementTypes)))
        
        for i in range(len(data)):
            for j in range(len(dataList[i])):
                dataList[i:i + 1, data[i]:data[i] + 1] = 1
        
        return dataList
    
    @staticmethod
    def auto(data):
        data = Encoder.label(list(data).copy())

        if len(Lists.getNumberOfElementTypes(data)) == 1:
            return 0         
        elif len(Lists.getNumberOfElementTypes(data)) > 2:
            return Encoder.oneHot(data)

        return data