# Election Results Scraper
This Python script scrapes election results from Wikipedia and visualizes them using a bar chart. It specifically targets the 2020 United States elections results page.

## Installation
To run this script, you need Python installed on your machine along with the following Python libraries:
- `requests`
- `BeautifulSoup4`
- `matplotlib`
You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 matplotlib

## How to run
Use python environment to run.

## How to Use
Once you run the script, it will automatically fetch the data from the specified Wikipedia page, process it, and display a bar chart showing the results of the 2020 US elections by state.

Note: The scraping functionality is based on the structure of the Wikipedia page as of the time of writing this script. If the structure of the webpage changes, the script may require updates.
## Result
here is a screenshot of the result diagram:
![image](https://github.com/Erixcai/HomeTakeTask/assets/116468493/10ca6ea3-d055-491a-9967-2dcaaf688a9f)

## Future job
There is still some error remaining in the graph. There is still a lot of gibberish at the horizontal and vertical coordinates. 
This is despite the fact that we know that the codes in the vertical coordinates represent different states (sorted alphabetically) 
and the vertical codes represent different votes. Even though we can get enough relative vote relationships from the chart for the 2020 election, 
the jumbled codes still negatively impact the viewability of our images. Here's what I analyzed as a possible problem: Because the website was looking 
for itself, it didn't manage to find the most appropriate model when analyzing the webpage using llm. This is the next problem that needs to be solved.
