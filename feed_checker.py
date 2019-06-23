import feedparser

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
    return []
