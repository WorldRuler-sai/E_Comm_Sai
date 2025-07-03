import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title("Ecomm_App")
    st.sidebar.title("  Upload Here")
    upl = st.sidebar.file_uploader(" ", type = ['csv','xlsx'])


    if upl is not None :
        try:
            if upl.name.endswith(".csv"):
                d = pd.read_csv(upl)
            else:
                d = pd.read_excel(upl)
            st.sidebar.success("File Uploaded Successfully!")

            st.subheader("Data Of The File:")
            st.dataframe(d)
            
            st.subheader("Details:")
            st.write("The Shape Of The Data: ",d.shape)
            st.write("Columns :",d.columns)
            st.write("The Null Data:",d.isnull().sum())

            st.subheader("Stats:")
            st.write(d.describe())

            sns.countplot(d,x="Gender",hue="Age")
            sns.countplot(d,x="City_Category",hue="Marital_Status")
            

        except Exception as E:
            print(E)

if __name__ == "__main__":
    main()