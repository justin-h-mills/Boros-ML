# **Hyperbolic Tangent (Tanh)**

<br>

The tanh function is a non-linear activation function commonly used in neural networks. It maps a real-valued number to the range [-1, 1]. One key advantage of tanh over the sigmoid function is that its output is zero-centered, meaning that the average output of the function is closer to zero.

The zero-centered property of tanh makes it desirable in many practical scenarios. When used as an activation function in neural networks, having a zero-centered output can help alleviate the issue of gradient vanishing and facilitate learning. With a zero-centered output, the positive and negative inputs to subsequent layers can balance each other, allowing for better propagation of gradients during backpropagation and promoting efficient learning.

In contrast, the sigmoid function, another commonly used activation function, does not have a zero-centered output. This lack of zero-centering can result in consistently positive or negative gradients, which can slow down learning and hinder convergence.

Due to its zero-centered output and improved gradient propagation properties, the tanh non-linearity is often preferred over the sigmoid non-linearity in practice. It is commonly used in various tasks, including natural language processing, image classification, and recurrent neural networks.

In summary, the tanh function is a non-linear activation function that maps a real-valued input to the range [-1, 1]. Its zero-centered output makes it preferable to the sigmoid function in many practical scenarios, as it helps mitigate gradient vanishing and facilitates efficient learning in neural networks.

<br>

## **Definition**

$$Tanh(x) = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$$

$$Tanh\grave{(}x) = 1-Tanh(x)^2$$

<br>

## **Properties**

- **Introduction of Non-Linearity:** Tanh introduces non-linearity into the neural network, enabling it to model complex relationships and capture intricate patterns in the data.
- **Zero-Centered Output:** The output of tanh is zero-centered, which helps alleviate the issue of gradient vanishing and facilitates better gradient propagation during backpropagation. This can lead to more effective learning and convergence in neural networks.
- **Wider Output Range:** Compared to the sigmoid function, tanh has a wider output range from -1 to 1. This increased range allows for more diverse representations of data, potentially improving the model's ability to capture and differentiate between different levels of activation.
- **Symmetry around the Origin:** Tanh is symmetric around the origin (0), which can be advantageous in certain scenarios where symmetric behavior is desired or expected.

<br>

## **Advantages**

* The zero-centered output of tanh helps alleviate the issue of gradient vanishing, facilitating better gradient propagation during backpropagation. This can lead to more effective learning and convergence in neural networks.
* Introduces non-linearity, enabling the neural network to model complex relationships and capture intricate patterns in the data.
* The wider output range of tanh allows for more diverse representations of data, potentially improving the model's ability to capture and differentiate between different levels of activation.

<br>

## **Limitations**

* Saturates at the extreme ends of the input range (-1 and 1), leading to the vanishing gradient problem, especially in deep neural networks or long sequences. This saturation can cause slower learning or hinder the model's ability to capture fine-grained details in the data.
* The output of tanh is limited to the range [-1, 1], which may not be suitable for all types of data or tasks. In some cases, a wider or narrower range of activations may be more appropriate.
* Similar to other activation functions, tanh does not have a direct probabilistic interpretation or clear thresholding behavior. This can make it harder to interpret the behavior of the model or provide meaningful insights into the predictions.

<br>

### **Note:**

It's important to note that the advantages and limitations of using a particular activation function may vary depending on the specific context and problem at hand. Experimentation and evaluation on a case-by-case basis are recommended to determine the most suitable activation function for a given neural network.

<br>

---

<br>

## References

- [Tanh on Papers with Code](https://paperswithcode.com/method/tanh-activation)

<br>

---

The references provided above offer more in-depth information on the Tanh activation function and related research. Feel free to explore these resources for further insights and a deeper understanding of the topic.