# Task 1

Suppose we want to find an element in an array (get its index). We can do this simply
by going through all the elements. But what if the array is already sorted? In this
case, you can use binary search. The principle is simple: first we take the element
in the middle and compare it with the one we want to find. If the central element
is larger than ours, we consider the array to the left of the central one, and if
it is larger - to the right and repeat this until we find our element.
