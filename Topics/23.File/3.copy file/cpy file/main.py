#copyfile()= copies contents of a file
#copy() = copyfile() + permission mode+destination ca be a directory
#copy2()= copy() + copies metadata (fie's creation and modification times)

import shutil
shutil.copfile('test.txt','copy.txt')  #(source , destination)