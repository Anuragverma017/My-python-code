email=str("this is a email text for solving the question 3 of chapter 6 this is used for that the email is containing the some keywords that are Make lots of money , buy now , click this ")
if (email.find("Make lots of money") != -1 or email.find("buy now") != -1 or email.find("click this") != -1):
    print("This is a spam email")
else:
    print("This is not a spam email")    