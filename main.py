import os
import random
import tomllib
from pathlib import Path
from pprint import pprint, pformat
from cevigspfpautomation import plw as ms


def choose_pfp(pfps: list[str]) -> str:
    """
    Define how the pfp is chosen
    :param pfps: A list of filenames in the pfps/ directory. e.g. ["pfp-moab.png", "pfp-lego.png", ...]
    :return: The desired pfp to set (str), e.g. "pfp-moab.png"
    """
    # If you wanted to set a pfp e.g. by day of the week,
    # where the pfp for monday is called 'mon.png', tuesday's pfp is 'tue.jpg' etc (any file extension allowed)
    # from datetime import datetime
    # dayname = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"][datetime.now().weekday()]
    # print(f"Choosing pfp for {dayname}")
    # return next(filter(lambda s: dayname in s.lower(), pfps))

    return random.choice(pfps)

# DON'T TOUCH BELOW THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING

def main():
    """
    The main script which sets your pfp. This is run by the GitHub action every day.
    """
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    assert "email" not in config, "Don't use config.toml for email! Use github secrets instead!" 
    assert "password" not in config, "Don't use config.toml for password! Use github secrets instead!"

    # if no secret value is set, github sets it to an empty string
    # we are also using getenv for some unrequired ones for local testing purposes.
    username = os.environ["KEGSCRAPER_USERNAME"]
    password = os.environ["KEGSCRAPER_SECRET"]
    
    assert username and password, "need authentication!"

    print(f"""\
## Settings (passed as **kwargs to set_pfp)
{pformat(config)}
""")

    pfp_dir = Path("pfps")
    pfps = next(pfp_dir.walk())[2]  # root, dirs, files (we choose files)

    print("## Pfp list:")
    pprint(pfps)
    pfp: Path = (pfp_dir / choose_pfp(pfps)).resolve()
    assert pfp.exists(), f"Invalid pfp {pfp!r}.\nThis is a problem with the choose_pfp() function - that you presumably edited - NOT pfpautomation itself."
    print(f"Chose {pfp=}")

    ms.set_pfp(username, password, str(pfp), **config)


if __name__ == '__main__':
    main()
