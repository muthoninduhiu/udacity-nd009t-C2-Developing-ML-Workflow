# **Machine Learning Workflow For Scones Unlimited On Amazon SageMaker**
### **Background**
Image Classifiers are used in the field of computer vision to identify the content of an image and it is used across a broad variety of industries, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms, and even in diagnostic medicine.

As an MLE, my goal is to ship a scalable and safe model. Once the model becomes available to other teams on-demand, it’s important that the model can scale to meet demand, and that safeguards are in place to monitor and control for drift or degraded performance.


#### **Project Steps Overview**
In this project:
* I will use AWS Sagemaker to build an image classification model that can tell bicycles apart from motorcycles. 
* Then deploy the model.
* Use AWS Lambda functions to build supporting services.
* Use AWS Step Functions to compose the model and services into an event-driven application


#### **Lambda Functions Inputs and Outputs**
1. Serialize the Image data

![Serialize Image](https://github.com/muthoninduhiu/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/serialize_image.png) 

3. Classify the image data and get inferences

![Classify Image](https://github.com/muthoninduhiu/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/classify_images.png)

4. Filter Inferences based on a particular threshold

![Filter Inferences](https://github.com/muthoninduhiu/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/filter_infered_results.png)

## Step Function 
To show the event driven application between the three lambda functions above by automating various tasks of Machine Learning process from Data Preparation, Model Creation, Model Deployment and Inference.

### Step Function Graphs
![Failed step function](https://github.com/muthoninduhiu/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/stepfunctions_graph_fail.png)                          ![SuccessFull Step Function](https://github.com/muthoninduhiu/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/stepfunctions_graph.png)

### Execution Flow of the Step Function with success
![Step Function Execution](https://github.com/muthoninduhiu/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/step_functions_execution_steps.png)
