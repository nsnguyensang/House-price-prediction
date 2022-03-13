# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:52:38 2022

@author: Admin
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Admin/Downloads/House_price/trained_model1.sav', 'rb'))

def prediction(input_data):
    
    input_data_as_numpy_as_reshape = np.array(input_data).reshape(1,-1)
    y_ = loaded_model.predict(input_data_as_numpy_as_reshape)
    return y_


def main():
    import csv
    import pandas as pd
    
    df=pd.read_csv('C:/Users/Admin/Downloads/table(1).csv')
    st.title('House Price Prediction Web App')
    
    Loai_hinh = ["", "Nhà ngõ", "Nhà phố liền kề", "Nhà mặt phố", "Nhà biệt thự"]
    
    t1 = st.text_input('Diện tích đất')
    t2 = st.selectbox('Số phòng ngủ', range(1, 40))
    t3 = st.selectbox('Số phòng vệ sinh', range(1, 40))
    
    a1 = st.selectbox('Tỉnh thành', ['Đà Nẵng', 'Thành phố Hồ Chí Minh', 'Cần Thơ', 'Hà Nội', 'Bình Dương', 'Đồng Nai',
'Hải Phòng', 'Long An', 'Quảng Ngãi', 'Đắk Lắk', 'Bắc Giang', 'Khánh Hòa',
 'Bến Tre', 'Thừa Thiên Huế', 'Sóc Trăng', 'Tây Ninh', 'Vĩnh Phúc', 'Hưng Yên',
 'Bình Thuận', 'Kiên Giang', 'An Giang', 'Bắc Ninh', 'Quảng Nam', 'Nam Định',
 'Vĩnh Long', 'Lâm Đồng', 'Đắk Nông', 'Bình Phước', 'Cà Mau',
 'Bà Rịa - Vũng Tàu', 'Đồng Tháp', 'Hòa Bình', 'Bình Định', 'Hải Dương',
 'Ninh Thuận', 'Tiền Giang', 'Thái Nguyên', 'Thanh Hóa', 'Nghệ An', 'Hậu Giang',
 'Phú Yên', 'Bạc Liêu', 'Quảng Ninh', 'Lào Cai', 'Trà Vinh', 'Phú Thọ',
 'Gia Lai', 'Thái Bình', 'Hà Tĩnh', 'Ninh Bình', 'Kon Tum', 'Hà Nam', 'Yên Bái',
 'Lạng Sơn', 'Sơn La', 'Quảng Trị', 'Tuyên Quang', 'Bắc Kạn', 'Hà Giang',
 'Quảng Bình'])
    list_0 = df.loc[df["tỉnh thành"] == a1]["quận huyện"].values
    a2 = st.selectbox('Quận huyện', list_0)
    t9 = df.loc[df["tỉnh thành"] == a1].loc[df["quận huyện"] == a2]["mật độ dân số"].values[0]
    
    t4 = st.text_input('Chiều ngang')
    t5 = st.text_input('Chiều dọc')
    t6 = st.text_input('Kinh độ')
    t7 = st.text_input('Vĩ độ')
    t8 = st.selectbox('Loại hình nhà ở', Loai_hinh)
    
    
    if t8 == "Nhà ngõ":
        t8 = 1
    if t8 == "Nhà phố liền kề":
        t8 = 2
    if t8 == "Nhà mặt phố":
        t8 = 3
    if t8 == "Nhà biệt thự":
        t8 = 4
    price = ''
    
    if st.button('Dự đoán'):
        price = prediction([t1, t2, t3, t4, t5, t6, t7, t8, t9])
        
    st.success(price)


if __name__ == '__main__':
    main()
   