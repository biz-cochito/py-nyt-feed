from rich import print
from rich.console import Console
from rich.text import Text
import cli.style as style
from .article import Article
# from .images import get_image, draw_image


def compile_article(response):
    article_block = Text()
    article = Article(response)
    title = article.title
    abstract = article.abstract
    published = article.published
    url = article.url
    section = article.section
    article_block.append(title, style=style.style_title)
    article_block.append(abstract)
    article_block.append(published)
    article_block.append(url, style=style.style_frame)
    article_block.append(section, style=style.style_muted)
    # article_block.stylize(style.style_frame)
    return article_block
    
    

def display_article(response):
    article_block = compile_article(response)
    console = Console()
    console.print(article_block)
    # print("\n")
