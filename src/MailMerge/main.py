#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
def main():
    with open("/workspaces/100Days/src/MailMerge/Input/Letters/starting_letter.txt") as letter_file:
        contents = letter_file.read()
    
    with open("/workspaces/100Days/src/MailMerge/Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
        names = [name.strip() for name in names]
    
    for name in names:
        file_name = f"Letter_to_{name}"
        with open(f"/workspaces/100Days/src/MailMerge/Output/ReadyToSend/{file_name}", "w") as output_file:
            custom_letter = contents.replace("[name]", name)
            output_file.write(custom_letter)

main()