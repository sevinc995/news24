class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "Ray-Ban Meta",
    "You can now use the glasses to remind you make a phone call or even where you parked your car."
    "https://picsum.photos/400?random=1"
)

news2 = News(
    "Amazon's new Fire tablet",
    "The company's refreshed Fire HD 8 will get some new AI tools, but they're rolling out to other Amazon tablets, too.",
    "https://picsum.photos/400?random=2"
)

news3 = News(
    "Meta unveils AI video tool: Movie Gen".
    "Movie Gen can create new clips from text prompts or edit your face into existing footage - complete with sound.",
    "https://picsum.photos/400?random=3"
)



news_list = []