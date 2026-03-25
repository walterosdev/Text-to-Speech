from nltk.tokenize import sent_tokenize

class Summarizer:
    def summarize(self, text, language="spanish", num_sentences=3):
        sentences = sent_tokenize(text, language=language)
        return " ".join(sentences[:num_sentences])