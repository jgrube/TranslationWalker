# TranslationWalker
Quick and dirty script to translate comments from Japanese to English. The script will take a parent directory and find all C source and header files in that directory and all subdirectories. Using the google-translate-python library, any Japanese comments are translated to English using an online translator. English comments are left as-is.

# Dependencies
* [google-translate-python](https://github.com/terryyin/google-translate-python)
* glob
* codecs
* chardet
