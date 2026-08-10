import tomllib


class Config:
    def __init__(self, config):
        self.sections = config["general"]["sections"]
        self.article_count = config["general"]["article_count"]
        self.disp_date = config["display"]["date"]
        self.disp_section = config["display"]["section"]
        self.disp_numbers = config["display"]["numbers"]
        self.disp_abstract = config["display"]["abstract"]


def init_config(file):
    with open(file, "rb") as f:
        toml = tomllib.load(f)
        config = Config(toml)
    return config
