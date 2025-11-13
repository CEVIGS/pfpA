import plw as ms
import os
import random
from pathlib import Path

# Implement custom configuration here
# Note that results/ and result.jpg WILL be overwritten/deleted every run
SAVE_RESULTS = False
SAVE_FINAL_RESULT = True

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
    username = os.environ["KEGSCRAPER_USERNAME"]
    secret = os.environ["KEGSCRAPER_SECRET"]

    pfp_dir = Path(__file__).parent / "pfps"
    pfps = next(pfp_dir.walk())[2]  # root, dirs, files (we choose files)

    print(f"Found {pfps=}")
    pfp: Path = (pfp_dir / choose_pfp(pfps)).resolve()
    assert pfp.exists(), f"Invalid pfp {pfp!r}"
    print(f"Chose {pfp=}")

    ms.set_pfp(username, secret, str(pfp),
               save_results=SAVE_RESULTS,
               save_final_result=SAVE_FINAL_RESULT)


if __name__ == '__main__':
    main()
