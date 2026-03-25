import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from langdetect import detect, LangDetectException

LANGUAGE_MAP = {
    "es": "spanish",
    "en": "english",
    "fr": "french",
    "de": "german",
    "it": "italian",
    "pt": "portuguese"
}

class TextProcessor:
    def __init__(self,default_language='spanish'):
        self.language=None
        self.default_language=default_language  
    def process(self,text):
        try:
            detected_lang=detect(text)
            self.language=LANGUAGE_MAP.get(detected_lang, self.default_language)
        except LangDetectException:
            print("❌ No se pudo detectar el idioma del texto.")
            return []
        #Validar si NLTK Soporta el idioma
        if self.language not in stopwords.fileids():
            print(f"❌ Idioma no soportado: {self.language}")
            return []
        
        stop_words=set(stopwords.words(self.language))

        text=text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens=word_tokenize(text)

        return [w for w in tokens if w not in stop_words]
    
    