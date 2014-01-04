RSS_Feed
========

This code uses Python to access RSS Feed information


1. Add media source to Feedly RSS feed. 
             example: Marketwatch.com

2. Grab the feedly link to the MarketWatch RSS feed. 
             example: http://feedly.com/#subscription%2Ffeed%2Fhttp%3A%2F%2Fwww.marketwatch.com%2Frss%2Ftopstories

3. Run this string through Get_feed_link.py to extract the RSS site without the feedly.com part 
             example output: http://www.marketwatch.com/rss/topstories

4. Use output from #3 as input to Get_feed_data.py. Get_feed_data.py has a few different functions that can return number of articles, titles, original links.
