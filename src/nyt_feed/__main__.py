from nyt_feed.api import auth_nyt
from nyt_feed.cli.config import init_config
from nyt_feed.cli.previews import display_article


def main():
    nyt = auth_nyt()
    config = init_config("config.toml")

    if not config.sections:
        stories = nyt.top_stories()
    elif len(config.sections) > 1:
        stories = []
        for sec in config.sections:
            for x in nyt.top_stories(section=sec):
                stories.append(x)
    else:
        stories = nyt.top_stories(section=config.sections[0])

    i = 1
    for story in stories:
        display_article(story, number=i)
        i += 1


if __name__ == "__main__":
    main()
