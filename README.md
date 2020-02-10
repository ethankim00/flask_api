# iris

## Description
Api to make predictions on the Iris dataset. The dataset consists 4 measurements for 150 samples of 3 different varieties of Irises. 
## Usage
Takes a Post request containing one or more of the feature measurements and returns the predicted class as a string in JSON format

Example
```python
# Input
{
	"sepal_width":4,
	"sepal_length":3.5,
	"petal_width":2.5,
	"petal_length":4
}
```

```python
# Output
{
  "Prediction": "versicolor"
}
```

The application.py file can be run to initialize the server and requests submitted via postman. 

If one or more of the predictors is missing it is replaced with the sample mean. For example if no value is specified for sepal_width, the model will use the average value of 3.06 to return a prediction. If all values are missing then an error is raised. 

## Additional Information
1. 
The Iris dataset is very small and thus fitting models does not lead to any memory or computing issues. Handling datasets which do not fit into system memory would require some alternative aproaches. For development of a model one can use a smaller random sample of the data, allowing for rapid prototyping. The final model should then be fit on the full dataset using one of the following approaches. One is to use a cloud computing platform to provide the necessary memory. One could also progressively load the data or use a relational database. The streaming approach might require a choice of model that can handle iterative learning, for example one trained using stochastic gradient descent. 


