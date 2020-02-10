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
