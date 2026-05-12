# section_style = Style(color="grey")
from cli.previews import display_article
from nyt.nyt_api import auth_nyt

nyt = auth_nyt()
top_stories = nyt.top_stories()

def main(collection):
    
    for story in collection:
        display_article(story)

if __name__ == "__main__":
    main(top_stories)