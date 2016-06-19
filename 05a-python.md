# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> The biggest difference between lists and tuples is that lists are mutable (editable), and tuples are not. Lists can have items appended, removed, and items in the list can have their values edited at any time.
Tuples have a pre-defined length and values, and as such are designed to both have (slightly) faster run speeds and can be used as keys for dictionaries.
This is by design so that the keys used for dictionaries cannot be changed by a function, which is why lists cannot be used (as they can easily change, causing more potential downstream harm).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both collections of items, but differ in two main ways:

1) Lists are ordered, and sets are not. Items in a set do not have an index and do not record when they are written. As such, items in lists can be referenced by an index (position) and manipulated via that index. For sets, it is easier to locate existence of an element and one can perform calculations/analysis on the entire set

2) Lists can contain multiple copies of the same item, but sets cannot.

List example: The number of people that visit a store each day. Since these values can be repeated, they should be stored in a list (or tuple, if it is intended to be immutable source data).
Set example: How many items trigger a certain event, such as (the morbid example) "How many states have had shootings with 4+ deaths in the last year?". If this has happened more than once, a state should not be recounted and will simply reside in the set when the first event is triggered.

Finding a specific element of a list/set is faster in a set because it is ordered via a hash table instead of an index. Lists must be iterated through to find the object you are looking for, but a set simply needs its requisite hash to be found.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is a nameless function, designed for simple calculations that don't need formal construction. They can be used as an inline function, so there is no need to define them before they are needed. This allows you to perform some pretty common complex analyses without having to define everything beforehand.

Example: sorted(['Sorting', 'can', 'Be', 'Fun', 'but', 'Often', 'Is', 'not'],
  key = lambda word: word.lower())

The sorted() function treats capitalized letters ahead of lowercase ones, and using a defined function to do the same thing would have to be defined before sorted() is called, it cannot be constructed when it is called like the lambda function here.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a quick and easy way to use a for loop to check for a certain condition in a set/list/tuple and then perform necessary calculations or analyses. They can also perform all the functions that map and filter use but with much less text, all neatly wrapped in a single line (usually).

Example:
>>> X = [x+5 for x in range(10)]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Example with map:
>>> print map(lambda x: x+5, range(10))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Set comprehensions are just list comprehensions but for sets (no order, no duplicates). Set comprehensions would be particularly useful in an example such as searching for prime numbers, usually done by first calculating numbers which are not prime. To do so, they would need to be contained in a set, because many numbers will be divisible by different smaller numbers, making it difficult to calculate using a list.

Dictionary comprehensions work in the same way but need a key/value pair set for whatever they are to be iterated over (searching for usernames:emails for instance).

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days (not counting final day as 1 day)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
