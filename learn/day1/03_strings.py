#Replace Double space with single string


ran_str="Hi this is a  random string  that might have multiple  double  spaces. But I'm gonna replace the  double spaces with  single  space."
print(ran_str)
ran_str= ran_str.replace("  ", " ")
print(ran_str + "And now the double spaces are replaced.")