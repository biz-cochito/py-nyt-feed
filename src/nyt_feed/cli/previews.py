from rich.console import Console
from rich.style import Style
from rich.text import Text

from nyt_feed.api.models import Article


def display_article(response, number=None):
    preview_block = Text()
    console = Console()
    article = Article(response)
    article_url = article.url.strip("URL: ")
    title_link = Text(
        article.title, style=Style(link=article_url, color="color(10)", bold=True)
    )
    title_number = Text(f"{str(number)}. ", style="dim")
    title = Text.assemble(title_number, title_link)
    preview_block.append(title)
    date_stripped = article.published.strip("Published: ")
    pub_date = Text(date_stripped, style="dim")
    info = Text.assemble(article.abstract, pub_date)
    preview_block.append(info)
    preview_block.append(article.section, style="dim")
    console.print(preview_block)
