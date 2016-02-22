import codecs
import os
import fnmatch

BLOCKSIZE = 1048576 # Or some other, desired size in bytes
BasePath = 'C:/ToConvert' # Base directory location of files to be converted

SourceList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.c')]
    
HeaderList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.h')]
    
ConvertList = SourceList + HeaderList;

for path in ConvertList:
    print path # Print path in case we encounter an error opening this file
    newtarget = path + "_utf"
    
    # Ignore errors if file isn't encoded in shift_jis
    with codecs.open(path, "r", "shift_jis", errors='ignore') as sourceFile:
        with codecs.open(newtarget, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
    os.remove(path)
    os.rename(newtarget, path)
print "Completed encoding conversion" 
