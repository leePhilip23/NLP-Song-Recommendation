import streamlit as st

def main():
    # Set Material Design theme
    set_material_design()

    # Page title
    st.title("NLP News Summarizer")

    # Text input field (search bar)
    input_text = st.text_input("Enter news article title")

    # Submit button
    if st.button("Submit"):
        # Add your NLP summarization logic here
        # For the sake of this example, we'll simply display the entered text
        test_output = "Elon Musk plans to change Twitter's logo to an \"X\" from the blue bird, following his $44 billion acquisition of the platform last year. Musk has a history with the letter \"X,\" evident in his companies SpaceX and X.com. The move has sparked skepticism among Twitter's audience, as previous changes have been divisive, and the platform faces new competition from Meta's Threads app."
        st.subheader("Summary of news article:")
        st.write(test_output)

def set_material_design():
    # Set page configuration
    st.set_page_config(
        page_title="NLP News Summarizer",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inject custom HTML and CSS for Material Design
    st.markdown(
        f'<link href="./styles.css" rel="stylesheet">',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
