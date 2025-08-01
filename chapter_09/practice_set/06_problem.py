
with open("06_log.txt") as f:
    content = f.read()
word = "python"
if(word in content):
    print(f"yes , {word} is present in the content")
else:
    print(f"No , {word} is not present in the content")