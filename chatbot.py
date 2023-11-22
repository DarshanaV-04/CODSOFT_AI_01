#the needed libraries for the chatbot application to be imported
import re,random;
import nltk;
from nltk.stem import WordNetLemmatizer;

#the class to store the response of the bot for negative and quitting the chat 
class chatBot:
    neg_commands=("Nope","NO","Not yet ready","Sorry it's too late","Nahi");
    quit_commands=("Quit","Its over","Thank you for your response","Bye","Exit");
#to understand the human commands and fit it into certain rules
    def __init__(self):
        self.chatBot_replies={
            'product_related_queries':r'product|item',
            'price_related_queries':r'price|amount|rate',
            'support_related_queries':r'technical|support|issue',
            'billing_related_queries':r'bill|bill id|receipt',
            'delivery_related_help':r'delivery|time|address',
            'booking_ticket':r'booking|movie|theatre',
            'advice':r'frustration|loneliness|alone',
            'love':r'heart-break|breakup|failure',
            'career':r'successful|future|happiness'
        }
    def greet(self):
        print("Hello!Welcome to chatbot Iam bot Darshana\n")
        name=input("May I know your name please\n")
        greet_statement=input(f"Hi {name} How may I help you?\n")
#checking if the response is in negative or quit commands
        if greet_statement in self.neg_commands:
            print("Have a nice day")
            return
        self.chat()
#function for exiting the chat based on the response from user
    def exit(self,response):
        for chat in self.quit_commands:
            if response==chat:
                print("Glad to have your response!Have a exciting day .")
#function for checking any negative commands from the user
    def neg(self,response):
        for chat in self.neg_commands:
            if response==chat:
                ("Sorry .I cant understand the context you are asking for")

#to get the input from user
    def chat(self):
        response=input("Can you tell me your requests").lower()
#to check whether it is not in quit_commands
        while not  self.exit(response):
            response=input(self.rules(response))
#function to check for rules in the text given by the user
    def rules(self,response):
    #regex_pattern is used to identity the match found in response from the user and reules which is built_in in the chatbot
        for match,regex_pattern in self.chatBot_replies.items():
        #searching the response in the regex_pattern
            pattern_found=re.search(regex_pattern,response)
            if pattern_found and match=="product_related_queries":
                return self.product_related_queries()
            elif pattern_found and match=="price_related_queries":
                return self.price_related_queries()
            elif pattern_found and match=="support_related_queries":
                return self.support_related_queries()
            elif pattern_found and match=="billing_related_queries":
                return self.billing_related_queries()
            elif pattern_found and match=="delivery_related_help":
                return self.delivery_related_help()
            elif pattern_found and match=="booking_ticket":
                return self.booking_ticket()
            elif pattern_found and match=="advice":
                return self.advice()
            elif pattern_found and match=="love":
                return self.love()
            elif pattern_found and match=="career":
                return self.career()
    #if no match is found another function is returned
        return self.no_match()
#statements to be written if user input matches with product_related_queries
    def product_related_queries(self):
        replies=("Thank you for choosing our product which is highly rated\n",
                 "This product is a customer friendly product\n",
                 "For further details visit our corressponding website\n" )
        return random.choice(replies)
#statements to be written if user input matches with price_related_queries
    def price_related_queries(self):
        replies=("The price of the product is in deal offer\n",
                 "The product is worth the cost to buy\n",
                 "You have a great discount for the product\n")
        return random.choice(replies)
#statements to be written if user input matches with support_related_queries
    def support_related_queries(self):
        replies=("For technical support you can contact the customer care in the website\n",
                 "Your issue will be resolved by our support team in a short period of time\n")
        return random.choice(replies)
#statements to be written if user input matches with billing_related_queries
    def billing_related_queries(self):
        replies=("The bill receipt will be sent to your registered mail-id\n",
                 "The bill invoice is present in your app\n",
                 "The discount offer is available in your bill\n",
                 "The bill-id is in your invoice\n")
        return random.choice(replies)
#statements to be written if user input matches with delivery_related_help
    def delivery_related_help(self):
        replies=("The delivery of the product is delayed\n",
                 "The product will be delivered to the appropriate address\n",
                 "The tracking of the product to be delivered is available in the website\n")
        return random.choice(replies)
    def booking_ticket(self):
        replies=("The theatre nearby is available in the website\n",
                 "The available slot of ticket is shown in the website\n",
                 "The booking is going to get over\n")
        return random.choice(replies)
    def advice(self):
        replies=("Get motivated from your inspirers\n",
                 "Don't leave hope at anypoint\n ",
                 "Every failure is fight step for success")
        return random.choice(replies)
    def love(self):
        replies=("Don't get broken for your failures\n",
                 "He/She doesnot deserve you\n",
                 "You deserve someone better\n","Move on with your life\n")
        return random.choice(replies)
    def career(self):
        replies=("Career is very important in your life\n",
                 "Don't leave your career for anyone\n",
                 "Be successful in your life\n",
                 "Come out from your obstacle\n")
        return random.choice(replies)
#function if no match is found in between the pattern and user_input
    def no_match(self):
        replies=("Sorry I cant understand your query\n"
                 ,"Can  you repeat your request once again\n",
                 "Due to technical issue I cant assist you\n")
        return random.choice(replies)
Bot=chatBot()
Bot.greet()




