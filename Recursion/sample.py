s= "A man, a plan, a canal: Panama"

low = s.lower()
cleaned_str = "".join(filter(str.isalnum, low))
        
print(cleaned_str)