import os

file_path = r"<directory path>"


def rename_file(file_path):
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

rename_file(file_path)

