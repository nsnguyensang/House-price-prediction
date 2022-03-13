# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:46:27 2022

@author: Admin
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/Admin/Downloads/House_price/trained_model1.sav', 'rb'))
x=[400,	2, 3,	10	,40,	106.64857	,10.80190	,1	,1156]
x=np.array(x).reshape(1,-1)
y_ = loaded_model.predict(x)
print('Giá dự đoán là (triệu): ')
print(y_)