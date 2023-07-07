# **Sigmoid**

<br>

Sigmoid activations, also known as logistic activations, are a common type of activation function used in neural networks. They have an S-shaped curve that maps input values to a range between 0 and 1.

While sigmoid activations have been widely used in the past, they have certain drawbacks discussed in the literature. One drawback is the issue of sharp damp gradients during backpropagation from deeper hidden layers to the input layers. This means that as gradients propagate backward through the network, they can diminish rapidly, hindering effective learning and slowing down convergence.

Another drawback of sigmoid activations is gradient saturation, especially in the tails of the curve. When input values are extremely large or small, the gradients become close to zero, causing the vanishing gradient problem. This makes it challenging for the network to update weights effectively and learn from these layers.

Additionally, sigmoid activations are known for relatively slow convergence compared to other activation functions. This slow convergence can be attributed to the saturating nature of the sigmoid function, posing challenges for gradient-based optimization algorithms.

As a result of these drawbacks, sigmoid activations have been largely replaced by alternative activation functions, such as Rectified Linear Units (ReLUs) or variants like Leaky ReLUs. These alternatives address the issues of gradient saturation and slow convergence, offering improved performance and training dynamics.

In summary, sigmoid activations have been used in the past but suffer from drawbacks including sharp damp gradients, gradient saturation, and slow convergence. These limitations have led to the adoption of alternative activation functions that provide better performance and training dynamics in neural networks.

<br>

## **Definition**

$$Sigmoid(x)=\frac{1}{(1+e^{-x})}$$

$$Sigmoid\grave{(}x)=Sigmoid(x)(1-Sigmoid(x))$$

<br>

## **Properties**

- **Output Range between 0 and 1:** Sigmoid activations squash input values to a range between 0 and 1, which is beneficial in tasks where the output needs to represent probabilities or binary classifications.
- **Differentiable Everywhere:** Sigmoid functions are differentiable everywhere, allowing for the use of gradient-based optimization methods like backpropagation during training.
- **Smooth and Continuous Transitions:** Sigmoid activations offer smooth and continuous transitions between output values, which can be desirable in certain scenarios.
- **Interpretability as Probabilities:** The output of sigmoid activations can be interpreted as a probability or confidence score, making it easier to understand the model's predictions in classification tasks.

<br>

## **Advantages**

* Provides an intuitive probabilistic interpretation of the output, particularly in binary classification tasks.
* Differentiable everywhere enabling the use of gradient-based optimization methods like backpropagation, facilitating efficient learning and convergence.
* Offers smooth and continuous transitions between output values, promoting smooth learning dynamics in the network.

<br>

## **Limitations**

* Prone to the vanishing gradient problem, especially when input values are large. This can result in slow convergence and difficulties in learning deep neural networks.
* Saturates at the extreme ends of the curve, causing gradients to become very small. This hinders the learning process and limits the model's ability to capture more nuanced patterns in the data.
* Not centered around zero, potentially introducing a bias in the activations and affecting the symmetry and learning capability of the model.
* Calculating the exponentials required in the sigmoid function can be computationally expensive, particularly when dealing with large-scale neural networks.

<br>

### **Note:**

It's important to note that the advantages and limitations of using a particular activation function may vary depending on the specific context and problem at hand. Experimentation and evaluation on a case-by-case basis are recommended to determine the most suitable activation function for a given neural network.

<br>

---

<br>

## References

- [Sigmoid on Papers with Code](https://paperswithcode.com/method/sigmoid-activation)

<br>

---

The references provided above offer more in-depth information on the Sigmoid activation function and related research. Feel free to explore these resources for further insights and a deeper understanding of the topic.