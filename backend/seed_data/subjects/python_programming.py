subject_data = {
    "name": "Python Programming",
    "description": "Master Python fundamentals and advanced concepts step by step",
    "icon": "🐍",
    "color": "bg-blue-500",
    "levels": [
        {
            "name": "Variables & Data Types",
            "description": "Learn about Python variables, strings, numbers, and basic data types",
            "quizzes": [
                {
                    "title": "Python Variables & Data Types Quiz",
                    "description": "Test your understanding of Python variables and basic data types",
                    "questions": [
                        {
                            "text": "Which of the following is NOT a valid Python variable name?",
                            "choices": [
                                {"text": "my_var", "is_correct": False},
                                {"text": "2variable", "is_correct": True},
                                {"text": "_private", "is_correct": False},
                                {"text": "Variable", "is_correct": False}
                            ],
                            "explanation": "Variable names in Python cannot start with a number. They must start with a letter or underscore.",
                            "resources": [
                                {"title": "Python Variable Naming Rules", "url": "https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator"},
                                {"title": "PEP 8 Style Guide", "url": "https://pep8.org/"}
                            ]
                        },
                        {
                            "text": "What is the data type of the value 3.14 in Python?",
                            "choices": [
                                {"text": "int", "is_correct": False},
                                {"text": "float", "is_correct": True},
                                {"text": "double", "is_correct": False},
                                {"text": "decimal", "is_correct": False}
                            ],
                            "explanation": "In Python, decimal numbers are represented as float data type.",
                            "resources": [
                                {"title": "Python Numeric Types", "url": "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex"}
                            ]
                        },
                        {
                            "text": "Which of the following is a valid way to create a string in Python?",
                            "choices": [
                                {"text": "str = 'Hello'", "is_correct": False},
                                {"text": "str = \"Hello\"", "is_correct": False},
                                {"text": "str = '''Hello'''", "is_correct": False},
                                {"text": "All of the above", "is_correct": True}
                            ],
                            "explanation": "Python supports single quotes, double quotes, and triple quotes for strings.",
                            "resources": [
                                {"title": "Python Strings", "url": "https://docs.python.org/3/tutorial/introduction.html#strings"}
                            ]
                        },
                        {
                            "text": "What is the output of: print(type([]))",
                            "choices": [
                                {"text": "<class 'list'>", "is_correct": True},
                                {"text": "<class 'array'>", "is_correct": False},
                                {"text": "<class 'tuple'>", "is_correct": False},
                                {"text": "<class 'set'>", "is_correct": False}
                            ],
                            "explanation": "Empty square brackets create a list in Python.",
                            "resources": [
                                {"title": "Python Lists", "url": "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists"}
                            ]
                        },
                        {
                            "text": "Which of the following is a boolean value in Python?",
                            "choices": [
                                {"text": "True", "is_correct": True},
                                {"text": "true", "is_correct": False},
                                {"text": "TRUE", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "Python boolean values are True and False (case-sensitive).",
                            "resources": [
                                {"title": "Python Booleans", "url": "https://docs.python.org/3/library/stdtypes.html#boolean-values"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Python Data Types Challenge",
                    "description": "Test your knowledge of Python's built-in data types and type conversion.",
                    "questions": [
                        {
                            "text": "Which of the following is a mutable data type in Python?",
                            "choices": [
                                {"text": "tuple", "is_correct": False},
                                {"text": "list", "is_correct": True},
                                {"text": "str", "is_correct": False},
                                {"text": "int", "is_correct": False}
                            ],
                            "explanation": "Lists are mutable, while tuples, strings, and ints are immutable.",
                            "resources": [
                                {"title": "Python Data Types", "url": "https://docs.python.org/3/library/stdtypes.html"}
                            ]
                        },
                        {
                            "text": "What is the result of int('10.5') in Python?",
                            "choices": [
                                {"text": "10", "is_correct": False},
                                {"text": "10.5", "is_correct": False},
                                {"text": "Error", "is_correct": True},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "int('10.5') raises a ValueError because '10.5' is not a valid integer string.",
                            "resources": [
                                {"title": "Python int()", "url": "https://docs.python.org/3/library/functions.html#int"}
                            ]
                        },
                        {
                            "text": "Which function returns the length of a string in Python?",
                            "choices": [
                                {"text": "size()", "is_correct": False},
                                {"text": "count()", "is_correct": False},
                                {"text": "len()", "is_correct": True},
                                {"text": "length()", "is_correct": False}
                            ],
                            "explanation": "len() returns the length of a string, list, or other collection.",
                            "resources": [
                                {"title": "Python len()", "url": "https://docs.python.org/3/library/functions.html#len"}
                            ]
                        },
                        {
                            "text": "What is the output of: print(type(3.0))",
                            "choices": [
                                {"text": "<class 'float'>", "is_correct": True},
                                {"text": "<class 'int'>", "is_correct": False},
                                {"text": "<class 'str'>", "is_correct": False},
                                {"text": "<class 'complex'>", "is_correct": False}
                            ],
                            "explanation": "3.0 is a float in Python.",
                            "resources": [
                                {"title": "Python float", "url": "https://docs.python.org/3/library/stdtypes.html#float"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a valid string method in Python?",
                            "choices": [
                                {"text": "upper()", "is_correct": False},
                                {"text": "lower()", "is_correct": False},
                                {"text": "capitalize()", "is_correct": False},
                                {"text": "reverse()", "is_correct": True}
                            ],
                            "explanation": "reverse() is not a string method; use slicing or reversed().",
                            "resources": [
                                {"title": "Python String Methods", "url": "https://docs.python.org/3/library/stdtypes.html#string-methods"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Python Variables Practice Quiz",
                    "description": "Practice your skills with Python variable assignment, naming, and scope.",
                    "questions": [
                        {
                            "text": "Which of the following is a valid variable name in Python?",
                            "choices": [
                                {"text": "my-var", "is_correct": False},
                                {"text": "my_var", "is_correct": True},
                                {"text": "2var", "is_correct": False},
                                {"text": "var2", "is_correct": True}
                            ],
                            "explanation": "Variable names can contain letters, numbers, and underscores, but cannot start with a number or contain dashes.",
                            "resources": [
                                {"title": "Python Variable Names", "url": "https://docs.python.org/3/reference/lexical_analysis.html#identifiers"}
                            ]
                        },
                        {
                            "text": "What is the scope of a variable defined inside a function?",
                            "choices": [
                                {"text": "Global", "is_correct": False},
                                {"text": "Local", "is_correct": True},
                                {"text": "Module", "is_correct": False},
                                {"text": "Class", "is_correct": False}
                            ],
                            "explanation": "Variables defined inside a function are local to that function.",
                            "resources": [
                                {"title": "Python Variable Scope", "url": "https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces"}
                            ]
                        },
                        {
                            "text": "What is the output of: x = 10; def foo(): x = 5; print(x); foo()",
                            "choices": [
                                {"text": "10", "is_correct": False},
                                {"text": "5", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "The function foo defines its own local x, so it prints 5.",
                            "resources": [
                                {"title": "Python Local Variables", "url": "https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces"}
                            ]
                        },
                        {
                            "text": "Which keyword is used to declare a global variable inside a function?",
                            "choices": [
                                {"text": "global", "is_correct": True},
                                {"text": "nonlocal", "is_correct": False},
                                {"text": "static", "is_correct": False},
                                {"text": "extern", "is_correct": False}
                            ],
                            "explanation": "The global keyword is used to declare global variables inside a function.",
                            "resources": [
                                {"title": "Python global Keyword", "url": "https://docs.python.org/3/reference/simple_stmts.html#the-global-statement"}
                            ]
                        },
                        {
                            "text": "What is the output of: x = 1; def foo(): global x; x = 2; foo(); print(x)",
                            "choices": [
                                {"text": "1", "is_correct": False},
                                {"text": "2", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "The global keyword allows the function to modify the global variable x.",
                            "resources": [
                                {"title": "Python global Keyword", "url": "https://docs.python.org/3/reference/simple_stmts.html#the-global-statement"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Control Structures",
            "description": "Master if statements, loops, and conditional logic",
            "quizzes": [
                {
                    "title": "Python Control Structures Quiz",
                    "description": "Test your understanding of Python control flow and loops",
                    "questions": [
                        {
                            "text": "What is the output of: for i in range(3): print(i)",
                            "choices": [
                                {"text": "0,1,2", "is_correct": True},
                                {"text": "1,2,3", "is_correct": False},
                                {"text": "0,1,2,3", "is_correct": False},
                                {"text": "1,2", "is_correct": False}
                            ],
                            "explanation": "range(3) generates numbers from 0 to 2 (exclusive of 3).",
                            "resources": [
                                {"title": "Python for Loops", "url": "https://docs.python.org/3/tutorial/controlflow.html#for-statements"}
                            ]
                        },
                        {
                            "text": "Which statement is used to skip the current iteration in a Python loop?",
                            "choices": [
                                {"text": "break", "is_correct": False},
                                {"text": "continue", "is_correct": True},
                                {"text": "pass", "is_correct": False},
                                {"text": "skip", "is_correct": False}
                            ],
                            "explanation": "continue skips the current iteration and continues with the next one.",
                            "resources": [
                                {"title": "Python break and continue", "url": "https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements"}
                            ]
                        },
                        {
                            "text": "What is the result of: x = 5; print('Even' if x % 2 == 0 else 'Odd')",
                            "choices": [
                                {"text": "Even", "is_correct": False},
                                {"text": "Odd", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "This is a ternary operator. Since 5 % 2 == 1 (not 0), it prints 'Odd'.",
                            "resources": [
                                {"title": "Python Conditional Expressions", "url": "https://docs.python.org/3/reference/expressions.html#conditional-expressions"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Python Loop Practice Quiz",
                    "description": "Practice your skills with Python loops, including for and while loops.",
                    "questions": [
                        {
                            "text": "What is the output of: for i in range(5): print(i)",
                            "choices": [
                                {"text": "0,1,2,3,4", "is_correct": True},
                                {"text": "1,2,3,4,5", "is_correct": False},
                                {"text": "0,1,2,3,4,5", "is_correct": False},
                                {"text": "1,2,3,4", "is_correct": False}
                            ],
                            "explanation": "range(5) generates numbers from 0 to 4 (inclusive).",
                            "resources": [
                                {"title": "Python for Loops", "url": "https://docs.python.org/3/tutorial/controlflow.html#for-statements"}
                            ]
                        },
                        {
                            "text": "Which of the following is a valid way to create a while loop in Python?",
                            "choices": [
                                {"text": "while i < 10: print(i)", "is_correct": False},
                                {"text": "while i < 10: print(i)", "is_correct": False},
                                {"text": "while i < 10: print(i)", "is_correct": False},
                                {"text": "All of the above", "is_correct": True}
                            ],
                            "explanation": "Python supports single quotes, double quotes, and triple quotes for strings.",
                            "resources": [
                                {"title": "Python while Loops", "url": "https://docs.python.org/3/tutorial/controlflow.html#while-statements"}
                            ]
                        },
                        {
                            "text": "What is the output of: i = 0; while i < 5: print(i); i += 1",
                            "choices": [
                                {"text": "0,1,2,3,4", "is_correct": True},
                                {"text": "1,2,3,4,5", "is_correct": False},
                                {"text": "0,1,2,3,4,5", "is_correct": False},
                                {"text": "1,2,3,4", "is_correct": False}
                            ],
                            "explanation": "The while loop prints numbers from 0 to 4.",
                            "resources": [
                                {"title": "Python while Loops", "url": "https://docs.python.org/3/tutorial/controlflow.html#while-statements"}
                            ]
                        },
                        {
                            "text": "Which keyword is used to break out of a loop in Python?",
                            "choices": [
                                {"text": "break", "is_correct": True},
                                {"text": "continue", "is_correct": False},
                                {"text": "pass", "is_correct": False},
                                {"text": "exit", "is_correct": False}
                            ],
                            "explanation": "The break keyword is used to exit a loop immediately.",
                            "resources": [
                                {"title": "Python break and continue", "url": "https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements"}
                            ]
                        },
                        {
                            "text": "What is the output of: i = 0; while i < 5: print(i); i += 1; if i == 3: break",
                            "choices": [
                                {"text": "0,1,2,3", "is_correct": True},
                                {"text": "1,2,3,4", "is_correct": False},
                                {"text": "0,1,2,3,4", "is_correct": False},
                                {"text": "1,2,3,4,5", "is_correct": False}
                            ],
                            "explanation": "The while loop prints numbers from 0 to 2 and breaks at 3.",
                            "resources": [
                                {"title": "Python while Loops", "url": "https://docs.python.org/3/tutorial/controlflow.html#while-statements"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Functions & Modules",
            "description": "Create reusable code with functions and organize with modules",
            "quizzes": [
                {
                    "title": "Python Functions & Modules Quiz",
                    "description": "Test your understanding of Python functions and module system",
                    "questions": [
                        {
                            "text": "What is the output of: def func(x, y=10): return x + y; print(func(5))",
                            "choices": [
                                {"text": "15", "is_correct": True},
                                {"text": "5", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "y has a default value of 10, so func(5) returns 5 + 10 = 15.",
                            "resources": [
                                {"title": "Python Functions", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        },
                        {
                            "text": "Which keyword is used to import a specific function from a module?",
                            "choices": [
                                {"text": "import", "is_correct": False},
                                {"text": "from", "is_correct": True},
                                {"text": "include", "is_correct": False},
                                {"text": "require", "is_correct": False}
                            ],
                            "explanation": "from keyword is used to import specific items from a module.",
                            "resources": [
                                {"title": "Python Import System", "url": "https://docs.python.org/3/reference/import.html"}
                            ]
                        },
                        {
                            "text": "What is the output of: def func(): return 1, 2; x, y = func(); print(x)",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "(1, 2)", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function returns a tuple (1, 2), which is unpacked into x and y.",
                            "resources": [
                                {"title": "Python Multiple Return Values", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Python Function Practice Quiz",
                    "description": "Practice your skills with Python functions, including default arguments and return values.",
                    "questions": [
                        {
                            "text": "What is the output of: def func(x, y=5): return x + y; print(func(3))",
                            "choices": [
                                {"text": "8", "is_correct": True},
                                {"text": "3", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "y has a default value of 5, so func(3) returns 3 + 5 = 8.",
                            "resources": [
                                {"title": "Python Functions", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a valid way to call a function in Python?",
                            "choices": [
                                {"text": "func(1, 2)", "is_correct": False},
                                {"text": "func(1, 2, 3)", "is_correct": False},
                                {"text": "func(1, y=2)", "is_correct": False},
                                {"text": "func(y=2, x=1)", "is_correct": True}
                            ],
                            "explanation": "Keyword arguments can be passed in any order, but positional arguments must be before keyword arguments.",
                            "resources": [
                                {"title": "Python Function Arguments", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        },
                        {
                            "text": "What is the output of: def func(): return 1, 2; x, y = func(); print(x)",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "(1, 2)", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function returns a tuple (1, 2), which is unpacked into x and y.",
                            "resources": [
                                {"title": "Python Multiple Return Values", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        },
                        {
                            "text": "What is the output of: def func(): return 1, 2; x, y = func(); print(x)",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "(1, 2)", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function returns a tuple (1, 2), which is unpacked into x and y.",
                            "resources": [
                                {"title": "Python Multiple Return Values", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        },
                        {
                            "text": "What is the output of: def func(): return 1, 2; x, y = func(); print(x)",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "(1, 2)", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function returns a tuple (1, 2), which is unpacked into x and y.",
                            "resources": [
                                {"title": "Python Multiple Return Values", "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Object-Oriented Programming",
            "description": "Understand classes, objects, inheritance, and OOP principles",
            "quizzes": [
                {
                    "title": "Python OOP Quiz",
                    "description": "Test your understanding of Python OOP concepts",
                    "questions": [
                        {
                            "text": "What is the output of: class MyClass: pass; obj = MyClass(); print(type(obj))",
                            "choices": [
                                {"text": "<class 'MyClass'>", "is_correct": True},
                                {"text": "<class 'object'>", "is_correct": False},
                                {"text": "<class 'type'>", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "obj is an instance of MyClass, so type(obj) returns the class type.",
                            "resources": [
                                {"title": "Python Classes", "url": "https://docs.python.org/3/tutorial/classes.html"}
                            ]
                        },
                        {
                            "text": "Which method is called when an object is created?",
                            "choices": [
                                {"text": "__init__", "is_correct": True},
                                {"text": "__new__", "is_correct": False},
                                {"text": "__create__", "is_correct": False},
                                {"text": "__construct__", "is_correct": False}
                            ],
                            "explanation": "__init__ is the constructor method that is called when an object is instantiated.",
                            "resources": [
                                {"title": "Python __init__ Method", "url": "https://docs.python.org/3/reference/datamodel.html#object.__init__"}
                            ]
                        },
                        {
                            "text": "What is inheritance in Python?",
                            "choices": [
                                {"text": "A class can inherit from multiple parent classes", "is_correct": False},
                                {"text": "A class can inherit from one parent class", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "Neither A nor B", "is_correct": False}
                            ],
                            "explanation": "Python supports both single and multiple inheritance.",
                            "resources": [
                                {"title": "Python Inheritance", "url": "https://docs.python.org/3/tutorial/classes.html#inheritance"}
                            ]
                        },
                        {
                            "text": "What is the output of: class Parent: def method(self): return 'Parent'; class Child(Parent): pass; c = Child(); print(c.method())",
                            "choices": [
                                {"text": "Parent", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False},
                                {"text": "Child", "is_correct": False}
                            ],
                            "explanation": "Child inherits the method from Parent, so c.method() returns 'Parent'.",
                            "resources": [
                                {"title": "Python Method Inheritance", "url": "https://docs.python.org/3/tutorial/classes.html#inheritance"}
                            ]
                        },
                        {
                            "text": "What is encapsulation in OOP?",
                            "choices": [
                                {"text": "Bundling data and methods that operate on that data", "is_correct": False},
                                {"text": "Hiding implementation details", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "Creating multiple objects", "is_correct": False}
                            ],
                            "explanation": "Encapsulation bundles data and methods together and hides implementation details.",
                            "resources": [
                                {"title": "Python Encapsulation", "url": "https://docs.python.org/3/tutorial/classes.html"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Python OOP Practice Quiz",
                    "description": "Practice your skills with Python OOP concepts, including inheritance and encapsulation.",
                    "questions": [
                        {
                            "text": "What is the output of: class MyClass: pass; obj = MyClass(); print(type(obj))",
                            "choices": [
                                {"text": "<class 'MyClass'>", "is_correct": True},
                                {"text": "<class 'object'>", "is_correct": False},
                                {"text": "<class 'type'>", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "obj is an instance of MyClass, so type(obj) returns the class type.",
                            "resources": [
                                {"title": "Python Classes", "url": "https://docs.python.org/3/tutorial/classes.html"}
                            ]
                        },
                        {
                            "text": "Which method is called when an object is created?",
                            "choices": [
                                {"text": "__init__", "is_correct": True},
                                {"text": "__new__", "is_correct": False},
                                {"text": "__create__", "is_correct": False},
                                {"text": "__construct__", "is_correct": False}
                            ],
                            "explanation": "__init__ is the constructor method that is called when an object is instantiated.",
                            "resources": [
                                {"title": "Python __init__ Method", "url": "https://docs.python.org/3/reference/datamodel.html#object.__init__"}
                            ]
                        },
                        {
                            "text": "What is inheritance in Python?",
                            "choices": [
                                {"text": "A class can inherit from multiple parent classes", "is_correct": False},
                                {"text": "A class can inherit from one parent class", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "Neither A nor B", "is_correct": False}
                            ],
                            "explanation": "Python supports both single and multiple inheritance.",
                            "resources": [
                                {"title": "Python Inheritance", "url": "https://docs.python.org/3/tutorial/classes.html#inheritance"}
                            ]
                        },
                        {
                            "text": "What is the output of: class Parent: def method(self): return 'Parent'; class Child(Parent): pass; c = Child(); print(c.method())",
                            "choices": [
                                {"text": "Parent", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False},
                                {"text": "Child", "is_correct": False}
                            ],
                            "explanation": "Child inherits the method from Parent, so c.method() returns 'Parent'.",
                            "resources": [
                                {"title": "Python Method Inheritance", "url": "https://docs.python.org/3/tutorial/classes.html#inheritance"}
                            ]
                        },
                        {
                            "text": "What is encapsulation in OOP?",
                            "choices": [
                                {"text": "Bundling data and methods that operate on that data", "is_correct": False},
                                {"text": "Hiding implementation details", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "Creating multiple objects", "is_correct": False}
                            ],
                            "explanation": "Encapsulation bundles data and methods together and hides implementation details.",
                            "resources": [
                                {"title": "Python Encapsulation", "url": "https://docs.python.org/3/tutorial/classes.html"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Advanced Topics",
            "description": "Explore decorators, generators, context managers, and more",
            "quizzes": [
                {
                    "title": "Python Advanced Topics Quiz",
                    "description": "Test your understanding of Python advanced concepts",
                    "questions": [
                        {
                            "text": "What is a decorator in Python?",
                            "choices": [
                                {"text": "A function that modifies another function", "is_correct": True},
                                {"text": "A class that wraps another class", "is_correct": False},
                                {"text": "A module import statement", "is_correct": False},
                                {"text": "A type annotation", "is_correct": False}
                            ],
                            "explanation": "A decorator is a function that takes another function and extends its behavior.",
                            "resources": [
                                {"title": "Python Decorators", "url": "https://docs.python.org/3/glossary.html#term-decorator"}
                            ]
                        },
                        {
                            "text": "What is the output of: def gen(): yield 1; yield 2; g = gen(); print(next(g))",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "This is a generator function. next(g) returns the first yielded value, which is 1.",
                            "resources": [
                                {"title": "Python Generators", "url": "https://docs.python.org/3/tutorial/classes.html#generators"}
                            ]
                        },
                        {
                            "text": "What is the purpose of 'with' statement in Python?",
                            "choices": [
                                {"text": "Context management", "is_correct": True},
                                {"text": "Exception handling", "is_correct": False},
                                {"text": "Loop control", "is_correct": False},
                                {"text": "Function definition", "is_correct": False}
                            ],
                            "explanation": "The 'with' statement is used for context management, ensuring proper resource cleanup.",
                            "resources": [
                                {"title": "Python Context Managers", "url": "https://docs.python.org/3/reference/compound_stmts.html#with"}
                            ]
                        },
                        {
                            "text": "What is the output of: try: 1/0; except ZeroDivisionError: print('Error'); else: print('Success')",
                            "choices": [
                                {"text": "Error", "is_correct": True},
                                {"text": "Success", "is_correct": False},
                                {"text": "Both", "is_correct": False},
                                {"text": "Neither", "is_correct": False}
                            ],
                            "explanation": "1/0 raises a ZeroDivisionError, so the except block executes and prints 'Error'.",
                            "resources": [
                                {"title": "Python Exception Handling", "url": "https://docs.python.org/3/tutorial/errors.html"}
                            ]
                        },
                        {
                            "text": "What is the purpose of __slots__ in Python classes?",
                            "choices": [
                                {"text": "To save memory", "is_correct": False},
                                {"text": "To restrict attributes", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "To improve performance", "is_correct": False}
                            ],
                            "explanation": "__slots__ restricts the attributes a class can have and saves memory by not creating a dictionary for each instance.",
                            "resources": [
                                {"title": "Python __slots__", "url": "https://docs.python.org/3/reference/datamodel.html#object.__slots__"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Python Advanced Topics Practice Quiz",
                    "description": "Practice your skills with Python advanced concepts, including decorators and context managers.",
                    "questions": [
                        {
                            "text": "What is a decorator in Python?",
                            "choices": [
                                {"text": "A function that modifies another function", "is_correct": True},
                                {"text": "A class that wraps another class", "is_correct": False},
                                {"text": "A module import statement", "is_correct": False},
                                {"text": "A type annotation", "is_correct": False}
                            ],
                            "explanation": "A decorator is a function that takes another function and extends its behavior.",
                            "resources": [
                                {"title": "Python Decorators", "url": "https://docs.python.org/3/glossary.html#term-decorator"}
                            ]
                        },
                        {
                            "text": "What is the output of: def gen(): yield 1; yield 2; g = gen(); print(next(g))",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "None", "is_correct": False}
                            ],
                            "explanation": "This is a generator function. next(g) returns the first yielded value, which is 1.",
                            "resources": [
                                {"title": "Python Generators", "url": "https://docs.python.org/3/tutorial/classes.html#generators"}
                            ]
                        },
                        {
                            "text": "What is the purpose of 'with' statement in Python?",
                            "choices": [
                                {"text": "Context management", "is_correct": True},
                                {"text": "Exception handling", "is_correct": False},
                                {"text": "Loop control", "is_correct": False},
                                {"text": "Function definition", "is_correct": False}
                            ],
                            "explanation": "The 'with' statement is used for context management, ensuring proper resource cleanup.",
                            "resources": [
                                {"title": "Python Context Managers", "url": "https://docs.python.org/3/reference/compound_stmts.html#with"}
                            ]
                        },
                        {
                            "text": "What is the output of: try: 1/0; except ZeroDivisionError: print('Error'); else: print('Success')",
                            "choices": [
                                {"text": "Error", "is_correct": True},
                                {"text": "Success", "is_correct": False},
                                {"text": "Both", "is_correct": False},
                                {"text": "Neither", "is_correct": False}
                            ],
                            "explanation": "1/0 raises a ZeroDivisionError, so the except block executes and prints 'Error'.",
                            "resources": [
                                {"title": "Python Exception Handling", "url": "https://docs.python.org/3/tutorial/errors.html"}
                            ]
                        },
                        {
                            "text": "What is the purpose of __slots__ in Python classes?",
                            "choices": [
                                {"text": "To save memory", "is_correct": False},
                                {"text": "To restrict attributes", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "To improve performance", "is_correct": False}
                            ],
                            "explanation": "__slots__ restricts the attributes a class can have and saves memory by not creating a dictionary for each instance.",
                            "resources": [
                                {"title": "Python __slots__", "url": "https://docs.python.org/3/reference/datamodel.html#object.__slots__"}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
} 