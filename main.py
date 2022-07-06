csby = 1970

#Greets user
print("Hello! I'm CyHelp. ")
name = input("What's your name? \n")
print(f'Nice to meet you, {name}. \n')

#Recounts start of Cybersecurity
cy = int(input('What year is it? \n'))
time = cy - csby
print(f"Wow! That's {time} years since cybersecurity began!\n")
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks.")
input('Press enter to continue.')


#Describes Cybersecurity
print('Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.')
print('These people can be governments, individuals, companies, community organizations, and hackers. \n')
input('Press enter to continue.')

#Introduces CIA Triad
ans = input('Would you like to learn about the CIA triad? /n Type yes or no.')
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability.")


#Explains pillars of CIA Triad
topic = str(input("Which part of the CIA triad would you like to learn more about? Enter the lowercase letter of the following options: \n (c) confidentiality, (i) integrity, (a) availability, or (n) for none of the above"))
if topic.lower() == 'c':
  print('Confidentiality makes sure data is private. \n')
elif topic.lower() == 'i':
  print('Integrity makes sure data has not been tampered with and can be trusted. \n')
elif topic.lower() == 'a':
  print('Availability makes sure authorized people can access the data. \n')
elif topic.lower() == 'n':
  print('okay. \n')
else:
  Print("That's not an option. Please choose one of the options listed.")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")