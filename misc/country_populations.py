def  getCountries(s, p):
  answer = 0
  url = 'https://jsonmock.hackerrank.com/api/countries/search?name={}'.format(s)
  
  with urllib.request.urlopen(url) as response:
    html = response.read()
    html_string = json.loads(html.decode('utf-8'))
    
  size = len(html_string['data'])
  #print("size: ", size) //s='in' returning only 10 results so not able to get to 21 results to parse
  
  for i in range(size):
    if int(html_string['data'][i]['population']) >= p:
      answer += 1
      
  return (answer)
  
