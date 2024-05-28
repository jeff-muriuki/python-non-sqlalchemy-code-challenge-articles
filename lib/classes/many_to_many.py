class Article:
    all= []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError('title must be...')
        self._title = title
        self.author = author
        self.magazine = magazine
        #self._author= None
        #self._magazine= None
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title    
    
    @property
    def author(self):
        return self._author        

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception('invalid Author')
        self._author= value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance (value, Magazine):
            raise Exception('Invalid Magazine')
        self._magazine= value


class Author:
    all= []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError('Name must be string')
        self._name = name
        self._articles= []
        Author.all.append(self)
        

    @property
    def name(self):
        return self._name    
    #@property
    def articles(self):
        #return self._articles
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Invalid magazine")
        article = Article(self, magazine, title)
        #self._articles.append(article)
        return article

    def topic_areas(self):
        if not self.articles():
            return None
        categories = set(article.magazine.category for article in self.articles())
        return list(categories)

class Magazine:
    all= []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError('name must be of type str and ...')
        self._name = name
        if not isinstance(category, str) or len(category) == 0:
            raise TypeError('category must be a non-empty string')
        self._category= category
        #self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError('Name must be a string and between 2 and 16 characters')
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('category must be ...')
        self._category= value
    
    #@property
    def articles(self):
        #return self._articles
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            if article.author not in author_counts:
                author_counts[article.author] = 0
            author_counts[article.author] += 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        return contributing_authors if contributing_authors else None

