# TranslationWalker
Quick and dirty script to translate comments from Japanese to English. The script will take a parent directory and find all C source and header files in that directory and all subdirectories. Using the google-translate-python library, any Japanese comments are translated to English using an online translator. English comments are left as-is.

## Usage
Files must be UTF8 encoded (run EncodingConverter.py if needed). The script will search for all C source and header files in a given directory and translate one by one. If a header file doesn't contain any comments to be translated, it can be added to the list of files to skip. MyMemory has a 1000 word/day quota and that can be increased to 10,000 if you add an email to your request. See their [usage limits page](http://mymemory.translated.net/doc/usagelimits.php).

## EncodingConverter.py
The EncodingConverter script will convert shift-jis encoded files into UTF8 files. The script will only search for .c and .h files. If a header file is already UTF8, it can be added to the "ProblemHeaderList" to be skipped.


## Dependencies
* [google-translate-python](https://github.com/terryyin/google-translate-python)

