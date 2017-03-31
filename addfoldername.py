import os, sys

def main(in_directory):
	for dir_name, sub_dirs, file_names in os.walk(in_directory):
		dir_path = os.path.dirname(dir_name)
		folder_name = os.path.basename(dir_name)
		for file_name in file_names:
			source = os.path.join(dir_path, folder_name,file_name)
			destination = os.path.join(dir_path, folder_name, folder_name+"_"+file_name)
			print source + " --> " + destination
			os.rename(source, destination)

if __name__ == "__main__":
	main(sys.argv[1])