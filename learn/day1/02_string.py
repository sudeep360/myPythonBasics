#This is a letter templete thet uses replace method


statement='''Hello <|NAME|>
You are selected! Hurrah!!
<|DATE|>'''
name=input("Enter your name: ")
date=input("Enter date: ")
statement=statement.replace("<|NAME|>", name)
statement=statement.replace("<|DATE|>", date)
print(statement)