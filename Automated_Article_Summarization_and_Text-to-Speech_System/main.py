from article_service import ArticleService
from text_processor import TextProcessor
from summarizer import Summarizer
from tts_service import TextToSpeechService

def main():
    url = "https://www.eltiempo.com/mundo/mexico/operativo-que-llevo-a-muerte-de-el-mencho-llevara-a-una-disputa-interna-en-el-cartel-jalisco-nueva-generacion-advierte-informe-3535993"

    try:
        # 1. Obtener artículo
        article_service = ArticleService(url)
        article = article_service.get_text()

        print(article.title)
        print(article.authors)

        text = article.text

        # 2. Procesar texto (detección de idioma incluida)
        processor = TextProcessor()
        tokens = processor.process(text)

        if tokens is None:
            print("❌ Error procesando el texto")
            return

        language_detected = processor.language
        language_nltk = processor.language

        # 3. Resumir
        summarizer = Summarizer()
        summary = summarizer.summarize(
                    text,
                    language=language_nltk
                    )

        print("📌 Resumen:\n")
        print(summary)

        # 4. Convertir a audio
        tts = TextToSpeechService(language="es")  # puedes mapear idioma si quieres
        audio_path = tts.save_audio(summary)

        print(f"\n🔊 Audio generado en: {audio_path}")

    except Exception as e:
        print(f"🚨 Error general: {e}")


if __name__ == "__main__":
    main()