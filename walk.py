from translate import Translator
import chardet
import codecs
import fnmatch
import os, os.path
import sys

def HasUnicode(InputString):
    encoding = chardet.detect(InputString.encode('utf-8'))
    if encoding['encoding'] == 'ascii':
        return False
    else:
        return True
        
def TranslateLine(InputString):
    #Clean up input string for the translator
    #White space and comment delimeters can produce wrong output
    LeadingWhitespace = InputString[:len(InputString)-len(InputString.lstrip())]
    InputString = InputString.lstrip().rstrip('\r\n')
    InputString = InputString.replace("/* ", '').replace(" */", '').replace("/*", '').replace("*/", '')
    
    translation = translator.translate(InputString.encode('utf-8'))

    #Add leading whitespace back and add comment delimeters
    TranslatedLine = LeadingWhitespace + "/* " + translation + " */\n"
    return TranslatedLine
    

BasePath = 'C:/ToTranslate'

SourceList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.c')]
    
HeaderList = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(BasePath)
    for f in fnmatch.filter(files, '*.h')]
    
TranslateList = SourceList + HeaderList;

translator = Translator(from_lang='ja', to_lang='en')

for path in TranslateList:
    print path # Print path in case we encounter an error opening this file
    newtarget = path + "_temp"
    
    with codecs.open(path, "r", "utf-8") as sourceFile:
        with codecs.open(newtarget, "w", "utf-8") as targetFile:
            while True:
                line = sourceFile.readline()
                if not line:
                    break
                targetFile.write(line) # Write line first so that translated comment follows
                
                if HasUnicode(line):
                    TranslatedLine = TranslateLine(line)
                    if "HTTP://MYMEMORY.TRANSLATED.NET/DOC/QUOTAREACHED" in TranslatedLine:
                        print "Translation quota reached! Exiting."
                        # Exit without deleting so that the lines that were translated can be saved
                        sys.exit(0)
                    else:                        
                        targetFile.write(TranslatedLine)
    os.remove(path)
    os.rename(newtarget, path)
print "Completed translation" 
