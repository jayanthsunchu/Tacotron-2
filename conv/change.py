import os 
dir_to = 'C:\\taco\\siri\\'
for filename in os.listdir(dir_to):
  os.rename(os.path.join(dir_to,filename),os.path.join(dir_to,filename+'.wav'))
