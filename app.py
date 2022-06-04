import dataclasses
import streamlit as st
import pandas as pd
import numpy as np
from src.visualizations import visualize_all, visualize_selected, all_plot_description, selected_plot_description
from src.elastic import check_and_create_index, elastic_search
from src.introduction import intro_content, team_members
from utils import create_filter_map, filter_data
from elasticsearch import Elasticsearch

DATA_PATH = "./data/final_annotation.csv"
INDEX_NAME = 'yelp_reviews'
DOMAIN = 'elasticsearch'
# DOMAIN = '0.0.0.0'


@st.cache
def load_data():
    data = pd.read_csv(DATA_PATH)
    data = data.iloc[:, 1:]
    return data


def visual_mapper(data_type, plot, feature=None):
    keyword_map = {'Word Cloud': 'word cloud',
                   'Distribution Plot': 'distribution plot',
                   'Bar Plot': 'bar plot'}
    if data_type == 'all':
        with st.spinner('Please wait, this may take a few seconds...'):
            visualize_all(keyword_map[plot])
            all_plot_description(keyword_map[plot])
        if plot == 'Distribution Plot':
            st.caption(
                "Tip: You can click on an 'aspect' key to highlight their corresponding values on the chart.")
    elif data_type == 'selected':
        with st.spinner('Please wait, this may take a few seconds...'):
            visualize_selected(keyword_map[plot], feature)
            selected_plot_description(keyword_map[plot], feature)


def main():
    st.sidebar.title('Annotated Yelp Reviews')

    page = st.sidebar.selectbox(
        '', ('Introduction', 'Data', 'Visualization'), index=0)

    if page == 'Introduction':
        intro_content()
        team_members()

    elif page == 'Data':

        # Load datat and create index
        with st.spinner('Loading data, please wait...'):
            data = load_data()
            es = Elasticsearch(host=DOMAIN)
            index = check_and_create_index(es, DOMAIN, INDEX_NAME, data)

        search_query = st.text_input("Search something...")
        st.subheader('Raw data')
        st.caption(
            'Tip: You can hover over the reviews to view the complete text.')

        service = st.sidebar.multiselect(
            'Service', ('Positive', 'Negative', 'Neutral', 'Undefined'))
        environment = st.sidebar.multiselect(
            'Environment', ('Good', 'Moderate', 'Bad', 'Undefined'))
        price = st.sidebar.multiselect(
            'Price', ('Expensive', 'Reasonable', 'Cheap', 'Undefined'))

        if st.sidebar.button('Apply'):
            with st.spinner('Loading, please wait...'):
                if search_query:
                    data = elastic_search(index, data, search_query)
                filter_dict = {'Service': service,
                               'Environment': environment, 'Price': price}
                filters = create_filter_map(filter_dict)
                filtered_data = filter_data(data, filters)
                st.dataframe(filtered_data, height=15000, width=10000)
        else:
            with st.spinner('Loading, please wait...'):
                if search_query:
                    data = elastic_search(index, data, search_query)
                st.dataframe(data, height=15000, width=10000)

    # Visualizations
    elif page == 'Visualization':
        visual_type = st.sidebar.selectbox('', ('All', 'Selected'))
        plot_type = st.sidebar.radio(
            'Plot ', ('Word Cloud', 'Distribution Plot', 'Bar Plot'))
        if visual_type == 'All':
            st.subheader(plot_type)
            visual_mapper('all', plot_type)
        elif visual_type == 'Selected':
            feature = st.sidebar.radio(
                'Feature ', ('Service', 'Environment', 'Price'))
            st.subheader(plot_type + " (" + feature + ")")
            visual_mapper('selected', plot_type, feature)


if __name__ == '__main__':
    main()
