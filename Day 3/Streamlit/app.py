import streamlit as st

def main():
    st.title("My Chatbot App")

    # Sidebar for app navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Chatbot", "About"])

    if page == "Home":
        st.header("Welcome to My Chatbot App")
        st.write("This is a simple Streamlit app with a chatbot section.")
        st.write("Use the sidebar to navigate to the Chatbot.")

    elif page == "Chatbot":
        st.header("Chatbot")
        st.write("This is where your chatbot interface will go.")
        
        # Placeholder for chatbot interface
        user_input = st.text_input("You:", "")
        if st.button("Send"):
            # Here you would typically process the user input and get a response
            # For now, we'll just echo the input
            st.text_area("Chatbot:", value=f"You said: {user_input}", height=100)

    elif page == "About":
        st.header("About")
        st.write("This is a simple Streamlit app created as a template for a chatbot interface.")

if __name__ == "__main__":
    main()
