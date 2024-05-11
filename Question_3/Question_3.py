import openai
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_openai_response(api_key, user_query):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_query}]
    )
    return response.choices[0].message['content']


def google_search(query, api_key, cse_id):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {'key': api_key, 'cx': cse_id, 'q': query}
    response = requests.get(url, params=params)
    return response.json()


def extract_data_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract element 'table' from HTML
    tables = soup.find_all('table')
    data = []
    for table in tables:
        for row in table.find_all('tr')[1:]:  # Assume the first line is title
            cols = row.find_all('td')
            if len(cols) >= 2: 
                state = cols[0].text.strip()
                result = cols[1].text.strip()
                data.append((state, result))
    # if we did not get any data, always happens when the search engine returns a pdf link
    if data ==[]:
        raise('Ops, we did not find any data from resources! Try again!')
        
    return data

def clean_data(data):
    cleaned_data = []
    unique_data = set()  # use set to unique data
    
    for item in data:
        # pick all the data that include '%' and no '\n' or ' '.
        cleaned_item = [x for x in item if '%' in x and len(x) <= 10 and '\n' not in x and ' ' not in x]
        
        # use tuple to make sure that there isn't any duplicated item
        if cleaned_item and all(cleaned_item) and len(cleaned_item) > 1:
            cleaned_tuple = tuple(cleaned_item)
            
            if cleaned_tuple not in unique_data:
                unique_data.add(cleaned_tuple)
                cleaned_data.append(cleaned_tuple)
    # If the cleaned_dada is still empty
    if cleaned_data == []:
        raise('There is not any data satisfy your requirement. Search it again.')
    return cleaned_data

def plot_pie_chart(data, title):
    
    labels = []
    sizes = []
    
    for item in data:
        labels.append(f"{item[0]} vs {item[1]}")  
        size1 = float(item[0].strip('%'))
        size2 = float(item[1].strip('%'))
        sizes.append([size1, size2])
    
    
    for i, size in enumerate(sizes):
        fig, ax = plt.subplots()
        
        
        total = sum(size)
        if total < 100:
    
            size.append(100 - total)
            
            pie_labels = ['First', 'Second', 'Remaining']
            pie_colors = ['blue', 'green', 'gray']  
        else:
            pie_labels = ['First', 'Second']
            pie_colors = ['blue', 'green']

        
        ax.pie(size, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=pie_colors)
        ax.axis('equal')  
        plt.title(f"{title}")
        plt.show()
        

def main():
    openai_api_key = 'your-openai-api-key' # replace these keys and id to your own
    google_api_key = 'your-google-api-key'
    google_cse_id = 'your google-cse-id'
    user_query = "What's 2012 US election result?"
    count = 0
    # Get a response from OpenAI
    response_text = get_openai_response(openai_api_key, user_query)
    print('response_test: '+ response_text)
    # Use the response to query Google Custom Search
    results = google_search(response_text, google_api_key, google_cse_id)
    print('results: '+ str(results))
    # Print the search results
    for result in results.get('items', []):
        print(result['title'])
        print(result['link'])
        print(result['snippet'])
        print()
        count += 1
        if count == 1:
            break
    web_link = result['link']
    print('web_link: '+ web_link)
    extract_data = extract_data_from_url(web_link)
    # print('extract_data: '+ str(extract_data))
    
    clean_extract_data=clean_data(extract_data)
    print('clean_extract_data: '+ str(clean_extract_data))
    
    plot_pie_chart(clean_extract_data, user_query)
    
    
    
if __name__ == '__main__':
    main()
