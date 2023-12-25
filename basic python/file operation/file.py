import os

# *Creating the new directory
# os.mkdir('rakib')

# *Using os.makedirs()
'''Python-এ os.makedirs() পদ্ধতি পুনরাবৃত্তিমূলকভাবে একটি ডিরেক্টরি তৈরি করতে ব্যবহৃত হয়। এর মানে লিফ ডিরেক্টরি তৈরি করার সময় যদি কোনও মধ্যবর্তী-স্তরের ডিরেক্টরি অনুপস্থিত থাকে, os.makedirs() পদ্ধতি সেগুলি তৈরি করবে।'''
# directory = "rakib"
# parent_dir = "D:/Pycharm projects/"
# path = os.path.join(parent_dir, directory) 
# os.makedirs(path) 

# *Removing the file
# os.remove('./file.py')

# *Deleting directory
# os.rmdir(directory name)
# os.rmdir('rakib')

# *Renaming the file
# rename(current-name, new-name)
# os.rename('./file.py','r.py')
# *The getcwd() method
# This method returns the current working directory.
print(os.getcwd())

# *Changing the current working directory
# The chdir() method is used to change the current working directory to a specified directory.
# os.chdir('rakib')
# print(os.getcwd())

# *Listing out Files and Directories with Python
"""method in Python is used to get the list of all files and directories in the specified directory. If we don’t specify any directory, then the list of files and directories in the current working directory will be returned."""

# path = '/'
# dir_list = os.listdir(path=path)
# print(dir_list)

# os.path.exists()
'''এই পদ্ধতিটি প্যারামিটার হিসাবে ফাইলের নাম পাস করে একটি ফাইল বিদ্যমান আছে কি না তা পরীক্ষা করবে। OS মডিউলের PATH নামে একটি সাব-মডিউল রয়েছে যা ব্যবহার করে আমরা আরও অনেক কাজ করতে পারি।'''
result = os.path.exists("file_name") 

# os.path.getsize(): এই পদ্ধতিতে, পাইথন আমাদের ফাইলের আকার বাইটে দেবে। এই পদ্ধতিটি ব্যবহার করার জন্য আমাদের প্যারামিটার হিসাবে ফাইলের নাম পাস করতে হবে।
size = os.path.getsize("./file.py")
print("Size of the file is", size," bytes.")