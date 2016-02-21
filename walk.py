from translate import Translator
import chardet
import codecs
import fnmatch
import os, os.path

def HasUnicode(InputString):
    encoding = chardet.detect(InputString.encode('utf-8'))
    if encoding['encoding'] == 'ascii':
        return False
    else:
        return True
        
def TranslateLine(InputString):
    #clean up input string for the translator
    #white space and comment delimeters can produce wrong output
    LeadingWhitespace = InputString[:len(InputString)-len(InputString.lstrip())]
    InputString = InputString.lstrip().rstrip('\r\n')
    InputString = InputString.replace("/* ", '').replace(" */", '').replace("/*", '').replace("*/", '')
    
    translation = translator.translate(InputString.encode('utf-8'))

    #Add leading whitespace back and add comment delimeters
    TranslatedLine = LeadingWhitespace + "/* " + translation + " */\n"
    return TranslatedLine
    

BasePath = 'C:/Panasonic788/src/HDMIDrv'

#These header files are not encoded in SJIS so they need to be skipped
ProblemHeaderList = ["HDMIDrv_Tx_avfmt.h", "HDMIDrv_Rx_config.h"]

SourceList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.c')]
    
HeaderList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.h')]

translator = Translator(from_lang='ja', to_lang='en')

for path in SourceList:
    print path #print path in case we encounter an error opening this file
    newtarget = path + "_temp"
    
    with codecs.open(path, "r", "utf-8") as sourceFile:
        with codecs.open(newtarget, "w", "utf-8") as targetFile:
            while True:
                line = sourceFile.readline()
                if not line:
                    break
                targetFile.write(line) #write line first so that translated comment follows
                
                if HasUnicode(line):
                    TranslatedLine = TranslateLine(line)
                    if "HTTP://MYMEMORY.TRANSLATED.NET/DOC/QUOTAREACHED" in TranslatedLine:
                        print "Translation quota reached! Exiting."
                        sys.exit(0)
                    else:                        
                        targetFile.write(TranslatedLine)
    os.remove(path)
    os.rename(newtarget, path)
print "Completed source files" 

for path in HeaderList:
    print path #print path in case we encounter an error opening this file
    newtarget = path + "_temp"
    
    #Get file name from full path and check if it should be skipped
    if os.path.basename(path) in ProblemHeaderList:
        print "...skipped"
        continue
    
    with codecs.open(path, "r", "utf-8") as sourceFile:
        with codecs.open(newtarget, "w", "utf-8") as targetFile:
            while True:
                line = sourceFile.readline()
                if not line:
                    break
                targetFile.write(line) #write line first so that translated comment follows
                
                if HasUnicode(line):
                    TranslatedLine = TranslateLine(line)
                    if "HTTP://MYMEMORY.TRANSLATED.NET/DOC/QUOTAREACHED" in TranslatedLine:
                        print "Translation quota reached! Exiting."
                        sys.exit(0)
                    else:                        
                        targetFile.write(TranslatedLine)
    os.remove(path)
    os.rename(newtarget, path)
print "Completed header files"