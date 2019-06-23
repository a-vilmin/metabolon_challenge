import feedparser
from datetime import datetime, timedelta

def check_activity(feed_dict, length_of_time):
    none_in_interval = []
    for company, feeds in feed_dict.items():
        for feed in feeds:
            loaded_feed = feedparser.parse(feed)
            try:
                latest_entry = loaded_feed.entries[0]
            except KeyError:
                print("There was an error loading " + feed)
                continue

            # Get date, check if its from before the time interval, add name to list if it is
            latest_entry = datetime.strptime(latest_entry.published, "%a, %d %b %Y %H:%M:%S -%f")

            if latest_entry < datetime.now() - timedelta(days=length_of_time):
                none_in_interval += [company]
                break
    return none_in_interval
