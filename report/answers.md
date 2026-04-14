# Answers

Question 1: How does a for loop work with custom objects?

Answer:
A for loop calls __iter__ to get an iterator, then repeatedly calls __next__.
This continues until StopIteration is raised.

Limitation:
If StopIteration is not raised, the loop becomes infinite.

---

Question 2: What methods are required for iteration?

Answer:
__iter__ and __next__.
They define how iteration starts and proceeds.

---

Question 3: How does the with statement work internally?

Answer:
It calls __enter__ at the beginning and __exit__ at the end.
This controls setup and cleanup.

---

Question 4: When is __exit__ called?

Answer:
__exit__ is always called after the block finishes, even if an error occurs.

Limitation:
If __exit__ is missing, cleanup is not guaranteed.

---

Question 5: What problem do descriptors solve?

Answer:
Descriptors control attribute access and validation.
They ensure correct data is stored.

---

Question 6: What happens if a descriptor is not used?

Answer:
Attributes can be assigned freely without validation.
This may lead to invalid data.

---

Question 7: Why is direct iteration preferred?

Answer:
It is more readable and Pythonic.
It avoids manual index handling.

Limitation:
Index-based loops are more error-prone.
