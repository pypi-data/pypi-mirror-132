# FCMpy: A package for Constructing and Analysing Fuzzy Cognitive Maps in Python.
<div align = justify>

The fcmpy is Python package for automatically generating causal weights for fuzzy cognitive maps based on qualitative inputs (by using fuzzy logic), optimizing the FCM connection matrix via Machine Learning Algorithms and testing <em>what-if</em> scenarios. The package includes the following submodules:

* ExpertFcm
* Simulation
* Intervention
* ML

## Installation
FCMpy requires python >=3.8.1 and depends on:

* pandas>=1.0.3
* numpy>=numpy==1.18.2
* scikit-fuzzy>=0.4.2
* tqdm>=4.50.2
* openpyxl

The latest version can be installed by:

```
pip install fcmpy
```

Alternatively, you can install it from source or develop this package, you can fork and clone this repository then install FCMpy by running:

```
py -m pip install --user --upgrade setuptools wheel
py setup.py sdist bdist_wheel
py -m pip install install e . 
```

You can run the unittest for the package as follows:

```
py -m unittest discover unittests
```

## Documentation and tutorials
<a href="https://maxiuw.github.io/fcmpyhtml"> Tutorial and documentation </a> Learn how to use our library by following available tutorials and documentation!<br>

## License

Please read LICENSE.txt in this directory.

</div>