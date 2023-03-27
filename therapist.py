# Import necessary libraries
import random

# Create a list of potential responses to user input
responses = ["I'm sorry to hear that. How are you feeling right now?",
             "That sounds really tough. Would you like to talk about it?",
             "Thank you for sharing that with me. How can I support you?"]

# Define a function to handle the therapy session
def virtual_therapist():
    
    # Prompt the user to share their concerns
    user_input = input("Hello, how can I assist you today? ")
    
    # Provide a supportive response to the user's input
    print(random.choice(responses))
    
    # While loop to continue the conversation until the user is ready to end it
    while True:
        
        # Prompt the user for more information and provide appropriate guidance
        user_input = input()
        
        if user_input.lower() in ["quit", "exit", "goodbye", "bye"]:
            print("Thank you for sharing with me. Remember, you're not alone.")
            break
            
        elif "hotline" in user_input.lower():
            print("Here is a list of hotlines you can call for immediate assistance:")
            print("1. National Suicide Prevention Lifeline: 1-800-273-TALK (8255)")
            print("2. Crisis Text Line: Text HOME to 741741")
            
        elif "resource" in user_input.lower():
            print("Here are some resources that might be helpful to you:")
            print("1. National Alliance on Mental Illness (NAMI): https://www.nami.org/")
            print("2. Substance Abuse and Mental Health Services Administration (SAMHSA): https://www.samhsa.gov/")
        
        elif "suicide" in user_input.lower():
            print("Suicide is not a Way")
            
        else:
            print("I hear you. Can you tell me more about what you're experiencing?")
            
# Call the function to begin the therapy session
virtual_therapist()
