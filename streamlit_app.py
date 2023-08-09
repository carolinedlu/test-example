import streamlit as st
import urllib

uploaded_file = st.file_uploader("Choose a file")

def displayPDF(file):
    # Opening file from file path. this is used to open the file from a website rather than local
    with urllib.request.urlopen(file) as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

displayPDF("example.pdf")
# if uploaded_file is not None:
#     # # To read file as bytes:
#     # bytes_data = uploaded_file.getvalue()
#     # st.write(bytes_data)

#     # # To convert to a string based IO:
#     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     # st.write(stringio)

#     # # To read file as string:
#     # string_data = stringio.read()
#     # st.write(string_data)

#     # # Can be used wherever a "file-like" object is accepted:
#     # dataframe = pd.read_csv(uploaded_file)
#     # st.write(dataframe)

#     with open(uploaded_file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#         # pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
#         pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#         st.markdown(pdf_display, unsafe_allow_html=True)
#     # Displaying File
#     # st.markdown(pdf_display, unsafe_allow_html=True)
#     # try: 
#     #     # Opening file from file path
#     #     base64_pdf = base64.b64encode(uploaded_file).decode('utf-8')
#     # except Exception as e: 
#     #     raise ValueError(f"Can't encode the file. Details: {e}")

#     # # Embedding PDF in HTML
#     # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="1000" type="application/pdf"></iframe>'
#     # # Displaying File
#     # st.markdown(pdf_display, unsafe_allow_html=True)

# # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000px" type="application/pdf"></iframe>'
# # st.markdown(pdf_display, unsafe_allow_html=True)
