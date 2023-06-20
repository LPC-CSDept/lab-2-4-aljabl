def main():

    #assign variables
    original_str = 'Python Programming'

    #extract 'Python' from original string with index slicing
    sub1 = original_str[:6]

    #extract 'Programming' from original string with index slicing
    sub2 = original_str[7:18]

    #merge two substrings and save it to variable "merged_str"
    merged_str = sub2 + ' ' + sub1
    
    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
