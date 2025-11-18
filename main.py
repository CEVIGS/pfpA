import os
import random
from pathlib import Path
from pprint import pprint
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
    # if no secret value is set, github sets it to an empty string
    # we are also using getenv for some unrequired ones for local testing purposes.
    username = os.environ["KEGSCRAPER_USERNAME"]
    password = os.environ["KEGSCRAPER_SECRET"]
    save_results = os.getenv("SAVE_RESULTS", "") == "yes"
    save_final_result = os.getenv("SAVE_FINAL_RESULT", "") in ("yes", "")
    
    assert username and password, "need authentication!"

    print(f"""\
## Settings
{save_results=}
{save_final_result=}
""")

    pfp_dir = Path.cwd() / "pfps" # not sure if this is equivalent to Path("pfps")
    pfps = next(pfp_dir.walk())[2]  # root, dirs, files (we choose files)

    print("## Pfp list:")
    pprint(pfps)
    pfp: Path = (pfp_dir / choose_pfp(pfps)).resolve()
    assert pfp.exists(), f"Invalid pfp {pfp!r}.\nThis is a problem with the choose_pfp() function - that you presumably edited - NOT pfpautomation itself."
    print(f"Chose {pfp=}")

    ms.set_pfp(username, password, str(pfp),
               save_results=save_results,
               save_final_result=save_final_result)


if __name__ == '__main__':
    main()
