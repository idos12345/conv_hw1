r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**
Increasing k on our case improved generaliztion for unseen data until k=5, for k > 5
increasing k leaded to decreasing of the accuracy.
We can assume that ~5 closest neighbors of most of the test samples placed close enough to indicates the label
of the test sample while using bigger k pushed far and unrelated "neighbors" to the prediction which led to 
lower accuracy on unseen data. 


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""
# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**
That's due to the fact that if W separates then so is $\alpha W$. So W can always be normalized to fit any $\Delta$.
"""

part3_q2 = r"""
**Your answer:**
1. We can see in the visualization that the bright areas are similar to the digits. 
So the model's prediction is based on the area where the bright areas of the image (the image) 
and the bright areas of the classifier are aligned.
The mistakes it made are reasonable since the overlap area of the digit in the image with
the "wrong" classifier is large.

2. In KNN we use distance to classify, which means we take all features with the same weight. 
In SVM ob the other hand, the different pixels are given weight according to their contribution to the classification.
"""

part3_q3 = r"""
**Your answer:**
1. The learning rate seems to be good since the convergence time was low, 
and the loss did seem to get very close to its minimum value. The decrease was stable.
If the learning rate is to low, it could take many more epochs for the loss to get to its minima.
If the learning rate is too high, then the minima might be missed and the graph would look very unstable.

2. Slightly overfitted to the training set.
That's because the train loss graph is under the test loss and the train accuracy is above the test accuracy. 
"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
