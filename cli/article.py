class Article:
    def __init__(self, response):
        self.title = f"{response['title']}\n"
        self.abstract = f"{response['abstract']}\n"
        self.published = f"Published: {response['published_date']}\n"
        self.url = f"URL: {response['url']}\n"
        self.section = f"Section: {response['section']}\n"
        self.img_url = f"{response['multimedia'][1]['url']}\n"
