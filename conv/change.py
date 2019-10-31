import os 
dir_to = '/home/ubuntu/jay'
for filename in os.listdir(dir_to):
  os.rename(os.path.join(dir_to,filename),os.path.join(dir_to,filename+'.wav'))
