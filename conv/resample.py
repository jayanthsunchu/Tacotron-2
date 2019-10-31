import sox
import os
import argparse

parser = argparse.ArgumentParser(description="Resample Files to suit deep speech decoder.")
parser.add_argument('--inputdir', dest='inputdir', 
help='Input directory for the files to be resampled',
required=True)
parser.add_argument('--outputdir', dest='outputdir', 
help='Output directory for the files resampled',
required=True)


def resample_files(input_dir, output_dir):
  try: 
    for filename in os.listdir(input_dir):
      filename_split = filename.split(".wav")
      print(filename)
      tfm = sox.Transformer()
      tfm.set_output_format(bits=16, rate=22050, channels=1)
      tfm.build(os.path.join(input_dir,filename), os.path.join(output_dir,filename))
  except IOError: 
    print("There was an error trying to read input/output directory.")

if __name__ == "__main__":
  args = parser.parse_args()
  if(os.path.isdir(args.inputdir) and os.path.isdir(args.outputdir)):
    resample_files(args.inputdir, args.outputdir)
  else: 
    print("Input/Output directory doesn't exist")
