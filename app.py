import streamlit as st
import pandas as pd
import datetime
from utils import get_google_suggestions, get_amazon_suggestions

st.title("Extract Suggestions from Amazon and Google")

with st.form(key="kws_form"):
    kws = st.text_area("Enter the keywords:", "", height=300)
    submit = st.form_submit_button('Submit')

if submit:
    kws = kws.split()
    suggestions = []

    for kw in kws:
        google_suggestions = get_google_suggestions(kw)
        amazon_suggestions = get_amazon_suggestions(kw)
        suggestions += google_suggestions
        suggestions += amazon_suggestions
        
    suggestions = list(set(suggestions))

    st.text_area("Suggestions:",value="\n".join(suggestions), height=300)
    suggestions_df = pd.DataFrame(suggestions, columns=["Suggestions"]).to_csv(index=False)
    st.download_button('Download CSV', data=suggestions_df, file_name=f"suggestions-{datetime.date.today()}.csv")
