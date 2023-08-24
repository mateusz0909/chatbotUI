import streamlit as st

import time


# hotjar_js = ''s'
#       <script>
#     (function(h,o,t,j,a,r){
#         h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
#         h._hjSettings={hjid:3625184,hjsv:6};
#         a=o.getElementsByTagName('head')[0];
#         r=o.createElement('script');r.async=1;
#         r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
#         a.appendChild(r);
#     })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
# </script>
#     '''
# st.components.v1.html(hotjar_js)


class AIChat:
    USERNAME = 'user'
    PASSWORD = '1234'
    CATEGORIES = ['Baby Care', 'Supplements', 'Vaccines', 'Oral Care', 'Pet Care']

    def __init__(self):
        col1, col2, col3 = st.columns([1, 2, 1])
        self.css()
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False

        if st.session_state.logged_in:
            with col2:
                st.image('logo.png', width=150)
            self.main_app()
        else:
            with col2:
                st.image('logo.png', width=150)
            st.title("Login")
            self.login()

    def css(self):
        st.markdown('''
            <style>
            img {
                display: block;
                margin-left: 50%;
                margin-right: auto;
                width: 50%;
                margin-bottom: 3em;
                border-bottom: 2px solid white;
            }
            .stChatMessage {
                background-color: #ffbd4529;
            }
            .stChatMessage:nth-child(2n) {
                background-color: #ff004412;
            }
            </style>
        ''', unsafe_allow_html=True)

    def login(self):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if username == self.USERNAME and password == self.PASSWORD:
            st.session_state.logged_in = True
            st.success("Logged in successfully. Loading...")
            time.sleep(2)
            st.experimental_rerun()
        elif username == '' or password == '':
            return
        else:
            st.error("Invalid credentials")

    # main app
    def main_app(self):
        st.title("1. Select Category")
        category = st.selectbox('Select from the list:', self.CATEGORIES)

        st.title('2. Ask AI ✨')

        chat_container = st.container()

        with chat_container:
            with st.chat_message("assistant"):
                st.write(f"Hi, I'm AI Assistant. How can I assist you with {category}?")

            options = [
                '❓ Ask a Question',
                '🚀 Explore Insights'
            ]

            option = st.radio('Choose an option:', options)

            if option == '❓ Ask a Question':
                prompt = st.chat_input('Type your question here...')
                if prompt:
                    with chat_container:
                        with st.chat_message("user"):
                            st.write(prompt)
                        with st.chat_message("assistant"):
                            st.write('Answer to your question about ' + category + ': ...')

            #
            # elif option == '🗒️ Get Suggested Questions':
            #     topic_question = st.selectbox('Select Topic:', [
            #         'Value perception',
            #         'Quality',
            #         'Smell',
            #         'Type',
            #         'Sustainability'
            #     ])
            #
            #     selected_question = st.radio('Choose a question:', [
            #         'What are the most common words or phrases used by customers to describe the value perception of the product/service?',
            #         'How do customers perceive the pricing of the product/service? Is it considered affordable or expensive?',
            #         'Are there any specific promotions or discounts that customers mention in their reviews? How do these affect their perception of value?',
            #         'Do customers mention any specific features or benefits that they find particularly valuable in relation to the price they paid?',
            #         'Are there any negative comments about the value perception of the product/service? If so, what are the main reasons for this perception?'
            #     ])
            #
            #     submit_question = st.button('Submit Question')
            #
            #     if submit_question and selected_question:
            #         with chat_container:
            #             with st.chat_message("user"):
            #                 st.write(selected_question)
            #             with st.chat_message("assistant"):
            #                 with st.spinner(text='Working on it...'):
            #                     time.sleep(3)
            #                     st.write('Answer to your question: ...')

            elif option == '🚀 Explore Insights':
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


if __name__ == "__main__":
    # with streamlit_analytics.track(unsafe_password="bng1234"):
        app = AIChat()
