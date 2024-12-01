# Day 1 Historian Hysteria.
---

## Part 1
We have 2 list and the task is to **calculate the total distance starting by the _smallest_ one of each list**. For each pair, calculate the absolute difference between the numbers then sum the distances from each pair to determine the total "distance" between the two lists.

## Part 2
The task is to **determine how often each number from the left list appears in the right list**. Then, calculate a total similarity score by summing each number in the left list multiplied by the frequency of its occurrences in the right list.

---

This solution uses Python’s built-in functions like `sort`, `zip`, `map` and `count` to efficiently handle the task.

To solve this problem, I started by processing the input from a text file.

#### Input Processing

* Each line was stored as a string in a list.
* I removed any **newline characters** and **spaces** to keep only the numbers.
* The first number from each line was converted to an integer and added to one list using the `append` method.
* Similarly, I added the second number to another list.

#### Step 1: Sorting and Calculating Total Distance

* I sorted both lists using the `sort` method.

* To calculate the total distance:
    * I paired corresponding elements using the `zip` function.
    * I calculated the absolute differences between paired elements.
    * Finally, I summed these differences to get the result.

#### Step 2: Calculating the Total Similarity Score

* I iterated over the first list.

* For each number:
    * I checked with the `count` method to find how many times it appeared in the second list.
    * I multiplied the number by its frequency and added the result to the total score.

[Check code here!](solution.py)