from rich.console import Console
from rich.style import Style
from rich.text import Text

from nyt_feed.api.models import Article


def display_article(response, config, number=None):
    preview_block = Text()
    console = Console()
    article = Article(response)

    # Strip URL cleanly
    article_url = article.url.replace("URL: ", "").strip()
    title_link = Text(
        article.title, style=Style(link=article_url, color="color(10)", bold=True)
    )

    if config.disp_numbers and number is not None:
        title_number = Text(f"{str(number)}. ", style="dim")
        title = Text.assemble(title_number, title_link)
    else:
        title = title_link
    preview_block.append(title)

    info_parts = []
    if config.disp_abstract and article.abstract.strip():
        info_parts.append(article.abstract)

    if config.disp_date and article.published.strip():
        date_stripped = article.published.replace("Published: ", "").strip()
        info_parts.append(Text(f"{date_stripped}\n", style="dim"))

    if info_parts:
        info = Text.assemble(*info_parts)
        preview_block.append(info)

    if config.disp_section and article.section.strip():
        preview_block.append(article.section, style="dim")

    console.print(preview_block)
