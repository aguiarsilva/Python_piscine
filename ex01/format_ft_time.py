# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: baguiar- <baguiar-@student.42berlin.de>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/29 11:20:47 by baguiar-          #+#    #+#              #
#    Updated: 2026/04/29 11:51:56 by baguiar-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime, timedelta

now = datetime.now()
a = datetime(1970,1,1,00,00,00)
time_diff = (now-a).total_seconds()

print(f"Seconds since January 1, 1970: {"{:,}".format(time_diff)} or {"{0:.2E}".format(time_diff)} in scientific notation")
print(now.strftime("%b %d %Y"))

