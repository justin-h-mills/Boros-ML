# **Parameterized ReLU (PReLU)**

<br>

PReLU is an activation function that extends [ReLU](/research_notes/activation_functions/rectifier_activation_functions/relu.md) by allowing for the learning of different slopes for negative input values. Unlike ReLU, which has a fixed slope of zero, PReLU adapts its slope during training.

The motivation behind PReLU is to capture complex patterns effectively by providing different types of nonlinearity for different layers. In experiments with CNNs, it has been observed that PReLU activations in the initial layers tend to have positive slopes closer to linear. This is beneficial for capturing low-level features like edges or textures that exhibit positive and negative responses. By respecting both positive and negative responses, PReLU captures a wider range of information in the early layers.

In contrast, deeper layers tend to have smaller slope coefficients in PReLU. This indicates that as the network becomes deeper, it focuses more on extracting high-level features crucial for accurate predictions. The smaller coefficients retain more information from previous layers while emphasizing discriminative representations.

The flexibility of PReLU in learning different slopes for each neuron allows it to adapt to the specific requirements of different layers. By learning diverse non-linearities, PReLU improves the performance and representational capacity of deep neural networks.

In summary, PReLU is an activation function that introduces learnable slopes for negative values. It captures a wide range of information, with positive slopes in early layers to respect positive and negative responses, and smaller coefficients in deeper layers to promote discriminative representations.

<br>

## **Definition**

$$PReLU(x_{i})=\left\{ \begin{array}{cl} x_{i} & : \ x_{i} \gt 0 \\ \alpha_{i} x_{i} & : \ x_{i} \le 0 \end{array} \right.$$

$$PReLU\grave{(}x_{i})=\left\{ \begin{array}{cl} 0 & : \ x_{i} \gt 0 \\ x_{i} & : \ x_{i} \le 0 \end{array} \right.$$

In the equation, we have $x_{i}$ as the input of the nonlinear activation function PReLU on the i-th channel, and $a_{i}$ as a coefficient that controls the slope of the negative part of the function. The subscript i in $a_{i}$ indicates that we allow the nonlinear activation to vary across different channels. When $a_{i}$ equals 0, the activation function reduces to ReLU.

<br>

## **Properties**

- **Adaptive Slopes:** PReLU allows for the learning of different slopes for negative inputs, adapting to the specific requirements of different layers.
- **Improved Representational Capacity:** The adaptive slopes increase the expressive power of the activation function, enabling the capture of a wider range of patterns and relationships in the data.
- **Gradient Flow:** By allowing non-zero slopes for negative inputs, PReLU mitigates the vanishing gradient problem and facilitates more effective gradient flow during backpropagation.
- **Information Retention:** Using smaller coefficients for deeper layers promotes the retention of important information from earlier layers while focusing on extracting more discriminative features.

<br>

## **Advantages**

* The adaptive slopes and improved gradient flow contribute to better learning and convergence in neural networks.
* Ability to learn diverse slopes enables the model to capture a wider range of patterns and relationships, enhancing its representational capacity.
* The use of smaller coefficients in deeper layers facilitates better information flow and hierarchical learning in the network.

<br>

## **Limitations**

* Introduces additional complexity by adding learnable parameters, which can result in a larger number of trainable parameters and increased computational requirements.
* The flexibility of PReLU to learn diverse slopes increases the risk of overfitting, especially when the number of training samples is limited. Regularization techniques may be necessary to mitigate this risk.
* Introduces additional hyperparameters that need to be tuned, such as the initial values or constraints on the slope parameters, requiring additional experimentation and computational resources.

<br>

### **Note:**

It's important to note that the advantages and limitations of using a particular activation function may vary depending on the specific context and problem at hand. Experimentation and evaluation on a case-by-case basis are recommended to determine the most suitable activation function for a given neural network.

<br>

---

<br>

## References

- [PReLU on Papers with Code](https://paperswithcode.com/method/prelu)
- [(Research Paper) Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/pdf/1502.01852v1.pdf)

<br>

---

The references provided above offer more in-depth information on the PReLU activation function and related research. Feel free to explore these resources for further insights and a deeper understanding of the topic.