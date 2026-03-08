from langdetect import detect

def detect_language(text):

    try:
        lang = detect(text)
    except:
        lang = "en"

    return lang