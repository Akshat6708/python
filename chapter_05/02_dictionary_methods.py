

marks = {
    "akshat":78 , 
    "arin" : 93 , 
    "ajay" : 63 , 
    "aman " : 33, 
}
# print(marks)
# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"akshat": 99 , "arvind": 85})
# print(marks)

# print(marks.get("akshat2"))  # this give me none 
# print(marks["akshat2"]) # return a error so both are diffrents

# marks.clear()
# print(marks)

# copyMarks = marks.copy()
# print(copyMarks)

# popVal=marks.pop("akshat")
# print(marks)
# print(popVal)

popItem = marks.popitem()  # its remove last key value pair 
print(marks)
print(popItem)


