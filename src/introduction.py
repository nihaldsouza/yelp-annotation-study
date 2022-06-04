import streamlit as st


def team_members():
    st.sidebar.subheader("Group 6 Team Members:")
    st.sidebar.markdown(
        """
        - Jiajing Li
        - Nihal D'Souza
        - Shengjie Zhang
        - Zhiyi Li
        """
    )
    st.sidebar.subheader("Under the guidance of:")
    st.sidebar.markdown(
        """
        - Prof. Jungyeul Park
        - Prof. Garrett Nicolai
        - Mike Qiu (TA)
        """
    )

def intro_content():
    st.title("Introduction")
    st.write("The dataset that we have selected is Yelp Restaurant reviews in Vancouver. \
        The goal of our project is to build a corpus that can be used to train a question answering system. \
            The corpus can also be used to search and filter the restaurant reviews based on the questions that users are interested in.")

    st.markdown(
        """
        The features that we initially came up with were price of food, quality of food, service, environment, \
            party/family friendly, reservation needed or not, vegetarian food, free parking, serves alcohol or not. \
                However, due to the limitation of time and resources, we have only included service, environment, and \
                    price into our project. The labels that we have given them are:
        - **service**: positive, neutral, negative, undefined
        - **environment**: good, moderate, bad, undefined
        - **price of food**: expensive, reasonable, cheap, undefined
    """)

    st.subheader("Data")

    st.write("We collected the raw data from Yelp and filtered it to include 400 of the most useful restaurant reviews in Vancouver. \
         The average length of the reviews included is 308 words.")

    st.subheader("Annotations")

    st.write("For each review, we annotate it with related labels of the three questions (service, environment, price). \
        We hired 2 Amazon Mechanical Turk workers to do the annotation independently for each question. \
            To solve inconsistency among different annotators, we perform expert annotation for reviews that have inconsistent labels \
                and use our labels as the final annotation labels of these reviews.")

    st.subheader("App")

    st.markdown(
        """
        Our app contains three main pages: 
        - Introduction
        - Data (Search, Annotation Filters)
        - Visualization (Wordcloud, distribution plot, and bar plot)
        Detailed instructions about how to use them can be found on the peer-review Instructions.
        """)
    
    st.markdown("**A note on Wordcloud**: Since a review may mention more than one question, \
        there are many overlapping reviews for different features and the word cloud may look similar. \
            However, if you observe carefully, you would find that the size of the words are distinct in each word cloud. \
                For example, the word 'price' is larger in the word cloud of 'price' feature than that of 'environment' or 'service'.")

    
    