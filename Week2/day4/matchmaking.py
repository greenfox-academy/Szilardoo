# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve","Ashley","Bözsi","Kat","Jane"]
boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"]
order = []
for i in range(5):
    order += [girls[i]]
    order += [boys[i]]
print(order)
