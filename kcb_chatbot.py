## 1. import libaries
import streamlit as st

## 2. title and description

st.title("KCB BANK CHATBOT")
st.write("Welome to KCB Bank Chatbot. How can I assist you today?")

## 3. define your dictionary of responses

bank_responses = {
    "greeting": {
        "hello": "Hello! Welcome to KCB chatbot. How can I assist you?",
        "hi": "Hello! Welcome to KCB chatbot. How can I assist you?",
        "hey": "Hello! Welcome to KCB chatbot. How can I assist you?",
        "good morning": "Good morning! How can I assist you today?",
        "thank you": "You're welcome! How else can I assist you?",
        "thanks": "You're welcome! How else can I assist you?"
    },

    "account_balance": {
        "what is my account balance": "Please provide your account number to check your balance.",
        "check my balance": "Sure. Kindly enter your account number.",
        "how much money do i have": "Please share your account number.",
        "i don't know my account number": "No worries. Please visit the nearest branch for assistance."
    },

    "loan_information": {
        "what loans do you offer": "We offer personal, home, car, and business loans.",
        "how can i apply for a loan": "You can apply online or visit the nearest branch.",
        "what is the loan interest rate": "Loan interest rates vary depending on the loan type."
    },

    "branch_location": {
        "where is your branch": "Please share your city name to find the nearest branch.",
        "nearest branch": "Kindly provide your location."
    }
}
## 4. create messege history
## st.session_state this is the fucntiom that allow us tos store the message history
## is the box that used to store your message history

if "message" not in st.session_state:
    st.session_state.message = []
## 5.  display my chat histort

for sms in st.session_state.message:
    st.write(sms)
## 6. define user input
user_input = st.chat_input("type your message")

## 7. check the user input
if user_input:
    user_text = user_input.lower().strip()

## 8. define the user response
    response = None
    if user_text in bank_responses["greeting"]:
        response = bank_responses["greeting"][user_text]
    elif user_text in bank_responses["account_balance"]:
        response = bank_responses["account_balance"][user_text]
    elif user_text in bank_responses["loan_information"]:
        response = bank_responses["loan_information"][user_text]
    elif user_text in bank_responses["branch_location"]:
        response = bank_responses["branch_location"][user_text]
    elif user_text == "bye":
        response = "Good bye welcome to KCB bank chatbot service for more information please ask"
    else:
        response = " welcom to KCB bank we can assist you with account information,loan infomation,branch loaction and general queries"
## 9. save the response
    st.session_state.message.append(f"user: {user_input}")
    st.session_state.message.append(f"Bot: {response}")
    st.rerun()
## 10. refresh your chat
if st.button("restart chat"):
    st.session_state.message = []
    st.rerun()