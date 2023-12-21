import streamlit as st
import pandas as pd
import numpy as np
import plost 
import matplotlib.pyplot as plt


st.set_page_config(page_title="Github Repos Dashboard", page_icon=":chart_with_upwards_trend:",layout="wide")
github_data = pd.read_csv("/Users/emily/Documents/Github/beacon-dash/archive/github_dataset.csv").drop_duplicates()
length = github_data.shape[0]
lang = github_data['language'].value_counts()
language_count=pd.concat([lang.index.to_frame(),lang.to_frame()],axis=1)
#language_count = pd.concat([github_data['language'].to_frame(),lang.to_frame()])
#language_count = pd.merge(github_data['language'],lang.to_frame(),left_on=github_data['language'].to_frame().columns[0],right_on=lang.to_frame().columns[0])
df_sorted = github_data.sort_values(by=['stars_count'],ascending=False).reset_index(drop=True)
print(df_sorted[0:4])
print(language_count)
print(language_count.shape)
avg_stars = np.mean(github_data['stars_count']).round().astype(int)
avg_forks = np.mean(github_data['forks_count']).round().astype(int)
avg_pull = np.mean(github_data['pull_requests']).round().astype(int)
avg_contributors = np.mean(github_data['contributors']).round().astype(int)
average_stars_per_language = github_data.groupby('language')['stars_count'].mean().reset_index()
average_stars_per_language.sort_values(by=['stars_count'],ascending=False,inplace=True)


st.title("Github Repositories")

left_column, middle_column,right_column = st.columns((3,3,3))

with left_column:
    st.subheader("At a Glance:")
    st.markdown(f":blue[**{length}**] Unique Repositories ")
    st.markdown(":blue[**Javascript**] Most Frequent Language")
    #st.markdown(f":blue[***{avg_stars}***] Average Stars")

    st.markdown("***On Average:***")
    col1, col2, col3,col4 = st.columns((1.2,2,2,1.5))

    with col1:
        st.markdown(f":violet[**{avg_forks}**] Forks")
    with col2:
        st.markdown(f":violet[**{avg_pull}**] Pull Requests")
    with col3:
        st.markdown(f":violet[**{avg_contributors}**] Contributors")
    with col4:
        st.markdown(f":violet[**{avg_stars}**] Stars")
    st.markdown("***Popular Repos:***")
    st.markdown(":green[**995** stars]: iamshaunjp/Complete-React-Tutorial")
    st.markdown(":green[**977** stars]: adrianhajdin/project_graphql_blog")
    st.markdown(":green[**968** stars]: adrianhajdin/project_medical_pager_chat")
    st.markdown(":green[**960** stars]: brettkromkamp/contextualise")



with middle_column:
    st.subheader("Language Breakdown")
    st.markdown("Top 15 Languages with Highest Average Star Count")
    st.bar_chart(data=average_stars_per_language.head(15),x='language',y='stars_count',use_container_width=False)

    #st.bar_chart(data=df_sorted.head(10),x='repositories',y='stars_count',use_container_width=False)

    #plost.bar_chart(
       # data=df_sorted.iloc[:10],
       # bar='repositories',
       # value='stars_count',
        #group=False)
    
    #st.markdown("Most Stars: :blue[***iamshaunjp/Complete-React-Tutorial***]")

with right_column:
    st.markdown('### Language Frequency')
    st.write('Top 15 Languages by Appearance Frequency')
    plost.pie_chart(
    data=language_count.head(15),
    theta='count',color='language')
    print()
st.divider()
s1,s2 = st.columns(2)
with s1:
    st.markdown('### Repository Properties')

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('Number of Contributors v.s. Number of Pull Requests')
    st.scatter_chart(data=github_data,x='contributors',y='pull_requests',size=50,width=5)
with col2:
    st.markdown('Number of Forks v.s. Number of Stars')
    st.scatter_chart(data=github_data,x='forks_count',y='stars_count',size=50,width=5)

    #st.scatter_chart(data=[github_data['forks_count'].value_counts(),github_data['pull_requests']])

with col3:
    st.markdown('Number of Issues v.s. Number of Pull Requests')
    st.scatter_chart(data=github_data,x='issues_count',y='pull_requests',size=50,width=5)

    #st.bar_chart(data=average_stars_per_language.head(20),x='language',y='stars_count')

    #st.bar_chart(data=average_stars_per_language,x='language',y='stars_count')
