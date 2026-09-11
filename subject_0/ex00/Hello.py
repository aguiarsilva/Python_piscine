ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# modify list
ft_list[1] = "World!"

# modify tuple - immutable type in python
ft_tuple = ft_tuple[:1] + ("Germany",)

# modify set
ft_set.remove("tutu!")
ft_set.add("Berlin!")

# modify dict
ft_dict["Hello"] = "42 Berlin!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
