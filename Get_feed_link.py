feedly_o = "http://feedly.com/#subscription%2Ffeed%2Fhttp%3A%2F%2Fwww.marketwatch.com%2Frss%2Ftopstories"

def replace_str(my_string,exists,re_with):
    """This function takes a long string, a string to delete, and a string to replace it with.
It returns the new string"""
    my_len = len(my_string)
    str_len = len(exists)
    for i in range(0,my_len):
        if my_string[i:i+str_len]==exists:
            my_string = my_string[0:i]+re_with+my_string[i+str_len:]
            i = i=len(exists)
    return my_string

def find_feed(my_string):
    """This function takes a feedly feed address and produces the raw feed address"""
    prod_slash = replace_str(my_string,"%2F","/")
    prod_colon = replace_str(prod_slash,"%3A",":")
    my_string = prod_colon
    my_len = len(my_string)
    result = "Null"
  
    for i in range(0, my_len - 15):
        end = i+5
        if my_string[i:end] == "/http":
            break
    result = my_string[i+1:]
    return result

print find_feed(feedly_o)
