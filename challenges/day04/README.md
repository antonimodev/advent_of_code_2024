# Day 4 Ceres Search.

## Part 1

The task is to **find all occurrences of the word "XMAS" in a word search grid**. The word can appear in multiple orientations:

* Horizontal (left to right or right to left)
* Vertical (top to bottom or bottom to top)
* Diagonal (in any direction)
* Words can overlap, and all occurrences must be counted.

For example:

`MMMSXXMASM`
`MSAMXMSMSA`
`AMXSXMAAMM`
`MSAMASMSMX`
`XMASAMXAMM`
`XXAMMXXAMA`
`SMSMSASXSS`
`SAXAMASAAA`
`MAMMMXMMMM`
`MXMXAXMASX`

`XMAS` Word appears 18 times.

---

This solution uses Python's capabilities for iteration and input handling to efficiently analyze the grid.

#### Input Processing
The word search grid is provided as a text file, where each line represents a row. Here's how the input is processed:

* Read all lines from the file using Python's open function.
* Strip unnecessary characters like newlines to keep only the grid letters.
* Store each row as an element in a list.

#### Step 1: Checking for the Word in Any Direction

The function `is_word_in_direction` determines whether the word appears starting from a specific cell in the grid and moving in a given direction.

* Calculate the position of each letter in the word based on the steps.
* Check if the positions are within limits and match the letters in the word.
* Return True if all conditions are satisfied, else False.

#### Step 2: Counting All Occurrences of the Word

The function `count_words` iterates through every cell in the grid, trying all possible directions from each cell:

Directions:

* Right `(0, 1)`
* Down `(1, 0)`
* Down-right diagonal `(1, 1)`
* Down-left diagonal `(1, -1)`

For each direction, it also checks the reverse (*e.g., left, up, up-left, up-right*).

[Check code here!](solution.py)

<p align="center">
  <img src="../../images/AoC_2024_Star.png" alt="AoC 2024 Star" width="120" height="120">
</p>