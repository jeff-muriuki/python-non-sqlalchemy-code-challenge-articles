class Article:
    all= []
    def __init__(self,author, magazine, title):
        self.author= author
        self.magazine= magazine
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title= title
        else:
            raise ValueError('title must be...')
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
   
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author= value
        else:
            raise ValueError('author must be...')
        
    @property
    def magazine(self):
        return self._magazine
   
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine= value
        else:
            raise ValueError('magazine must be...')    

class Author:
    all= []
    def __init__(self, name):
        if  isinstance(name, str) and len(name) > 0:
            self._name= name
        else:
            raise ValueError('Name must be...')    
        Author.all.append(self)

    @property
    def name(self):
        return self._name      

    def articles(self):
        return [article for article in Article.all if article.author== self]  
    
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception('article must...')
        article= Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    all= []
    def __init__(self, name, category):
        self.name= name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance (name,str) and 2 <= len(name) <= 16:
            self._name= name
        else:
            raise ValueError('Name must be ...')    

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category= category
        else:
            raise ValueError('category must be...')    

    def articles(self):
        return [article for article in Article.all if article.magazine== self ]
    
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
