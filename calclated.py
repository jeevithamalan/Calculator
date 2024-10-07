import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    
    def div(self):
        if (b==0):
            return "Cannot be divided by Zero"
        else:
            return self.a / self.b

st.set_page_config(layout="wide")
selected=option_menu("Main Menu",['HOME','Calculator'])
if selected == 'HOME':
  
  st.title(":red[Welcome To Calculator App]")
  st.image("https://i5.walmartimages.com/asr/81c9d692-07e8-4c75-b1f0-2476fd6c63a1_1.61b6fd38f228784a3d888d7e761e896b.jpeg")

if selected == 'Calculator':

     a = st.number_input("Enter first number")
     b = st.number_input("Enter second number")

     obj=cal(a,b)
   
     choice = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

     if st.button("Calculate"):
        result = None

        if choice == "Addition":
            result= obj.add()

        elif choice == 'Subtraction':
            result= obj.sub()

        elif choice =='Multiplication':
            result=obj.mul()

        elif choice == 'Division':
            
            result=round(obj.div(),2)
        st.write("Result:",result)
