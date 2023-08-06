# coco_utils
A set of utility functions to process object detection (coco) datasets.


## Summary
- **COCO wrapper**,  Use coco_utils COCO function which has extra properties like `label_counts`, `label_presence`, `img_wise_counts`, `label_names`, `label_names_available`, `count_images`. 

```python
from coco_utils.coco import COCO
x = COCO("data/annotations/instances_val2017.json")
```

- **`plot labels`** function is used to plot and save `labels_correlogram.jpg` and `labels.jpg` files. 

```python
from coco_utils.plots import plot_coco_labels
loc = "data/annotations/instances_val2017.json"
plot_coco_labels(loc, "data/outputs/")
```


## Summary of set up

- Clone the repo and do `poetry install`. To install poetry on your [system/server](https://github.com/prakashjayy/fullstack_dl/issues/17). 

> How to run tests ?
- TODO 

> How to use ?
- `poetry add coco_utils` or `pip install coco_utils`

> Deployment instructions
- `poetry build` & `poetry publish` 


## Who do I talk to?

> Repo owner or admin
- Prakash Vanapalli

> Other community or team contact.
