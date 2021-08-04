# fetching data :
# url = 'https://www.allsides.com/media-bias/media-bias-ratings'

# r = fetch(url)
# parsing data :
# soup = BeautifulSoup(r['content'], 'html.parser')
# print(soup.prettify())

# So to get each row, we just select all <tr> inside <tbody>:
# rows = soup.select('tbody tr')
# getting title of the first row :
# .strip() ensures all the whitespace surrounding the name is removed.
# Many websites use whitespace as a way to visually pad the text inside elements so using strip() is always a good idea.
# row = rows[0]
# title = row.select_one('.source-title').text.strip()
# print(title)

# getting links
# sides_page = row.select_one('.source-title a')['href']
# sides_page = 'https://www.allsides.com' + sides_page
#
# print(sides_page)

# getting bias :
# bias = row.select_one('.views-field-field-bias-image a')['href']
# bias = bias.split('/')[-1]
# print(bias)

# community feedback :
# agree = int(row.select_one('.agree').text)
#
# disagree = int(row.select_one('.disagree').text)
#
# agree_ratio = agree / disagree

# print(f"Agree: {agree}, Disagree: {disagree}, Ratio {agree_ratio:.2f}")

# getting all rows:
# data = []
#
# for row in rows:
#     d = dict()
#
#     d['name'] = row.select_one('.source-title').text.strip()
#     d['allsides_page'] = 'https://www.allsides.com' + row.select_one('.source-title a')['href']
#     d['bias'] = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
#     d['agree'] = int(row.select_one('.agree').text)
#     d['disagree'] = int(row.select_one('.disagree').text)
#     d['agree_ratio'] = d['agree'] / d['disagree']
#     d['agreeance_text'] = get_agreeance(d['agree_ratio'])
#
#     data.append(d)
# print(data)