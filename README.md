# Diderot Computer-Aided Feedback (CAFE)

## CAFE libraries

This repository contains CAFE libraries in python and javascript.
Each library consits of a number of functions that return a value of
the form
```
{"is_error": True/False, 
 "is_correct": True/False, 
 "ratio": 0.0 - 1.0, 
 "feedback": "Feedback to be set to the student."}
```
The flag `is_error` indicates an error condition.
The flag `is_correct`indicates whether the user's answer is considerd to be correct or not.
The floating point number "ratio" indicates how correct the answer is.  The value `1.0` means fully correct `0.0` means incorrect.
The string "feedback" is a piece of feedback to be displayed to the user.
 
Each directory `python` and `javascript` are structured as follows

* The file `cafe.py/js` contains all CAFE functions.
* Other files contain specific CAFE functions relevant to a specific topic.  For example, `asymtotics.py/js" contains functions for feedback on asymptotic notation. 

## Usage

Computer aided feedback may be called by any "algorithmic check"
`\algoc` or "algorithmic grading" `\algog` "cookie".

For example, the following problem includes an `\algoc` "cookie" that
gives the user feedback about the correctness of their answer by using
the `grade_bigoh` function.  In principle the code folowing \algoc
could include any python or javascript code (python in this case) but
it must set the variable `res` which stands for "result".

```

\begin{problem}
Give a closed-form solution in terms of big-Oh for the following recurrences

\ask
$W(n) = 2W(n/2) + n$

\sol
$O(n\lg{n})$

\algoc
res = grade_bigoh(ans, 'n * log(n)', 'n')
\end{problem}

``` 

The following example uses an `\algog` cookie, which is used only for grading.

```

\begin{problem}
Give a closed-form solution in terms of big-Oh for the following recurrences

\ask
$W(n) = 2W(n/2) + n$

\sol
$O(n\lg{n})$

\algog
res = grade_bigoh(ans, 'n * log(n)', 'n')

\end{problem}
```
