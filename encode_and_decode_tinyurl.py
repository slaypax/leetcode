# https://leetcode.com/problems/encode-and-decode-tinyurl
# TinyURL is a URL shortening service where you enter a URL such as 
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.


# Runtime: 24 ms, faster than 93.85% of Python online submissions for Encode and Decode TinyURL.
import hashlib

class Codec:
    def __init__(self):
        self.url_map = {}
        self.prefix = 'https://tinyurl.com/'
        
    def encode(self, longUrl):
        urlHash = hashlib.md5(b'longUrl').hexdigest()[0:6]
        shortUrl = "{prefix}{urlhash}".format(prefix=self.prefix, urlhash=urlHash)
        self.url_map[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_map.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))