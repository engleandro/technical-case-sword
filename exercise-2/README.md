# Exercise 2

Write a Python program that takes as input the name of a txt file and creates another file
having the number of occurrences of each word in the original file in descending order. E.g.:

```
the 563
of 431
to 320
it 210
that 109
```

Your program should distribute the computation by having 10 worker threads simultaneously
building the resulting list.

# Solution

The solution is in the `app` folder.

The prerequisite to run the solution is to install a simple Python runtime (no external dependencies are required).

To test it locally:

```bash
# run the entrypoint of application "main.py"
python main.py .\example.txt words.txt
```
