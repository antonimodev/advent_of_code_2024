# Day 2 Red-Nosed Reports.

## Part 1
We have several reports, each consisting of a sequence of numbers, and the task is to **determine whether each report is safe or unsafe based on specific rules**.

### Rules for Safety

* A report is safe if:
    * All consecutive numbers either increase or decrease consistently by 1, 2, or 3.
<br>
* A report is unsafe if:
    * Any pair of consecutive numbers has a change greater than 3 (*either an increase or decrease*).
    * There is no valid change between two consecutive numbers (*e.g., repetition like* `4 → 4`).
    * The sequence alternates between increasing and decreasing.

## Part 2

The **same rules** for determining safety apply as in Part 1. However we are going to introduce the Problem Dampener, a mechanism that allows removing one problematic number to potentially salvage an otherwise unsafe report.

* If removing one level from an unsafe report makes it safe, the report is considered safe.

`7 6 4 2 1`: Safe without removing any level.
`1 2 7 8 9`: Unsafe regardless of which level is removed.
`9 7 6 2 1`: Unsafe regardless of which level is removed.
`1 3 2 4 5`: Safe by removing the **second level**, **3**.
`8 6 4 4 1`: Safe by removing the **third level**, **4**.
`1 3 6 7 9`: Safe without removing any level.

Now, the task is to **modify the analysis to account for the Problem Dampener**.

---

This solution uses Python’s built-in functions like `range`, `len` and `map` to efficiently solve the task. To solve this problem I break it in two parts, but first of all is processing the input.

#### Input Processing

The input consisted of a text file, with each line representing a report. These were processed into a format suitable for analysis:

* Each line was split into a list of integers using Python’s `map` function.
* The resulting lists were stored for further processing.

This transformation provided a structured way to analyze reports sequentially.

#### Step 1: Identifying Safe Reports

To determine if a report was safe, I broke the problem into two key checks:

* Valid Differences: Consecutive numbers in the report must differ by a value between 1 and 3 (inclusive).
* Consistent Trends: The report must consistently increase or decrease based on its initial trend. Any deviation from this trend renders the report unsafe.

The logic for these checks was encapsulated in the `is_safe_report` function, which:

* Iterates over the report.
* Compares consecutive numbers for valid differences.
* Tracks the sequence's trend to detect inconsistencies.

#### Step 2: Introducing the Problem Dampener

In the second part, reports could now be considered safe if removing a single problematic number made them comply with the rules. To handle this, I created a function called `problem_dampener` that allows re-check the report after remove 1 number.

* For each number, create a modified version of the report excluding that number.
* Re-check validity using the same rules from Step 1 to evaluate the modified report.

This ensures that **only one number** is removed, and the process stops as soon as the report becomes valid. If no single removal works, the report remains unsafe.

[Check code here!](solution.py)

<p align="center">
  <img src="../../images/AoC_2024_Star.png" alt="AoC 2024 Star" width="120" height="120">
  <img src="../../images/AoC_2024_Star.png" alt="AoC 2024 Star" width="120" height="120">
</p>