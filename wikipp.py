#import wikipediaapi
#wiki_wiki = wikipediaapi.Wikipedia('en')
#page_py = wiki_wiki.page('Python_(programming_language)')
#print(page_py)
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Title: %s" % page_py.title)
    # Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary[0:200])
    # Page - Summary: Python is a widely used high-level programming language for
