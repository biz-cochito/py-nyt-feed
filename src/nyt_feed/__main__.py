from nyt_feed.api import auth_nyt
from nyt_feed.cli.previews import display_article


def main():
    nyt = auth_nyt()
    top_stories = nyt.top_stories()

    i = 1
    for story in top_stories:
        display_article(story, number=i)
        i += 1


if __name__ == "__main__":
    main()
