# Day 3 Mull It Over.

## Part 1

We receive an input and the task to complete is to **find the valid string "mul(x,y)" instructions, and sum up the results of these multiplications**.

Conditional mul(X,Y) instructions:

* X and Y are integers between 1 and 999.
* No invalid characters, extra spaces or incorrect delimiters are allowed.
* An invalid examples could be:
    * `mul(4*)`, `mul[3,7]`, `mul( 8, 5)`
* Valid example could be:
    * `mul(2,4)` → 8

## Part 2

In this part, conditional instructions are introduced to enable or disable the execution of valid mul instructions. So, now the task is to **execute only the enabled mul instructions and sum up the result of the new multiplications**.

Conditional Instructions
* By default, mul instructions are enabled.
* do(): Enables subsequent mul instructions.
* don't(): Disables subsequent mul instructions.

---

This solution leverages Python’s re module, utilizing functions like `findall` to efficiently parse and process the corrupted input. The problem is approached in two stages: identifying valid patterns and introducing conditional logic to filter results.

#### Input Processing

The input is stored as a single string, which contains both valid and irrelevant characters. Using **regular expressions** (*RegEx*) from Python's re module, I efficiently extracted valid patterns representing mul(X,Y) instructions.

#### Step 1: Extracting and Calculating Results

We're going to extract regex pattern, `r"mul\(\d+,\d+\)"`, is defined to **match valid mul instructions containing two numbers separated by a comma and enclosed in parentheses**. Using `re.findall`, all matches are stored in a list.

For each match we're going to parse and calculate:

* Extract numbers using the pattern `r"\d+"`.
* Convert the extracted strings to integers using map.
* Multiply the two numbers and accumulate their product in a running total.

#### Step 2: Conditional Execution with Flags

To handle `do()` and `don't()` instructions, a flag-based system was implemented to control whether mul instructions should be processed.

Flag Initialization and Instruction Handling:

* The flag starts as True, enabling mul processing by default.
* If a do() instruction is encountered, the flag is set to True.
* If a don't() instruction is encountered, the flag is set to False.

Conditional processing while scanning the input:

* If the flag is True, valid mul(X,Y) patterns are processed using the same logic from Step 1.
* If the flag is False, these instructions are skipped.