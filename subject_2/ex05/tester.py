from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import cv2

array = ft_load("landscape.jpg")
cv2.imshow("Original", array)

cv2.imshow("Invert", ft_invert(array))
cv2.imshow("Red", ft_red(array))
cv2.imshow("Green", ft_green(array))
cv2.imshow("Blue", ft_blue(array))
cv2.imshow("Grey", ft_grey(array))

cv2.waitKey(0)
cv2.destroyAllWindows()

print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
