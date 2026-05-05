# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baguiar- <baguiar-@student.42berlin.de>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/29 11:09:04 by baguiar-          #+#    #+#              #
#    Updated: 2026/04/29 11:09:11 by baguiar-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#modify list
ft_list[1] = "World!"

#modify tuple - immutable type in python
del ft_tuple
ft_tuple = ("Hello", "France!")

#modify set
ft_set.remove("tutu!")
ft_set.add("Paris!")

#modify dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
