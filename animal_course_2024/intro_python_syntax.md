# Python introduction

Python is very user friendly programming languga with simple syntax. Python also provides extensive libraries for multiple problems. This gives Python the ultimate power for creating project very fast with a steep learning curve.

## Python basics

Python basics can be found all over the internet. A high quality that targets the area of data and image analysis can be found here: [PoL Bio-Image Analysis Training School - Early Career Track](https://biapol.github.io/PoL-BioImage-Analysis-TS-Early-Career-Track/intro.html#acknowledgements) and more resorces can be found at [BiAPoL github](https://github.com/BiAPoL).

### Variables and data types

1. Variables 
* 1.1 Integer
       
    Integers are whole numbers without a fractional part. In Python, you can create an integer by simply assigning a number without a decimal point to a variable. For example:

    ```python
    my_integer = 10
    print("The variable is", type(my_integer), "and the value is", my_integer, ".")
    ```

    This will output:

    ```
    The variable is <class 'int'> and the value is 10.
    ```
* 1.2 String
       
    A string in Python is a sequence of characters enclosed within single quotes (' '), double quotes (" ").
    
    ```python
    my_name = "Daniel"
    print(f"My name is {my_name}.")
    ```

    This will output:

    ```
    My name is Daniel.
    ```

* 1.3 Other types

    There are other types of variables that Python can process. It is assign automatically unless you define the type of the variable, for instance, integer or float.

    You can also use more complicated datatypes such as a list:

     ```python
    list_of_animals = [3, 6, 8, 10, 12]
    print(f"The 3rd measured sample was the animal {list_of_animals[2]}.")
    ```
    
    This will output:

    ```
    The 3rd measured sample was the animal 8.
    ```
    or more as a dictionary wich is a set of keys and coresponding values.

    ```python
    dic_of_treatment = {
        "control": [1, 2, 3],
        "treatment_1": [4, 5, 6],
        "treatment_2": [7, 8, 9]
    }
    print(f"The samples in control group are {dic_of_treatment['control']}.")
    print(f"The samples in treatment 1 are {dic_of_treatment['treatment_1']}.")
    print(f"The samples in treatment 2 are {dic_of_treatment['treatment_2']}.")
    ```

    This will output:

    ```
    The samples in control group are [1, 2, 3].
    The samples in treatment 1 are [4, 5, 6].
    The samples in treatment 2 are [7, 8, 9].
    ```

2. Importing libraries

    The library is a collection of modules and functions that are written to complete a specific task.
    
    ```python
    # import Python library for plotting
    import matplotlib.pyplot as plt
    # create x and y dataset
    x_vals = [-2, -1, 0, 1, 2]
    y_vals = [-4, -2, 0, 2, 4]
    # plot the resutls
    plt.plot(x_vals, y_vals)
    plt.show()
    ```
    This will output:

    ![Plot of the dataset](./static/images/plot_example.png)

3. Looping

    Run the code until a statement or condition end the loop. The most common loops are "for" loop and "while" loop.

    ```python
    # create the dictionary of the animals
    dic_of_treatment = {
        "control": [1, 2, 3],
        "treatment_1": [4, 5, 6],
        "treatment_2": [7, 8, 9]
    }
    # loop the dictionary and print the groups
    for key in dic_of treatment:
        print(key)
    ```

    This will output:

    ```
    control
    treatment_1
    treatment_2
    ```




