# Search Online & Answer Questions in Diagram
This python script answers the question 'If i just ask you a question, can you search online (programmatically), and answer the question in a chart or graph?' In this script, I used 'What was 2020 US election results?' as an example to demo the result.

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
Use python environment to run.

## How to Use
Once you run the script, it will automatically fetch the data from the specified Wikipedia page, process it, and display a bar chart showing the results of the 2020 US elections by state.

Note: The scraping functionality is based on the structure of the Wikipedia page as of the time of writing this script. If the structure of the webpage changes, the script may require updates.

Also, the plot_result function should also be modified if you changed the topic, but you don't need to modify the skeleton.
## Result
here is a screenshot of the result diagram:
![image](https://github.com/Erixcai/HomeTakeTask/assets/116468493/b7e64ed1-c8c2-43b2-b29a-9e8bc3a8585a)
![image](https://github.com/Erixcai/HomeTakeTask/assets/116468493/8a65a342-83d2-4aa1-8450-31eecde6e5ee)


## Future job
1.The pictures should be made a little more elaborate. For example, have each bar graph show the name of the state where it belongs.
2.Making the code implementation more universal.
