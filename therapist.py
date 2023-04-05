import random

# Dictionaries to store responses and actions for different keywords
responses = {"default": ["Ich verstehe. Wie geht es Ihnen jetzt?",
                         "Das klingt wirklich schwierig. Möchten Sie darüber sprechen?",
                         "Vielen Dank, dass Sie das mit mir geteilt haben. Wie kann ich Sie unterstützen?"],
             "hotline": ["Hier sind einige Hotlines, die Sie anrufen können, um sofortige Unterstützung zu erhalten:",
                         "1. Telefonseelsorge: 0800-1110111",
                         "2. Nummer gegen Kummer für Kinder und Jugendliche: 116111"],
             "resource": ["Hier sind einige Ressourcen, die für Sie hilfreich sein könnten:",
                          "1. Deutsche Depressionshilfe: https://www.deutsche-depressionshilfe.de/",
                          "2. Online-Selbsthilfe-Programm gegen Depressionen: https://www.selbsthilfe-depressionen.de/"],
             "suicide": ["Selbstmord ist keine Lösung."]}

actions = {"bye": "Vielen Dank, dass Sie mit mir gesprochen haben. Denken Sie daran, Sie sind nicht allein.",
           "language": "Ich verstehe, dass Sie eine andere Sprache sprechen. Wie kann ich helfen?",
           "share": "Möchten Sie Ihre Erfahrungen mit anderen teilen oder auf externe Ressourcen wie Foren oder Chatrooms verweisen?",
           "ai": "Ich kann Ihnen personalisierte Vorschläge und Empfehlungen geben. Soll ich das tun?"}

# List of questions to ask the user
questions = ["Können Sie mir mehr darüber erzählen?",
             "Wie lange haben Sie dieses Problem schon?",
             "Wie hat sich Ihr Leben aufgrund dieses Problems verändert?",
             "Haben Sie jemanden, mit dem Sie darüber sprechen können?",
             "Gibt es Dinge, die Sie tun, um sich in schwierigen Zeiten zu beruhigen?"]

# Define a function to handle the therapy session
def virtual_therapist():
    
    # Prompt the user to share their concerns
    user_input = input("Hallo, wie kann ich Ihnen heute helfen? ")
    
    # Provide a supportive response to the user's input
    print(random.choice(responses["default"]))
    
    # While loop to continue the conversation until the user is ready to end it
    while True:
        
        # Prompt the user for more information and provide appropriate guidance
        user_input = input()
        
        if user_input.lower() in ["quit", "exit", "goodbye", "bye"]:
            print(actions["bye"])
            break
        
        # Check for keywords and execute corresponding actions
        elif "hotline" in user_input.lower():
            for response in responses["hotline"]:
                print(response)
        elif "resource" in user_input.lower():
            for response in responses["resource"]:
                print(response)
        elif "suicide" in user_input.lower():
            for response in responses["suicide"]:
                print(response)
        elif "language" in user_input.lower():
            print(actions["language"])
        elif "share" in user_input.lower():
            print(actions["share"])
        elif "ai" in user_input.lower():
            print(actions["ai"])
        # If no keyword is found, ask a question to focus the conversation
        else:
            print(random.choice(questions))
            
# Call the function to begin the therapy session
virtual_therapist()
