import codecs
import os
import fnmatch

BLOCKSIZE = 1048576 # or some other, desired size in bytes
BasePath = 'C:/ToConvert' # Base directory location of files to be converted

#These header files are not encoded in SJIS so they need to be skipped
ProblemHeaderList = ["bad_header_1.h", "bad_header_2.h"]

SourceList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.c')]
    
HeaderList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.h')]

for path in SourceList:
    print path #print path in case we encounter an error opening this file
    newtarget = path + "_utf"
    
    with codecs.open(path, "r", "shift_jis") as sourceFile:
        with codecs.open(newtarget, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
    os.remove(path)
    os.rename(newtarget, path)
print "Completed source files" 

for path in HeaderList:
    print path #print path in case we encounter an error opening this file
    newtarget = path + "_utf"
    
    #Get file name from full path and check if it should be skipped
    if os.path.basename(path) in ProblemHeaderList:
        print "...skipped"
        continue
    
    with codecs.open(path, "r", "shift_jis") as sourceFile:
        with codecs.open(newtarget, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
    os.remove(path)
    os.rename(newtarget, path)
print "Completed header files" 
