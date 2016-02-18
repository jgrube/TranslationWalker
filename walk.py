from translate import Translator 
import chardet
from glob import glob
import codecs

def HasUnicode(InputString):
    encoding = chardet.detect(InputString.encode('utf-8'))
    if encoding['encoding'] == 'ascii':
        return False
    else:
        return True
        
def TranslateLine(InputString):
    InputString = InputString.replace("/* ", '').replace(" */", '').replace("/*", '').replace("*/", '')
    translation = translator.translate(InputString.encode('utf-8'))
    #print translation


translator = Translator(from_lang='ja', to_lang='en')

SourceList = glob("C:\ToTranslate\*\*.c")
HeaderList = glob("C:\ToTranslate\*\*.h")

for path in SourceList:
    print path
    FileHandle = codecs.open(path, encoding='shift_jis')
    for line in FileHandle:
        if HasUnicode(line):
            TranslateLine(line)
            
    FileHandle.close()

print "Complete"
