def format_name(f_name,l_name):
    if not f_name and not l_name:
        return 'No return values for empty string'

    formatted_fname=f_name.title()
    formatted_lname=l_name.title()
    return formatted_fname,formatted_lname

first=input("Enter first name")
last=input("Enter second name")
print(format_name(first,last))