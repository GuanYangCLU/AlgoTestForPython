class Codec:
    def __init__(self):
        self.id = 0
        self.urlMap = {}
        self.tinyMap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny = str(self.id)
        if longUrl not in self.urlMap:
            self.urlMap[longUrl] = tiny
            self.tinyMap[tiny] = longUrl
            self.id += 1
        else:
            tiny = self.urlMap[longUrl]
        return tiny
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.tinyMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
