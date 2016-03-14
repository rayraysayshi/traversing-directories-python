# If you just want to read or write a file see open(), 
# if you want to manipulate paths,
import os 

print "This program traverses the directory you choose for a string you seek."
print "Enter the directory like so: /Users/raymondklucik/Documents/dev/python/traverse"
input_dir = raw_input("Enter the directory path to be searched: ")
search = raw_input("Enter word to be searched: ")

array = {}
s = "/"
list = []

# Generate the file names in a directory tree by walking 
# the tree either top-down or bottom-up.
# for root, dirs, files in os.walk("/Users/raymondklucik/Documents/dev/python/traverse"):
for root, dirs, files in os.walk(input_dir):
	for dir in dirs:
		print "dir: " + dir 
		list.append(dir)
		i = 0 
		for file in files:
			# method .endswith	
			if file.endswith(".txt"):
				# print(os.path.join(root, file))
				# 
				f = open(os.path.join(root, file), 'r')
				for line in f:
					if search in line:						
						i += 1
						break  
		obj = s.join(list)				
		array[obj] = i 
		print i 

print array

