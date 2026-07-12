class Article:
    def __init__(self, response):
        self.title = f"{response.get('title', '')}\n"
        self.abstract = f"{response.get('abstract', '')}\n"
        self.published = f"Published: {response.get('published_date', '')}\n"
        self.url = f"URL: {response.get('url', '')}\n"
        self.section = f"Section: {response.get('section', '')}\n"
        
        multimedia = response.get('multimedia')
        if multimedia and len(multimedia) > 1:
            self.img_url = f"{multimedia[1].get('url', '')}\n"
        elif multimedia and len(multimedia) > 0:
            self.img_url = f"{multimedia[0].get('url', '')}\n"
        else:
            self.img_url = None

