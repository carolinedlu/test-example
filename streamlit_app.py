import streamlit as st

st.title("Ask A Source: Thomas More's 'The History of Richard III'")
col1, col2 = st.columns([2,3])
with col1:
    #method 1
    pdf_url = 'https://github.com/Dr-Hutchinson/prompt_chain_0/blob/main/annotated_full_text.pdf'
    pdf_display = F'<iframe src="{pdf_url}" width="700" height="700" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    #method 2
    st.markdown("""
    <embed src="https://thomasmorestudies.org/wp-content/uploads/2020/09/Richard.pdf" width="800" height="800">
    """, unsafe_allow_html=True)

    st.markdown("""
        <embed src="https://thomasmorestudies.org/wp-content/uploads/2020/09/Richard.pdf" width="800" height="800">
        """, unsafe_allow_html=True)

    st.markdown("""
    <embed src="https://raw.githubusercontent.com/Dr-Hutchinson/prompt_chain_0/c2f3795f25683fb194e11072abb9d586964896a2/annotated_full_text.pdf" width="800" height="800">
    """, unsafe_allow_html=True)
