import streamlit as st
import joblib
import pandas as pd

model=joblib.load("spam_clf.pkl")
st.title("SPAM DETECTION PROJECT")
st.sidebar.image("flag.jpg")
st.sidebar.title("About us")
st.sidebar.text("DEV ARORA")
st.sidebar.title("Contact us at")
st.sidebar.text("9999999999")
col1,col2,col3=st.columns([3,.2,3])
with col1:
    st.header("single message prediction")
    text=st.text_input("Enter MSG")
    if st.button("Predict"):
        result=model.predict([text])
        if result=="spam":
         st.error("Spam->Irrelevent")
        else:
         st.success("Ham-> relevant")
with col3:
   st.header("bulk meassage prediction")
   file=st.file_uploader("select files to upload here",type=['txt',"csv"])
   if file!=None:
      df=pd.read_csv(file,header=None,names=["msg"])
      place=st.empty()
      place.dataframe(df)
      if st.button("Predict",key="b2"):
            df['result']=model.predict(df.msg)
            place.dataframe(df)
           