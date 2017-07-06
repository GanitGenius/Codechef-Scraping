from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup

my_url = 'https://www.codechef.com/contests'

# opening up connection and closing
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# apply BeautifulSoup
soup = bsoup(page_html, 'html.parser')

#  Present Contest
present_contest = soup.find('h3', text='Present Contests').next_sibling.next_sibling.table.tbody

print('Present Contest')
for contest in present_contest.find_all('tr'):
	code = contest.contents[1].string
	name = contest.contents[3].a.string
	start_time = contest.contents[5]['data-starttime']
	#format time
	start_date = contest.contents[5].contents[0]
	end_time = contest.contents[7]['data-endtime']
	#format time
	end_date = contest.contents[7].contents[0]

	print (code + ' ' + name + ' ' + start_time + ' ' + start_date + ' ' + end_time + ' ' + end_date)



#  Upcoming Contests
upcoming_contest = soup.find('h3', text='Future Contests').next_sibling.next_sibling.table.tbody

print('\nUpcoming Contests')
for contest in upcoming_contest.find_all('tr'):
	code = contest.contents[1].string
	name = contest.contents[3].a.string
	start_time = contest.contents[5]['data-starttime']
	#format time
	start_date = contest.contents[5].contents[0]
	end_time = contest.contents[7]['data-endtime']
	#format time
	end_date = contest.contents[7].contents[0]

	print (code + ' ' + name + ' ' + start_time + ' ' + start_date + ' ' + end_time + ' ' + end_date)


