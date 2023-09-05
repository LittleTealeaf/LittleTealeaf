from libs.cache import clean_cache
from libs.utils import out
from libs.wakatime import getStats
from libs.markdown import table


clean_cache()

wakatime_stats = getStats("last_7_days")

extracted = {
    "Languages": wakatime_stats["languages"][0:5],
    "Editors": wakatime_stats["editors"][0:5],
    "Operating Systems": wakatime_stats["operating_systems"][0:5]
}


waka_table = table(
    headers=["Past Week Stats"],
    content=[
        [
            ", ".join(
                [
                    f"{item['name']} ({item['text']})"
                    for item in data
                ]
            )

        ] for category, data in extracted.items()
    ]
)


out(
    f"""
### Hello there! I'm Thomas Kwashnak

I'm a Computer Science and Data Science double major with an Economics
minor at Quinnipiac University, graduating in 2024.
I enjoy diving into algorithms and learning the inner-workings of the tools
many programmers take for granted.

{waka_table}

"""
)
