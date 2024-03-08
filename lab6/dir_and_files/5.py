#Write a Python program to write a list to a file.
liverpool = ['Jurgen Klopp', 'Mohamed Salah', 'Diogo Jota', 'Darwin Núñez']
file = open('liverpool.txt','w')

for players in liverpool:
	file.write(liverpool+"\n")
    
file.close()