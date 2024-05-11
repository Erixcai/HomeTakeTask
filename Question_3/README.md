# Search Online & Answer Questions in Diagram
This python script answers the question 'If i just ask you a question, can you search online (programmatically), and answer the question in a chart or graph?' In this script, I used 'What was 2020 US election results?' as an example to demo the result.
Input: A sentence or user's query.
Output: A pie chart if data is good.

## Installation
To run this script, you need Python installed on your machine along with the following Python libraries:
- `requests`
- `BeautifulSoup4`
- `matplotlib`
You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 matplotlib
```
## How to run
Before you run the python script under your anaconda or python environment, your should set up these three things in main() function:
1. openai_api_key : https://platform.openai.com/docs/quickstart
2. google_api_key : https://developers.google.com/maps/documentation/javascript/get-api-key?hl=zh-cn
3. google_cse_id : https://support.google.com/programmable-search/answer/12499034?hl=en

After setting these links up, directly click 'run' in your environment.
## How to Use
After run it, you will see an input box in your terminal: 'Please enter your query: ' 
Enter your questions, then 'enter'.
## Result
Case 1: Good data.
  Input: What's 2020 election results?
  Output:
![d8ec4a7d1e5869c178ac1281fd68203](https://github.com/Erixcai/HomeTakeTask/assets/116468493/c73342f3-5096-41ea-8680-58f87f7700cc) \\n
Case 2: Data is bad.
  Input: What's UCLA 2023 new student gender rate?
  Output: raise('Ops, we did not find any data from resources! Try again!')


## Future job
1.The pictures should be made a little more elaborate. For example, have each bar graph show the name of the state where it belongs.
2.Making the code implementation more universal.
