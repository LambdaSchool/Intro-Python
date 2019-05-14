# Intro to Python I

It's time to learn a new language! Python!

Python is a popular, easy-to-use programming language that has significant
traction in the field.

Remember the goal is _learning to learn_, so keep track of what works for you
and what doesn't as you go through the process of exploring Python.

## Techniques for learning new languages

* Try to relate things you already know in another language (e.g. what an
  _array_ is) to the corresponding things in Python (e.g. a _list_) and how to
  use them.

* Write a bunch of "toy programs" that demonstrate different key features of the
  language

* Explore the standard library that's available for the language. Skim it
  briefly for now--the idea isn't to memorize everything but to file away
  generally what functionality is available.

* Write a more substantial toy program that uses a variety of the features.

Again, keep track of what works for you. Try different things to see what works
best for learning new languages.

## Resources

* [Installing Python and pipenv](https://github.com/LambdaSchool/CS-Wiki/wiki/Installing-Python-3-and-pipenv)
* [JavaScript<->Python cheatsheet](https://github.com/LambdaSchool/CS-Wiki/wiki/Javascript-Python-cheatsheet)
* [How to read Specs and Code](https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Read-Specifications-and-Code)
* [Python 3 standard library](https://docs.python.org/3.6/library/)

## Getting started

1. Make sure you have Python 3 and pipenv installed.

2. Go to the directory with the `Pipfile` and run
   ```
   pipenv install
   ```

3. After the install completes, run
   ```
   pipenv shell
   ```
   This will get you into the virtual environment. At this point, you should be
   able to run Python 3 by just running `python`:
   ```
   $ python --version
   Python 3.6.5
   ```

   You can exit the virtual environment by typing `exit`.

## Goals

• Learn the basic syntax and structure of Python

## Summary

• Implement a number of tiny Python programs that demonstrate Python syntax and language concepts.

## Instructions

Each directory inside the src/ directory presents exercises revolving around a particular concept in Python. Not all of these concepts are unique to Python (in fact, most probably aren't). This means that you can leverage knowledge you've obtained via exposure to other programming languages towards learning Python.

The suggested order for going through each of the directories is:

* `hello` -- Hello world
* `bignum` -- Print some big numbers
* `datatypes` -- Experiment with type conversion
* `modules` -- Learn to import from modules
* `printing` -- Formatted print output
* `lists` -- Python's version of arrays

* `comp` -- List comprehensions
* `dicts` -- Dictionaries
* `func` -- Functions
* `cal` -- Experiment with module imports
* `obj` -- Classes and objects

## Day 2

Put it together into a bigger toy program: a simple text adventure!

This is in `src/adv.py`. Check it out!
