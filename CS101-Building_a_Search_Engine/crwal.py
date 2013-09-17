#first,get and print
def get_next_link(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None
	start_quote = page.find('"',start_link)
	end_qoute = page.find('"',start_quote+1)
	url = page[start_quote+1:end_quote]
	return url,end_quote

def print_all_links(page):
	while True:
		url,endpos = get_next_link(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break
	
#go on,get and store
def get_all_links(page):
	links = []
	while True:
		url,endpos = get_next_link(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def add_to_index(index,keyword,url):
	for item in index:
		if item[0] == keyword:
			item[1].append(url)
			return 
	index.append([keyword,[url]])

def add_page_to_index(index,url,content):
	con_list = content.split()
	for item in con_list:
		add_to_index(index,item,url)

	
#ok, begin to crawl
def crawl_the_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while True:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			union(tocrawl,get_all_links(get_page(page)))
			crawled.append(page)
	return crawled

def union(p,q):
	for item in q:
		if item not in p:
			p.append(item)
	
def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""
		
def split_string(source,splitlist):
    flag = False
    word_list = []
    word = ''
    for char in source:
        #print char + '1'
        if char in splitlist:
           # print char + '2'
            flag = True
        else:
            if flag:
              #  print char + '3'
                word_list.append(word)
                word = char
                flag = False
            else:
                word = word + char
    word_list.append(word)
    return word_list