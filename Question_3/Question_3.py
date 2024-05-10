import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Function to scrape election results
def scrape_election_results():
    url = "https://en.wikipedia.org/wiki/2020_United_States_elections#:~:text=The%202020%20United%20States%20elections,Trump%20in%20the%20presidential%20election"  # Placeholder URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data in the page - This will depend on the website's structure
    data = []
    count = 0
    count_skip = 0
    for row in soup.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) > 1: # Assuming there are at least two columns for State and Result
            if count_skip <10:
                count_skip += 1
                continue
            if count < 40:
                state = cols[0].get_text()
                result = cols[1].get_text()
                data.append((state, result))
                count += 1
            else:
                break
            
    # print('rows are: '+str(row))
    print(str(data))
    return data

def visualize_data(data):
    # data preprocess
    states = [item[0].strip() for item in data]  
    results = [item[1].strip() for item in data]  
    
    # plot charts
    colors = ['red' if result == 'Rep' else 'blue' for result in results]  # choose the color as it should be
    plt.figure(figsize=(14, 7))
    plt.bar(states, range(len(states)), color=colors)  # use index as the height of bar
    plt.xlabel('States in Alpha-Beta Order')
    plt.ylabel('Results')
    plt.title('Election Results by State Margin')
    plt.xticks(rotation=90, color='white')  
    plt.show()
    
    # Create bar chart
    rep_count = results.count('Rep')
    dem_count = results.count('Dem')
    plt.figure(figsize=(7, 7))
    plt.pie([rep_count, dem_count], labels=['Republican', 'Democratic'], colors=['red', 'blue'], autopct='%1.1f%%')
    plt.title('Percentage of Republican vs Democratic Results')
    plt.show()


# Main function
def main():
    data = scrape_election_results()
    # plot_results(data)
    visualize_data(data)

if __name__ == "__main__":
    main()
