# HomeTakeTask
## DrLambda Take Home Project 2
In this project, I answered four questions about AI in total.
Question 1:play around julius.ai, use it to search and generate charts
Here is the screenshot of how I use julius to generate charts:
![image](https://github.com/Erixcai/HomeTakeTask/assets/116468493/d9a9905c-f09f-4fff-99d4-65bae90eff4a)

Question 2:if I give you a large chunk of data and a query, can you write a program to generate a chart similarly? using llm and python.
The answer to question 2 is under the 'question 2' file.Please Check there.
Please notice that, it's a template that should be modified before use it to graph.

Question 3: If i just ask you a question, can you search online (programmatically), and answer the question in a chart or graph?
The answer to question 3 is under the 'question 3' file.Please Check there.

Question 4. How long does it take, do you have any idea how to make it faster?
For my laptop, I used 0.55 seconds to get the graph/diagram from it.
Here are the ways to how to improve it: 
First, I can use parallel processing techniques with libraries like ‘multiprocessing’ or ‘concurrent.futures’ to distribute the work across multiple CPU cores. Secondly, my algorithm is just straightforward. The computation time would improve a lot if I used some search strategy to collect data from the website. Last, we can improve the performance on ‘Caching’ related stuff. We can consider caching the results using a library like ‘functools.lru_cache’ to avoid redundant computation.’



