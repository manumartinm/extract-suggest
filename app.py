import streamlit as st
import pandas as pd
import datetime
from utils import get_google_suggestions

st.title("Extract Google Suggest based on the Kws")

with st.form(key="kws_form"):
    kws = st.text_area("Enter the keywords:", "", height=300)
    submit = st.form_submit_button('Submit')

if submit:
    kws = kws.split()
    suggestions = []

    for kw in kws:
        google_suggestions = get_google_suggestions(kw)
        suggestions += google_suggestions
        
    st.text_area("Google Suggestions:", value="\n".join(suggestions), height=300)
    google_suggestions_df = pd.DataFrame(suggestions, columns=["Suggestions"]).to_csv(index=False)
    st.download_button('Download CSV', data=google_suggestions_df, file_name=f"google_suggestions-{datetime.date.today()}.csv")
