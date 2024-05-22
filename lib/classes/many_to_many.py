class Article:
    all= []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.add_new_article(self)
        
    @classmethod
    def add_new_article(cls, new_article):
        cls.all.append(new_article)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self,'_title') and isinstance(new_title, str) and 5 <= len(new_title) <=50:
            self._title = new_title
            
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine= new_magazine
    
    
    

class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self,'_name') and isinstance(new_name, str) and 0 <= len(new_name):
            self._name = new_name
    
    def articles(self):
        return[article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        all_magazines= {article.magazine for article in self.articles()}
        topic_areas = [articles.category for articles in all_magazines]
        if topic_areas == []:
            return None
        else:
            return topic_areas


class Magazine:
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.add_new_magazine(self)
        
       
    @classmethod
    def add_new_magazine(cls, new_magazine):
        cls.all.append(new_magazine)
 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and 0 < len(new_category):
            self._category = new_category
        
    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if self.articles() == []:
            return None
        else:
            return [article.title for article in self.articles()]
       

    def contributing_authors(self):
        all_articles_authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in set(all_articles_authors) if all_articles_authors.count(author) > 2]
        if contributing_authors == []:
            return None
        else:
            return contributing_authors
        
    @classmethod
    def total_for_specific_magazine(cls,magazine):
        return len(magazine.articles())
    
    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None
        else: 
            return max(cls.all, key=lambda magazine: magazine.total_for_specific_magazine(magazine))