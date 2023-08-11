import streamlit as st
import time

# Hardcoded credentials
USERNAME = 'user'
PASSWORD = 'password'

# Categories
CATEGORIES = ['Baby Care', 'Supplements', 'Vaccines', 'Oral Care', 'Pet Care']

col1, col2, col3 = st.columns([1,2,1])
css = st.markdown('''
            <style>
            img {
                margin: auto;
                position: relative;
                left: 50%;
                top: 50%
            }
             .stChatMessage {
                background-color: #ffbd4529
            }
            .stChatMessage:nth-child(2n) {
                background-color: #ff004412
            }
           
            </style>
        ''', unsafe_allow_html=True)

def login() -> object:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username == USERNAME and password == PASSWORD:
        st.session_state.logged_in = True
        st.success("Logged in successfully. Loading...")
        time.sleep(2)
        st.experimental_rerun()
    elif username == '' or password == '':
        return
    else:
        st.error("Invalid credentials")

def main_app():
    st.title("1. Select Category")
    category = st.selectbox('Select from the list:', CATEGORIES)

    st.title('2. Ask Bob')

    chat_container = st.container()

    with chat_container:
        with st.chat_message("assistant"):
            st.write(f"Hi, I'm Bob. How can I assist you with {category}?")

        options = [
            '❓ Ask Bob a Question',
            '🗒️ Get Suggested Questions',
            '🚀 Explore Insights and Analysis'
        ]

        option = st.radio('Choose an option:', options)

        if option == '❓ Ask Bob a Question':
            prompt = st.chat_input('Type your question here...')
            if prompt:
                with chat_container:
                    with st.chat_message("user"):
                        st.write(prompt)
                    with st.chat_message("assistant"):
                        st.write('Answer to your question about ' + category + ': ...')


        elif option == '🗒️ Get Suggested Questions':
            topic_question = st.selectbox('Select Topic:', [
                'Value perception',
                'Quality',
                'Smell',
                'Type',
                'Sustainability'
            ])

            selected_question = st.radio('Choose a question:', [
                'What are the most common words or phrases used by customers to describe the value perception of the product/service?',
                'How do customers perceive the pricing of the product/service? Is it considered affordable or expensive?',
                'Are there any specific promotions or discounts that customers mention in their reviews? How do these affect their perception of value?',
                'Do customers mention any specific features or benefits that they find particularly valuable in relation to the price they paid?',
                'Are there any negative comments about the value perception of the product/service? If so, what are the main reasons for this perception?'
            ])

            submit_question = st.button('Submit Question')

            if submit_question and selected_question:
                with chat_container:
                    with st.chat_message("user"):
                        st.write(selected_question)
                    with st.chat_message("assistant"):
                        with st.spinner(text='Working on it...'):
                            time.sleep(3)
                            st.write('Answer to your question: ...')

        elif option == '🚀 Explore Insights and Analysis':
            analysis_type = st.selectbox('Select Analysis Type:', [
                'R&R: Topic pros and cons',
                'R&R: Topic competitor compare',
                'R&R: Topic customer barriers',
                'R&R: Average customer',
                'R&R: Audience target',
                'R&R: Buyer Persona',
                'R&R: Brand recommendations'
            ])

            topic_insight = st.selectbox('Select Topic:', [
                'Recommendation',
                'Effect',
                'When',
                'Quality',
                'Male',
                'Female'
            ])

            submit_insights = st.button('Submit')

            if submit_insights and analysis_type and topic_insight:
                response = '''
                As an analyst exploring the rating and reviews of newborn diapers, here are some pros and cons of a type based on the reviews provided:

                **Pros:**
                - Soft and comfortable material
                - Good fit for some babies
                - Some users found the design to be cute and attractive

                **Cons:**
                - Thin and flimsy material compared to other brands
                - Tab ripping issues reported by some users
                - Chemical smells or brown spots reported by some users
                - Some users reported diaper rash after using this brand
                - Quality and quantity issues (less diapers per package or overall lower quality compared to previous purchases or other brands)

                It's important to keep in mind that each baby is different and may react differently to each brand, so these are just some general observations based on the reviews provided.'''

                with chat_container:
                    with st.chat_message("assistant"):
                        with st.spinner(text='Working on it...'):
                            time.sleep(3)
                            st.write(response)

# Initialization of login state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state.logged_in:
    with col2:
        st.image('logo.png', width=150)

    main_app()
else:
    with col2:
        st.image('logo.png', width=150)
        
    st.title("Login")
    login()
