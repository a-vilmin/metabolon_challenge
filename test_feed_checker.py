from feed_checker import check_activity
import unittest
from freezegun import freeze_time


class TestFeedChecker(unittest.TestCase):

    @freeze_time("2019-06-26 12:00:00")
    def test_check_activity(self):
        input_dict = {
            "Has Published": [
                """
                <rss version="2.0">
                <channel>
                <item>
                <pubDate>Mon, 26 Jun 2019 01:56:02 -0000</pubDate>
                </item>
                </channel>
                </rss>
                """
            ],
            "Has Not Published": [
                """
                <rss version="2.0">
                <channel>
                    <item>
                        <pubDate>Mon, 23 Jun 2019 01:56:02 -0000</pubDate>
                    </item>
                </channel>
                </rss>
                """
            ],
            "Has Not Published (Multiple Feeds)": [
                """
                <rss version="2.0">
                <channel>
                    <item>
                        <pubDate>Mon, 26 Jun 2019 01:56:02 -0000</pubDate>
                    </item>
                </channel>
                </rss>
                """,
                """
                <rss version="2.0">
                <channel>
                    <item>
                        <pubDate>Mon, 23 Jun 2019 01:56:02 -0000</pubDate>
                    </item>
                </channel>
                </rss>
                """
            ],
            "Has Published (Multiple Feeds)": [
                """
                <rss version="2.0">
                <channel>
                    <item>
                        <pubDate>Mon, 26 Jun 2019 01:56:02 -0000</pubDate>
                    </item>
                </channel>
                </rss>
                """,
                """
                <rss version="2.0">
                <channel>
                    <item>
                        <pubDate>Mon, 26 Jun 2019 05:56:02 -0000</pubDate>
                    </item>
                </channel>
                </rss>
                """
            ]

        }
        self.assertListEqual(check_activity(input_dict, 2), ["Has Not Published", "Has Not Published (Multiple Feeds)"])


if __name__ == '__main__':
    unittest.main()
