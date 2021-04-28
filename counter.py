"""
Quick symbol counter
any not recognized symbols will be counted as other
useful utility for reading 
"""



def main():
    done=False
    valid_sequence_char={"A":0,"B":0,"C":0,"D":0,"E":0,
                        "F":0,"G":0,"H":0,"I":0,"J":0,
                        "K":0,"L":0,"M":0,"N":0,"O":0,
                        "P":0,"Q":0,"R":0,"S":0,"T":0,
                        "U":0,"V":0,"W":0,"X":0,"Y":0,
                        "Z":0,
                        "a":0,"b":0,"c":0,"d":0,"e":0,
                        "f":0,"g":0,"h":0,"i":0,"j":0,
                        "k":0,"l":0,"m":0,"n":0,"o":0,
                        "p":0,"q":0,"r":0,"s":0,"t":0,
                        "u":0,"v":0,"w":0,"x":0,"y":0,
                        "z":0,
                        "0":0,"1":0,"2":0,"3":0,"4":0,
                        "5":0,"6":0,"7":0,"8":0,"9":0,
                        " ":0,"/":0,"other":0}
    while done==False:
        text=""
        final=""
        read_file=input("read file?\n-->")
        if read_file=="Y" or read_file=="y" or read_file=="Yes" or read_file=="YES" or read_file=="yes":
            file_name=input("file?\n-->")
            print("trying file"+file_name+".txt")
            try:
                a=open(str(file_name)+".txt","r")
                text=a.read()
                a.close()
                print("File "+file_name+".txt read")
            except Exception as e:
                print("can not read file "+str(file_name)+".txt")
                print(str(e))
        else:
            text=input("text?\n-->")
        for char in text:
            if char in valid_sequence_char:
                valid_sequence_char[char]=valid_sequence_char[char]+1
            else:
                valid_sequence_char["other"]=valid_sequence_char["other"]+1
        done=input("done?(type in done if true)\n-->")
        if done=="done":
            done=True
        else:
            done=False
    print("printing results")
    final=""
    for key in valid_sequence_char:
        final=final+"Key "+str(key)+": "+str(valid_sequence_char[key])+"\n"
    write_to_file=input("write to file?")
    if write_to_file=="Y" or write_to_file=="Yes" or write_to_file=="y" or write_to_file=="yes" or write_to_file=="YES":
        write_to_file=True
    else:
        write_to_file=False
    if write_to_file==True:
        file_name=input("new file?\n-->")
        try:
            a=open(str(file_name)+".txt","x")
            a.write(final)
            a.close()
            print("Final count written to file "+file_name+".txt")
            print("File "+file_name+".txt read")
        except Exception as e:
            print("can not read file "+str(file_name)+".txt")
            print(str(e))
    else:
        pass
    input()
    print(final)
    input()
    exit()



if __name__=="__main__":
    main()
