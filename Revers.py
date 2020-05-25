def reverse(st):
    n=st.split()
    n.reverse()
    return " ".join(n)
test="Hello World"
print(reverse(test))