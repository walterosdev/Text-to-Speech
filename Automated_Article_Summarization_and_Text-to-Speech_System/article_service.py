from newspaper import Article
from article_model import ArticleData

class ArticleService:
    def __init__(self,url):
        self.url=url        #Define la url del articulo al cual vamos a extraerle la informacion

    def get_text(self):
        article=Article(self.url)  #Utiliza la funcion de ARticle para obtener el articulo a partir de la URL
        article.download()  #Descarga el contenido bruto del articulo
        article.parse()     #Procesa el html descargado y destaca la informacion relevante

        if not article.text:
            raise ValueError("No se pudo extraer el texto")
        return ArticleData(
            title=article.title,
            text=article.text,
            authors=article.authors,
            publish_date=article.publish_date
        )
          