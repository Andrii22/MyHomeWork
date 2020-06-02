def filter_words(st):
    while '  ' in st:
        st.replace('  ',' ')
    return st.capitalize()