import pandas as pd
import streamlit as st
import seaborn as sns


@st.cache(persist=True,allow_output_mutation=True)
def explore_data(dataset):
	df = pd.read_csv(dataset)
	df = df.head(1000) 
	st.write(df.columns)
	df['lat'] = df['sourceLatitude']
	df['lon'] = df['sourceLongitude']
	return df
my_dataset = 'train.csv'
data = explore_data(my_dataset)


def main():
    st.title("درآمد خود را پیشبینی کنید")
    st.subheader("EDA Web App with Streamlit ")
    st.markdown("""
 براساس داده های به دست آمده از نظرسنجی سالیانه برنامه نویس ها و مدیران سیستم یک مدل یادگیری ماشین توسعه داده شده است تا درآمد برنامه نویس ها را پیشبینی کند.
    	""")

st.map(data)