import os

file_path = r"C:\Users\HP\Desktop\imp documents"

Q = int(input("Press 1 to convert in png or 2 to convert in jpg : "))

if 	Q == 1:
	os.chdir(file_path)
	i= 0
	for file in os.listdir():
		i+=1
		filename, fileext = os.path.splitext(file)

		if fileext == ".jpg": 
			fileext = ".png"
		elif fileext == ".jpeg":
			fileext = ".png"
		elif fileext == ".JPG":
			fileext = ".png"
		elif fileext == ".JPEG":
			fileext = ".png"

		else:
			continue
			
		newname = '{}{}'.format(filename,fileext)

		os.rename(file , newname)
		print(i,"Done")

elif Q==2:
	os.chdir(file_path)
	i= 0
	for file in os.listdir():
		i+=1
		filename, fileext = os.path.splitext(file)

		if fileext == ".png": 
			fileext = ".jpg"

		else:
			continue
			
		newname = '{}{}'.format(filename,fileext)

		os.rename(file , newname)
		print(i,"Done")

else:
	print("Invail extension")
	


