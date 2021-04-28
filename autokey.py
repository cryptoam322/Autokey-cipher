"""
An idea
Do not expcet this to remain secure against any dedicated adversaries.
"""



def main():
    print_banner()
    exit_on=False
    while exit_on==False:
        prng_type_set=False
        while prng_type_set==False:
            prng_list=get_prng_list_from_user()
            prng_type_set=check_prng_list(prng_list)
        valid_key=False
        while valid_key==False:
            key=get_key_from_user()
            valid_key=check_key(key)
        valid_salt_info=False:
        while valid_salt_info==False:
            salt_info=get_salt_info_from_user()
            valid_key=check_salt_info(salt_info)
        mode=canoncialize_mode(mode)    
    if mode=="encrypt":
        valid_plaintext=False
        while valid_plaintext==False:
            plaintext=get_plaintext()
            valid_plaintext=check_plaintext(plaintext)
        encrypt(prng_list,salt,key,plaintext)



def print_banner():
    """
    Prints the banner lol
    What did you expect?
    """
    print("autokey cipher program")
    print("add additional banner info here lol")
    print("_________________________________________\n"+ #41 char line for thoese that are wondering
          "|                WARNING                |\n"+
          "|  This is insecure and is just a toy.  |\n"+
          "|     Do not use as a secure cipher.    |\n"+#"Yes this is not centered. Sorry can not fix(above line's text is even, this is odd)
          "_________________________________________\n"+)
    print_copyright_info()



def print_copyright_info():
    """
    Prints copyright info
    well it should
    I still need to find one.
    What else did you expect?
    """
    pass



def get_prng_list_from_user():
    """
    Gets user PRNG information(this is not the key)
    """
    print("-Defining PRNG types")
    first_prng=input("1st PRNG?(null generation)\n-->")
    second_prng=input("2nd PRNG(null placement)\n-->")
    third_prng=input("3rd PRNG(keystream)\n-->")
    prng_list=(first_prng,second_prng,third_prng)
    return(prng_list)



def canoncialize_mode(mode):
    """
    Canoncializes mode for the main code
    """
    found_valid_mode=False
    valid_encrypt_modes=("E","e","enc","encrypt","Encrypt","ENCRYPT")
    valid_decrypt_modes=("D","d","dec","decrypt","Decrypt","DECRYPT")
    for valid_encrypt_mode in valid_encrypt_modes:
        if valid_encrypt_mode==mode:
            found_valid_mode=True
            break
    if found_valid_mode==True:
        mode="encrypt"
    for valid_decrypt_mode in valid_decrypt_modes:
        if valid_decrypt_mode==mode:
            found_valid_mode=True
            break
    if found_valid_mode==True:
        mode="decrypt"
    return(mode)



def check_prng_list(list):
    """
    Returns a boolean verifying whether the list of PRNGs are valid.
    Dict structure should be "valid intiator":"valid single type" or "valid initiator":tuple/list("a", "b", "c")
    notes:
    none=no prng
    1=basic type rng, likely insecure
    """
    valid_first_to_second_list={"none":"none","1":["none","1"]}
    valid_second_to_third_list={"none":"1","1":"1"}
    first=list[0]
    second=list[1]
    third=list[2]
    validated_first=False
    validated_second=False
    validated_third=False
    for valid_first_dict_key in valid_first_to_second_dict:
        if valid_first_dict_key==first: #possible match
            validated_first=True
            associated_valid_second_potential_list=valid_first_to_second_dict[first]
            for associated_valid_second in associated_valid_second_potential_list:
                if isinstance(associated_valid_second,type(str()))==True:   #single valid possible prng type
                    if associated_valid_second==second:
                        validated_second==True
                        break
                    else:   #let the default value handle this
                        pass
                else:   #must be a list, time to iterate through it
                    for valid_second in associated_valid_second:
                        if validated_second==second:
                            validated_second==True
                            break
                        else:   #try again
                            pass
        else:   #try again
            pass
    if validated_first==False or validated_second==False:
        return(False)
    for valid_second_dict_key in valid_second_to_third_dict:    #do this again for the second list
        if valid_second_dict_key==second: #possible full match
            #no need to set validated_second true becuase it is already set to true
            associated_valid_third_potential_list=valid_second_to_third_dict[second]
            for associated_valid_third in associated_valid_third_potential_list:
                if isinstance(associated_valid_third,type(str()))==True:   #single valid possible prng type
                    if associated_valid_third==third:
                        validated_third==True
                        break
                    else:   #let the default value handle this
                        pass
                else:   #must be a list, time to iterate through it
                    for valid_third in associated_valid_third:
                        if validated_third==third:
                            validated_thied==True
                            break
                        else:   #try again
                            pass
        else:   #try again
            pass
    if validated_third==True:
        return(True)
    else:
        return(False)



def get_key_from_user():
    """
    Gets user supplied key
    """
    print("-Requesting key")
    key=input("Key?(valid chracters: A-Z,a-z,0-9, ,/)\n-->")
    return(key)



def check_key(key):
    """
    This function exists to allow for future changes in software
    """
    return(check_valid_sequence(key))



def check_valid_sequence(test_sequence):
    """
    Returns a boolean verifying the sequence only contains A-Z,a-z,0-9," ","/" characters(ignore quotes).
    Empty string will return true
    """
    valid_sequence_char=("A","B","C","D","E",
                    "F","G","H","I","J",
                    "K","L","M","N","O",
                    "P","Q","R","S","T",
                    "U","V","W","X","Y",
                    "Z",
                    "a","b","c","d","e",
                    "f","g","h","i","j",
                    "k","l","m","n","o",
                    "p","q","r","s","t",
                    "u","v","w","x","y",
                    "z",
                    "0","1","2","3","4",
                    "5","6","7","8","9",
                    " ","/")    #full symbol set, 64 in total
    if test_sequence==None:
        return(False)   #Nope. ^Reject that^
    i=0
    for test_char in test_sequence:
        for valid_char in valid_sequence_char:
            if valid_char==test_char:
                i=i+1
            else:
                pass
    if i==len(test_sequence):
        return(True)
    else:
        return(False)



def get_salt_info_from_user():
    """
    Grabs salt info from user input and returns a tuple (enable?, salt)
    If the salt is enabled, the first element will be "salt enabled";
    otherwise it will be "salt disabled"
    """
    print("-Requesting salt info")
    salt_enable_valid==False
    while salt_enable_valid==False:
        salt_enable=input("Enable salt?(Y/N only)\n-->")
        if salt_enable=="Y" or salt_enable=="N":
            salt_enable_valid=True
        else:
            pass
    if salt_enable=="Y"
        salt_enable="salt enabled"
        salt=input("Salt?(single string with all valid charecters (A-Z,a-z,0-9, ,/))\n-->")
    else:
        salt_enable="salt disabled"
        salt=None
    salt_info=(salt_enable,salt)
    return(salt_info)



def check_salt_info(salt_info):
    """
    Returns boolean verifying that the salt_info is correct
    """
    salt_enable=salt_info[0]
    salt=salt_info[1]
    if salt_enable!="salt enabled" and salt_enable!="salt disabled":
        return(False)
    elif len(salt)!=64: #not expected size
        return(False)
    else:
        list_of_found_chars=[]
        found_duplicate_char=False
        for char in salt:
            if found_duplicate_char==True:
                break
            for found_char in list_of_found_chars:
                if char==found_char:
                    found_duplicate_char=True
                    break
                else:
                    list_of_found_chars.append(char)
        if found_duplicate_char==True:
            return(False)
        else:
            return(True)



def get_mode_from_user():
    """
    Gets mode from user
    """
    print("-Requesting mode")
    mode=input("Mode?(Encrypt/Decrypt)\n-->")
    return(mode)



def check_mode(mode):
    """
    Returns boolean validating mode
    """
    found_valid_mode=False
    valid_encrypt_modes=("E","e","enc","encrypt","Encrypt","ENCRYPT")
    valid_decrypt_modes=("D","d","dec","decrypt","Decrypt","DECRYPT")
    for valid_encrypt_mode in valid_encrypt_modes:
        if valid_encrypt_mode==mode:
            found_valid_mode=True
            break
    if found_valid_mode==True:
        return(True)
    for valid_decrypt_mode in valid_decrypt_modes:
        if valid_decrypt_mode==mode:
            found_valid_mode=True
            break
    if found_valid_mode==True:
        return(True)
    else:
        return(False)



if __name__ =="__main__":
    main()