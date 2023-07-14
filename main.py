def chatbot():
    print("Chatbot: Hi there!")
    while True:
        user_input = input("User: ").lower()

        if 'hello' in user_input:
            print("Chatbot: Hello, how are you? How can I help you today?")

        elif "what is year up's mission" in user_input or "what is year ups mission" in user_input:
            print("Chatbot: Year Up's mission is to close the Opportunity Divide by ensuring that young adults gain"
                  " the skills, experiences, and support that will empower them to reach their potential"
                  " through careers and higher education.")

        elif 'what is year up' in user_input:
            print("Chatbot: Year Up is a non-profit organization with a one of a kind mission.")

        elif 'what are the requirements to join year up' in user_input:
            print(
                "Chatbot: Year Up's eligibility requirements are that you are a U.S citizen, permanent resident, or have employment authorization card. You must be of age 18 to 29 and you have not obtained a bachelor's degree.")

        elif 'thank you for that information' in user_input:
            print("Chatbot: You're welcome!")

        elif 'goodbye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase it or ask something else?")


if __name__ == "__main__":
    chatbot()
