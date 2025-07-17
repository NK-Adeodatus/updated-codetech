subject_data = {
    "name": "C Programming",
    "description": "Build strong foundations in C programming language",
    "icon": "⚙️",
    "color": "bg-green-500",
    "levels": [
        {
            "name": "C Basics",
            "description": "Variables, data types, and operators",
            "quizzes": [
                {
                    "title": "C Basics Quiz",
                    "description": "Test your understanding of C variables, data types, and operators.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax to declare an integer variable in C?",
                            "choices": [
                                {"text": "int x;", "is_correct": True},
                                {"text": "integer x;", "is_correct": False},
                                {"text": "x int;", "is_correct": False},
                                {"text": "var x;", "is_correct": False}
                            ],
                            "explanation": "'int x;' is the correct way to declare an integer variable in C.",
                            "resources": [
                                {"title": "C Variables", "url": "https://www.tutorialspoint.com/cprogramming/c_variables.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: printf(\"%d\", 5 + 2 * 3);",
                            "choices": [
                                {"text": "21", "is_correct": False},
                                {"text": "11", "is_correct": True},
                                {"text": "17", "is_correct": False},
                                {"text": "15", "is_correct": False}
                            ],
                            "explanation": "Multiplication has higher precedence, so 2*3=6, then 5+6=11.",
                            "resources": [
                                {"title": "C Operator Precedence", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"}
                            ]
                        },
                        {
                            "text": "Which data type is used to store a single character in C?",
                            "choices": [
                                {"text": "char", "is_correct": True},
                                {"text": "string", "is_correct": False},
                                {"text": "character", "is_correct": False},
                                {"text": "text", "is_correct": False}
                            ],
                            "explanation": "char is used to store a single character in C.",
                            "resources": [
                                {"title": "C Data Types", "url": "https://www.tutorialspoint.com/cprogramming/c_data_types.htm"}
                            ]
                        },
                        {
                            "text": "What is the size of an int data type in C (typically)?",
                            "choices": [
                                {"text": "2 bytes", "is_correct": False},
                                {"text": "4 bytes", "is_correct": True},
                                {"text": "8 bytes", "is_correct": False},
                                {"text": "1 byte", "is_correct": False}
                            ],
                            "explanation": "An int is typically 4 bytes on most modern systems.",
                            "resources": [
                                {"title": "C Data Types", "url": "https://www.tutorialspoint.com/cprogramming/c_data_types.htm"}
                            ]
                        },
                        {
                            "text": "Which operator is used to get the address of a variable?",
                            "choices": [
                                {"text": "&", "is_correct": True},
                                {"text": "*", "is_correct": False},
                                {"text": "#", "is_correct": False},
                                {"text": "%", "is_correct": False}
                            ],
                            "explanation": "The & operator is used to get the address of a variable.",
                            "resources": [
                                {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Data Types & Operators Challenge",
                    "description": "Challenge your knowledge of C data types and operators.",
                    "questions": [
                        {
                            "text": "Which of the following is a floating-point data type in C?",
                            "choices": [
                                {"text": "float", "is_correct": True},
                                {"text": "int", "is_correct": False},
                                {"text": "char", "is_correct": False},
                                {"text": "long", "is_correct": False}
                            ],
                            "explanation": "float is a floating-point data type.",
                            "resources": [
                                {"title": "C Data Types", "url": "https://www.tutorialspoint.com/cprogramming/c_data_types.htm"}
                            ]
                        },
                        {
                            "text": "What is the result of: int x = 10 / 3; printf(\"%d\", x);",
                            "choices": [
                                {"text": "3", "is_correct": True},
                                {"text": "3.33", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False}
                            ],
                            "explanation": "Integer division truncates the decimal part.",
                            "resources": [
                                {"title": "C Operators", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"}
                            ]
                        },
                        {
                            "text": "Which operator is used for logical AND in C?",
                            "choices": [
                                {"text": "&&", "is_correct": True},
                                {"text": "&", "is_correct": False},
                                {"text": "and", "is_correct": False},
                                {"text": "||", "is_correct": False}
                            ],
                            "explanation": "&& is the logical AND operator.",
                            "resources": [
                                {"title": "C Logical Operators", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a valid C variable name?",
                            "choices": [
                                {"text": "_var", "is_correct": False},
                                {"text": "2var", "is_correct": True},
                                {"text": "var2", "is_correct": False},
                                {"text": "var_2", "is_correct": False}
                            ],
                            "explanation": "Variable names cannot start with a number.",
                            "resources": [
                                {"title": "C Variable Names", "url": "https://www.tutorialspoint.com/cprogramming/c_variables.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int a = 5, b = 2; printf(\"%d\", a % b);",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "2.5", "is_correct": False}
                            ],
                            "explanation": "The modulus operator (%) returns the remainder of integer division.",
                            "resources": [
                                {"title": "C Modulus Operator", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Variable Declarations Practice",
                    "description": "Practice your skills with C variable declarations and initialization.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct way to initialize a float variable in C?",
                            "choices": [
                                {"text": "float x = 3.14;", "is_correct": True},
                                {"text": "float x = '3.14';", "is_correct": False},
                                {"text": "float x = \"3.14\";", "is_correct": False},
                                {"text": "float x = int(3.14);", "is_correct": False}
                            ],
                            "explanation": "float x = 3.14; is the correct way to initialize a float variable.",
                            "resources": [
                                {"title": "C Variable Initialization", "url": "https://www.tutorialspoint.com/cprogramming/c_variables.htm"}
                            ]
                        },
                        {
                            "text": "Which keyword is used to define a constant variable in C?",
                            "choices": [
                                {"text": "const", "is_correct": True},
                                {"text": "constant", "is_correct": False},
                                {"text": "define", "is_correct": False},
                                {"text": "static", "is_correct": False}
                            ],
                            "explanation": "const is used to define a constant variable.",
                            "resources": [
                                {"title": "C Constants", "url": "https://www.tutorialspoint.com/cprogramming/c_constants.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 5; x += 2; printf(\"%d\", x);",
                            "choices": [
                                {"text": "7", "is_correct": True},
                                {"text": "5", "is_correct": False},
                                {"text": "2", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "x += 2 increments x by 2, so x becomes 7.",
                            "resources": [
                                {"title": "C Assignment Operators", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a valid C data type?",
                            "choices": [
                                {"text": "int", "is_correct": False},
                                {"text": "float", "is_correct": False},
                                {"text": "real", "is_correct": True},
                                {"text": "char", "is_correct": False}
                            ],
                            "explanation": "real is not a valid C data type.",
                            "resources": [
                                {"title": "C Data Types", "url": "https://www.tutorialspoint.com/cprogramming/c_data_types.htm"}
                            ]
                        },
                        {
                            "text": "Which operator is used for incrementing a variable by 1 in C?",
                            "choices": [
                                {"text": "++", "is_correct": True},
                                {"text": "+=", "is_correct": False},
                                {"text": "--", "is_correct": False},
                                {"text": "=+", "is_correct": False}
                            ],
                            "explanation": "++ is the increment operator in C.",
                            "resources": [
                                {"title": "C Increment Operator", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Control Flow",
            "description": "If, else, switch, and loops in C",
            "quizzes": [
                {
                    "title": "Control Flow Quiz",
                    "description": "Test your knowledge of C conditional statements and loops.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a simple if statement?",
                            "choices": [
                                {"text": "if (condition) { statements; }", "is_correct": True},
                                {"text": "if (condition) statements;", "is_correct": False},
                                {"text": "if condition { statements; }", "is_correct": False},
                                {"text": "if condition statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a simple if statement is 'if (condition) { statements; }'.",
                            "resources": [
                                {"title": "C Conditional Statements", "url": "https://www.tutorialspoint.com/cprogramming/c_if_else.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 10; if (x > 5) printf(\"%d\", x);",
                            "choices": [
                                {"text": "10", "is_correct": True},
                                {"text": "5", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False}
                            ],
                            "explanation": "The if statement executes if the condition is true.",
                            "resources": [
                                {"title": "C If Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_if_else.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a switch statement?",
                            "choices": [
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; break; }", "is_correct": True},
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; }", "is_correct": False},
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; }", "is_correct": False},
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; }", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a switch statement is 'switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; break; }'.",
                            "resources": [
                                {"title": "C Switch Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_switch.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 5; switch (x) { case 1: printf(\"%d\", 1); break; case 2: printf(\"%d\", 2); break; default: printf(\"%d\", 0); break; }",
                            "choices": [
                                {"text": "1", "is_correct": False},
                                {"text": "2", "is_correct": False},
                                {"text": "0", "is_correct": True},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The switch statement evaluates the expression and executes the case that matches.",
                            "resources": [
                                {"title": "C Switch Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_switch.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a while loop?",
                            "choices": [
                                {"text": "while (condition) { statements; }", "is_correct": True},
                                {"text": "while (condition) statements;", "is_correct": False},
                                {"text": "while condition { statements; }", "is_correct": False},
                                {"text": "while condition statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a while loop is 'while (condition) { statements; }'.",
                            "resources": [
                                {"title": "C Loops", "url": "https://www.tutorialspoint.com/cprogramming/c_while_loop.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Looping & Branching Challenge",
                    "description": "Challenge your skills with C loops and branching.",
                    "questions": [
                        {
                            "text": "What is the output of: int x = 0; while (x < 5) { printf(\"%d \", x); x++; }",
                            "choices": [
                                {"text": "0 1 2 3 4", "is_correct": True},
                                {"text": "0 1 2 3 4 5", "is_correct": False},
                                {"text": "0 1 2 3 4 5 6", "is_correct": False},
                                {"text": "0 1 2 3 4 5 6 7", "is_correct": False}
                            ],
                            "explanation": "The while loop prints numbers from 0 to 4.",
                            "resources": [
                                {"title": "C Loops", "url": "https://www.tutorialspoint.com/cprogramming/c_while_loop.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 10; do { printf(\"%d \", x); x--; } while (x > 0);",
                            "choices": [
                                {"text": "10 9 8 7 6 5 4 3 2 1", "is_correct": True},
                                {"text": "10 9 8 7 6 5 4 3 2 1 0", "is_correct": False},
                                {"text": "10 9 8 7 6 5 4 3 2 1 0 1", "is_correct": False},
                                {"text": "10 9 8 7 6 5 4 3 2 1 0 1 2", "is_correct": False}
                            ],
                            "explanation": "The do-while loop prints numbers from 10 to 1.",
                            "resources": [
                                {"title": "C Loops", "url": "https://www.tutorialspoint.com/cprogramming/c_while_loop.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a for loop?",
                            "choices": [
                                {"text": "for (initialization; condition; increment) { statements; }", "is_correct": True},
                                {"text": "for (initialization; condition; increment) statements;", "is_correct": False},
                                {"text": "for (initialization; condition; increment) statements;", "is_correct": False},
                                {"text": "for (initialization; condition; increment) statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a for loop is 'for (initialization; condition; increment) { statements; }'.",
                            "resources": [
                                {"title": "C Loops", "url": "https://www.tutorialspoint.com/cprogramming/c_for_loop.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: for (int i = 0; i < 5; i++) { printf(\"%d \", i); }",
                            "choices": [
                                {"text": "0 1 2 3 4", "is_correct": True},
                                {"text": "0 1 2 3 4 5", "is_correct": False},
                                {"text": "0 1 2 3 4 5 6", "is_correct": False},
                                {"text": "0 1 2 3 4 5 6 7", "is_correct": False}
                            ],
                            "explanation": "The for loop prints numbers from 0 to 4.",
                            "resources": [
                                {"title": "C Loops", "url": "https://www.tutorialspoint.com/cprogramming/c_for_loop.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a break statement?",
                            "choices": [
                                {"text": "break;", "is_correct": True},
                                {"text": "break;", "is_correct": False},
                                {"text": "break;", "is_correct": False},
                                {"text": "break;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a break statement is 'break;'.",
                            "resources": [
                                {"title": "C Break Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_break_statement.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Conditional Statements Practice",
                    "description": "Practice your skills with C conditional statements.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a simple if statement?",
                            "choices": [
                                {"text": "if (condition) { statements; }", "is_correct": True},
                                {"text": "if (condition) statements;", "is_correct": False},
                                {"text": "if condition { statements; }", "is_correct": False},
                                {"text": "if condition statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a simple if statement is 'if (condition) { statements; }'.",
                            "resources": [
                                {"title": "C Conditional Statements", "url": "https://www.tutorialspoint.com/cprogramming/c_if_else.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 10; if (x > 5) printf(\"%d\", x);",
                            "choices": [
                                {"text": "10", "is_correct": True},
                                {"text": "5", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False}
                            ],
                            "explanation": "The if statement executes if the condition is true.",
                            "resources": [
                                {"title": "C If Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_if_else.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a switch statement?",
                            "choices": [
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; break; }", "is_correct": True},
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; }", "is_correct": False},
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; }", "is_correct": False},
                                {"text": "switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; }", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a switch statement is 'switch (expression) { case 1: statements; break; case 2: statements; break; default: statements; break; }'.",
                            "resources": [
                                {"title": "C Switch Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_switch.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 5; switch (x) { case 1: printf(\"%d\", 1); break; case 2: printf(\"%d\", 2); break; default: printf(\"%d\", 0); break; }",
                            "choices": [
                                {"text": "1", "is_correct": False},
                                {"text": "2", "is_correct": False},
                                {"text": "0", "is_correct": True},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The switch statement evaluates the expression and executes the case that matches.",
                            "resources": [
                                {"title": "C Switch Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_switch.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a break statement?",
                            "choices": [
                                {"text": "break;", "is_correct": True},
                                {"text": "break;", "is_correct": False},
                                {"text": "break;", "is_correct": False},
                                {"text": "break;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a break statement is 'break;'.",
                            "resources": [
                                {"title": "C Break Statement", "url": "https://www.tutorialspoint.com/cprogramming/c_break_statement.htm"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Functions",
            "description": "Functions, parameters, and return values",
            "quizzes": [
                {
                    "title": "Functions Quiz",
                    "description": "Test your knowledge of C functions and their parameters.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a function definition?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list) { statements; }", "is_correct": True},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function definition is 'return_type function_name(parameter_list) { statements; }'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int add(int a, int b) { return a + b; } printf(\"%d\", add(5, 3));",
                            "choices": [
                                {"text": "8", "is_correct": True},
                                {"text": "5", "is_correct": False},
                                {"text": "3", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function 'add' is defined and called correctly.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function call?",
                            "choices": [
                                {"text": "function_name(argument_list);", "is_correct": True},
                                {"text": "function_name argument_list;", "is_correct": False},
                                {"text": "function_name(argument_list);", "is_correct": False},
                                {"text": "function_name(argument_list);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function call is 'function_name(argument_list);'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 10; int y = 20; printf(\"%d\", add(x, y));",
                            "choices": [
                                {"text": "30", "is_correct": True},
                                {"text": "10", "is_correct": False},
                                {"text": "20", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function 'add' is called with arguments x and y.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function prototype?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list);", "is_correct": True},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function prototype is 'return_type function_name(parameter_list);'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Function Parameters & Return Challenge",
                    "description": "Challenge your skills with C function parameters and return values.",
                    "questions": [
                        {
                            "text": "What is the output of: int add(int a, int b) { return a + b; } int x = 10; int y = 20; printf(\"%d\", add(x, y));",
                            "choices": [
                                {"text": "30", "is_correct": True},
                                {"text": "10", "is_correct": False},
                                {"text": "20", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function 'add' is called with arguments x and y.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function prototype?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list);", "is_correct": True},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function prototype is 'return_type function_name(parameter_list);'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 10; int y = 20; printf(\"%d\", add(x, y));",
                            "choices": [
                                {"text": "30", "is_correct": True},
                                {"text": "10", "is_correct": False},
                                {"text": "20", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function 'add' is called with arguments x and y.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function call?",
                            "choices": [
                                {"text": "function_name(argument_list);", "is_correct": True},
                                {"text": "function_name argument_list;", "is_correct": False},
                                {"text": "function_name(argument_list);", "is_correct": False},
                                {"text": "function_name(argument_list);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function call is 'function_name(argument_list);'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function definition?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list) { statements; }", "is_correct": True},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function definition is 'return_type function_name(parameter_list) { statements; }'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Function Implementation Practice",
                    "description": "Practice your skills with C function implementation.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a function definition?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list) { statements; }", "is_correct": True},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function definition is 'return_type function_name(parameter_list) { statements; }'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int add(int a, int b) { return a + b; } int x = 10; int y = 20; printf(\"%d\", add(x, y));",
                            "choices": [
                                {"text": "30", "is_correct": True},
                                {"text": "10", "is_correct": False},
                                {"text": "20", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The function 'add' is called with arguments x and y.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function call?",
                            "choices": [
                                {"text": "function_name(argument_list);", "is_correct": True},
                                {"text": "function_name argument_list;", "is_correct": False},
                                {"text": "function_name(argument_list);", "is_correct": False},
                                {"text": "function_name(argument_list);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function call is 'function_name(argument_list);'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function prototype?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list);", "is_correct": True},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False},
                                {"text": "return_type function_name(parameter_list);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function prototype is 'return_type function_name(parameter_list);'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a function definition?",
                            "choices": [
                                {"text": "return_type function_name(parameter_list) { statements; }", "is_correct": True},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False},
                                {"text": "return_type function_name(parameter_list) statements;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a function definition is 'return_type function_name(parameter_list) { statements; }'.",
                            "resources": [
                                {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Pointers & Arrays",
            "description": "Pointers, arrays, and memory management",
            "quizzes": [
                {
                    "title": "Pointers & Arrays Quiz",
                    "description": "Test your knowledge of C pointers and arrays.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a pointer declaration?",
                            "choices": [
                                {"text": "int *ptr;", "is_correct": True},
                                {"text": "int ptr;", "is_correct": False},
                                {"text": "int * ptr;", "is_correct": False},
                                {"text": "int *ptr;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a pointer declaration is 'int *ptr;'.",
                            "resources": [
                                {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int x = 10; int *ptr = &x; printf(\"%d\", *ptr);",
                            "choices": [
                                {"text": "10", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "100", "is_correct": False}
                            ],
                            "explanation": "The pointer 'ptr' is initialized with the address of 'x' and then dereferenced to get the value.",
                            "resources": [
                                {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for an array declaration?",
                            "choices": [
                                {"text": "int arr[5];", "is_correct": True},
                                {"text": "int arr 5;", "is_correct": False},
                                {"text": "int arr[5];", "is_correct": False},
                                {"text": "int arr 5;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for an array declaration is 'int arr[5];'.",
                            "resources": [
                                {"title": "C Arrays", "url": "https://www.tutorialspoint.com/cprogramming/c_arrays.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int arr[5] = {1, 2, 3, 4, 5}; printf(\"%d \", arr[2]);",
                            "choices": [
                                {"text": "3", "is_correct": True},
                                {"text": "1", "is_correct": False},
                                {"text": "2", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The array 'arr' is initialized and the third element (index 2) is printed.",
                            "resources": [
                                {"title": "C Arrays", "url": "https://www.tutorialspoint.com/cprogramming/c_arrays.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a pointer to an array?",
                            "choices": [
                                {"text": "int *arr_ptr = arr;", "is_correct": True},
                                {"text": "int arr_ptr = arr;", "is_correct": False},
                                {"text": "int *arr_ptr = &arr;", "is_correct": False},
                                {"text": "int *arr_ptr = arr;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a pointer to an array is 'int *arr_ptr = arr;'.",
                            "resources": [
                                {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Memory Management Challenge",
                    "description": "Challenge your skills with C memory management.",
                    "questions": [
                        {
                            "text": "What is the output of: int *ptr = (int *)malloc(sizeof(int)); *ptr = 10; printf(\"%d\", *ptr); free(ptr);",
                            "choices": [
                                {"text": "10", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "100", "is_correct": False}
                            ],
                            "explanation": "The 'malloc' function allocates memory and 'free' deallocates it.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'malloc'?",
                            "choices": [
                                {"text": "malloc(size);", "is_correct": True},
                                {"text": "malloc size;", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'malloc' is 'malloc(size);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int *ptr = (int *)malloc(sizeof(int)); *ptr = 10; printf(\"%d\", *ptr); free(ptr);",
                            "choices": [
                                {"text": "10", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "100", "is_correct": False}
                            ],
                            "explanation": "The 'malloc' function allocates memory and 'free' deallocates it.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'malloc'?",
                            "choices": [
                                {"text": "malloc(size);", "is_correct": True},
                                {"text": "malloc size;", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'malloc' is 'malloc(size);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'free'?",
                            "choices": [
                                {"text": "free(ptr);", "is_correct": True},
                                {"text": "free ptr;", "is_correct": False},
                                {"text": "free(ptr);", "is_correct": False},
                                {"text": "free(ptr);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'free' is 'free(ptr);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Array Manipulation Practice",
                    "description": "Practice your skills with C array manipulation.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for an array declaration?",
                            "choices": [
                                {"text": "int arr[5];", "is_correct": True},
                                {"text": "int arr 5;", "is_correct": False},
                                {"text": "int arr[5];", "is_correct": False},
                                {"text": "int arr 5;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for an array declaration is 'int arr[5];'.",
                            "resources": [
                                {"title": "C Arrays", "url": "https://www.tutorialspoint.com/cprogramming/c_arrays.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: int arr[5] = {1, 2, 3, 4, 5}; printf(\"%d \", arr[2]);",
                            "choices": [
                                {"text": "3", "is_correct": True},
                                {"text": "1", "is_correct": False},
                                {"text": "2", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "The array 'arr' is initialized and the third element (index 2) is printed.",
                            "resources": [
                                {"title": "C Arrays", "url": "https://www.tutorialspoint.com/cprogramming/c_arrays.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a pointer to an array?",
                            "choices": [
                                {"text": "int *arr_ptr = arr;", "is_correct": True},
                                {"text": "int arr_ptr = arr;", "is_correct": False},
                                {"text": "int *arr_ptr = &arr;", "is_correct": False},
                                {"text": "int *arr_ptr = arr;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a pointer to an array is 'int *arr_ptr = arr;'.",
                            "resources": [
                                {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'malloc'?",
                            "choices": [
                                {"text": "malloc(size);", "is_correct": True},
                                {"text": "malloc size;", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'malloc' is 'malloc(size);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'free'?",
                            "choices": [
                                {"text": "free(ptr);", "is_correct": True},
                                {"text": "free ptr;", "is_correct": False},
                                {"text": "free(ptr);", "is_correct": False},
                                {"text": "free(ptr);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'free' is 'free(ptr);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Strings & Structures",
            "description": "String manipulation and structs",
            "quizzes": [
                {
                    "title": "Strings & Structures Quiz",
                    "description": "Test your knowledge of C strings and structs.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a string declaration?",
                            "choices": [
                                {"text": "char str[] = \"Hello\";", "is_correct": True},
                                {"text": "char str = \"Hello\";", "is_correct": False},
                                {"text": "char str[] = \"Hello\";", "is_correct": False},
                                {"text": "char str = \"Hello\";", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a string declaration is 'char str[] = \"Hello\";'.",
                            "resources": [
                                {"title": "C Strings", "url": "https://www.tutorialspoint.com/cprogramming/c_strings.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: char str[] = \"Hello\"; printf(\"%s\", str);",
                            "choices": [
                                {"text": "Hello", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "HelloHello", "is_correct": False},
                                {"text": "HelloHelloHello", "is_correct": False}
                            ],
                            "explanation": "The string 'str' is printed using 'printf'.",
                            "resources": [
                                {"title": "C Strings", "url": "https://www.tutorialspoint.com/cprogramming/c_strings.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a struct definition?",
                            "choices": [
                                {"text": "struct student { int id; char name[20]; };", "is_correct": True},
                                {"text": "struct student { int id; char name[20]; };", "is_correct": False},
                                {"text": "struct student { int id; char name[20]; };", "is_correct": False},
                                {"text": "struct student { int id; char name[20]; };", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a struct definition is 'struct student { int id; char name[20]; };'.",
                            "resources": [
                                {"title": "C Structures", "url": "https://www.tutorialspoint.com/cprogramming/c_structures.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: struct student s1 = { 1, \"John\" }; printf(\"%d %s\", s1.id, s1.name);",
                            "choices": [
                                {"text": "1 John", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0 0", "is_correct": False},
                                {"text": "1 1", "is_correct": False}
                            ],
                            "explanation": "The struct 's1' is initialized and printed.",
                            "resources": [
                                {"title": "C Structures", "url": "https://www.tutorialspoint.com/cprogramming/c_structures.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a union definition?",
                            "choices": [
                                {"text": "union data { int x; char y; };", "is_correct": True},
                                {"text": "union data { int x; char y; };", "is_correct": False},
                                {"text": "union data { int x; char y; };", "is_correct": False},
                                {"text": "union data { int x; char y; };", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a union definition is 'union data { int x; char y; };'.",
                            "resources": [
                                {"title": "C Unions", "url": "https://www.tutorialspoint.com/cprogramming/c_unions.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "String Functions Challenge",
                    "description": "Challenge your skills with C string functions.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for 'strcpy'?",
                            "choices": [
                                {"text": "strcpy(dest, src);", "is_correct": True},
                                {"text": "strcpy dest, src;", "is_correct": False},
                                {"text": "strcpy(dest, src);", "is_correct": False},
                                {"text": "strcpy(dest, src);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'strcpy' is 'strcpy(dest, src);'.",
                            "resources": [
                                {"title": "C String Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_string_functions.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: char str1[] = \"Hello\"; char str2[] = \"World\"; strcpy(str1, str2); printf(\"%s\", str1);",
                            "choices": [
                                {"text": "World", "is_correct": True},
                                {"text": "Hello", "is_correct": False},
                                {"text": "HelloHello", "is_correct": False},
                                {"text": "HelloWorld", "is_correct": False}
                            ],
                            "explanation": "The 'strcpy' function copies 'str2' to 'str1'.",
                            "resources": [
                                {"title": "C String Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_string_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'strcat'?",
                            "choices": [
                                {"text": "strcat(dest, src);", "is_correct": True},
                                {"text": "strcat dest, src;", "is_correct": False},
                                {"text": "strcat(dest, src);", "is_correct": False},
                                {"text": "strcat(dest, src);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'strcat' is 'strcat(dest, src);'.",
                            "resources": [
                                {"title": "C String Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_string_functions.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: char str1[] = \"Hello\"; char str2[] = \"World\"; strcat(str1, str2); printf(\"%s\", str1);",
                            "choices": [
                                {"text": "HelloWorld", "is_correct": True},
                                {"text": "Hello", "is_correct": False},
                                {"text": "HelloHello", "is_correct": False},
                                {"text": "HelloWorldWorld", "is_correct": False}
                            ],
                            "explanation": "The 'strcat' function appends 'str2' to 'str1'.",
                            "resources": [
                                {"title": "C String Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_string_functions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'strlen'?",
                            "choices": [
                                {"text": "strlen(str);", "is_correct": True},
                                {"text": "strlen str;", "is_correct": False},
                                {"text": "strlen(str);", "is_correct": False},
                                {"text": "strlen(str);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'strlen' is 'strlen(str);'.",
                            "resources": [
                                {"title": "C String Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_string_functions.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Structs & Unions Practice",
                    "description": "Practice your skills with C structs and unions.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for a struct definition?",
                            "choices": [
                                {"text": "struct student { int id; char name[20]; };", "is_correct": True},
                                {"text": "struct student { int id; char name[20]; };", "is_correct": False},
                                {"text": "struct student { int id; char name[20]; };", "is_correct": False},
                                {"text": "struct student { int id; char name[20]; };", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a struct definition is 'struct student { int id; char name[20]; };'.",
                            "resources": [
                                {"title": "C Structures", "url": "https://www.tutorialspoint.com/cprogramming/c_structures.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: struct student s1 = { 1, \"John\" }; printf(\"%d %s\", s1.id, s1.name);",
                            "choices": [
                                {"text": "1 John", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0 0", "is_correct": False},
                                {"text": "1 1", "is_correct": False}
                            ],
                            "explanation": "The struct 's1' is initialized and printed.",
                            "resources": [
                                {"title": "C Structures", "url": "https://www.tutorialspoint.com/cprogramming/c_structures.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for a union definition?",
                            "choices": [
                                {"text": "union data { int x; char y; };", "is_correct": True},
                                {"text": "union data { int x; char y; };", "is_correct": False},
                                {"text": "union data { int x; char y; };", "is_correct": False},
                                {"text": "union data { int x; char y; };", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for a union definition is 'union data { int x; char y; };'.",
                            "resources": [
                                {"title": "C Unions", "url": "https://www.tutorialspoint.com/cprogramming/c_unions.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'malloc'?",
                            "choices": [
                                {"text": "malloc(size);", "is_correct": True},
                                {"text": "malloc size;", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False},
                                {"text": "malloc(size);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'malloc' is 'malloc(size);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'free'?",
                            "choices": [
                                {"text": "free(ptr);", "is_correct": True},
                                {"text": "free ptr;", "is_correct": False},
                                {"text": "free(ptr);", "is_correct": False},
                                {"text": "free(ptr);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'free' is 'free(ptr);'.",
                            "resources": [
                                {"title": "C Memory Management", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "File I/O & Advanced",
            "description": "File operations and advanced concepts",
            "quizzes": [
                {
                    "title": "File I/O & Advanced Quiz",
                    "description": "Test your knowledge of C file operations and advanced concepts.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for 'fopen'?",
                            "choices": [
                                {"text": "fopen(\"filename\", \"mode\");", "is_correct": True},
                                {"text": "fopen filename, mode;", "is_correct": False},
                                {"text": "fopen(\"filename\", \"mode\");", "is_correct": False},
                                {"text": "fopen(\"filename\", \"mode\");", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'fopen' is 'fopen(\"filename\", \"mode\");'.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: FILE *fp = fopen(\"test.txt\", \"w\"); fclose(fp);",
                            "choices": [
                                {"text": "Error", "is_correct": False},
                                {"text": "Success", "is_correct": True},
                                {"text": "0", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "The 'fopen' function opens a file and 'fclose' closes it.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'fprintf'?",
                            "choices": [
                                {"text": "fprintf(fp, \"format\", args);", "is_correct": True},
                                {"text": "fprintf fp, \"format\", args;", "is_correct": False},
                                {"text": "fprintf(fp, \"format\", args);", "is_correct": False},
                                {"text": "fprintf(fp, \"format\", args);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'fprintf' is 'fprintf(fp, \"format\", args);'.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: FILE *fp = fopen(\"test.txt\", \"w\"); fprintf(fp, \"Hello\"); fclose(fp);",
                            "choices": [
                                {"text": "Hello", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "The 'fprintf' function writes to the file and 'fclose' closes it.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'fscanf'?",
                            "choices": [
                                {"text": "fscanf(fp, \"format\", &var);", "is_correct": True},
                                {"text": "fscanf fp, \"format\", &var;", "is_correct": False},
                                {"text": "fscanf(fp, \"format\", &var);", "is_correct": False},
                                {"text": "fscanf(fp, \"format\", &var);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'fscanf' is 'fscanf(fp, \"format\", &var);'.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Preprocessor & Headers Challenge",
                    "description": "Challenge your skills with C preprocessor and headers.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for '#include'?",
                            "choices": [
                                {"text": "#include <header.h>;", "is_correct": True},
                                {"text": "#include header.h;", "is_correct": False},
                                {"text": "#include <header.h>;", "is_correct": False},
                                {"text": "#include <header.h>;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for '#include' is '#include <header.h>;'.",
                            "resources": [
                                {"title": "C Preprocessor", "url": "https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: #define PI 3.14; printf(\"%f\", PI);",
                            "choices": [
                                {"text": "3.14", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "The '#define' directive defines a constant.",
                            "resources": [
                                {"title": "C Preprocessor", "url": "https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for '#ifdef'?",
                            "choices": [
                                {"text": "#ifdef CONDITION; statements; #endif;", "is_correct": True},
                                {"text": "#ifdef CONDITION; statements; #endif;", "is_correct": False},
                                {"text": "#ifdef CONDITION; statements; #endif;", "is_correct": False},
                                {"text": "#ifdef CONDITION; statements; #endif;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for '#ifdef' is '#ifdef CONDITION; statements; #endif;'.",
                            "resources": [
                                {"title": "C Preprocessor", "url": "https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: #ifdef DEBUG; printf(\"Debug mode\"); #endif;",
                            "choices": [
                                {"text": "Debug mode", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "The '#ifdef' directive includes statements if the condition is defined.",
                            "resources": [
                                {"title": "C Preprocessor", "url": "https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for '#ifndef'?",
                            "choices": [
                                {"text": "#ifndef CONDITION; statements; #endif;", "is_correct": True},
                                {"text": "#ifndef CONDITION; statements; #endif;", "is_correct": False},
                                {"text": "#ifndef CONDITION; statements; #endif;", "is_correct": False},
                                {"text": "#ifndef CONDITION; statements; #endif;", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for '#ifndef' is '#ifndef CONDITION; statements; #endif;'.",
                            "resources": [
                                {"title": "C Preprocessor", "url": "https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm"}
                            ]
                        }
                    ]
                },
                {
                    "title": "File Handling Practice",
                    "description": "Practice your skills with C file handling.",
                    "questions": [
                        {
                            "text": "Which of the following is the correct syntax for 'fopen'?",
                            "choices": [
                                {"text": "fopen(\"filename\", \"mode\");", "is_correct": True},
                                {"text": "fopen filename, mode;", "is_correct": False},
                                {"text": "fopen(\"filename\", \"mode\");", "is_correct": False},
                                {"text": "fopen(\"filename\", \"mode\");", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'fopen' is 'fopen(\"filename\", \"mode\");'.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: FILE *fp = fopen(\"test.txt\", \"w\"); fclose(fp);",
                            "choices": [
                                {"text": "Error", "is_correct": False},
                                {"text": "Success", "is_correct": True},
                                {"text": "0", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "The 'fopen' function opens a file and 'fclose' closes it.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'fprintf'?",
                            "choices": [
                                {"text": "fprintf(fp, \"format\", args);", "is_correct": True},
                                {"text": "fprintf fp, \"format\", args;", "is_correct": False},
                                {"text": "fprintf(fp, \"format\", args);", "is_correct": False},
                                {"text": "fprintf(fp, \"format\", args);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'fprintf' is 'fprintf(fp, \"format\", args);'.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "What is the output of: FILE *fp = fopen(\"test.txt\", \"w\"); fprintf(fp, \"Hello\"); fclose(fp);",
                            "choices": [
                                {"text": "Hello", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "1", "is_correct": False}
                            ],
                            "explanation": "The 'fprintf' function writes to the file and 'fclose' closes it.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        },
                        {
                            "text": "Which of the following is the correct syntax for 'fscanf'?",
                            "choices": [
                                {"text": "fscanf(fp, \"format\", &var);", "is_correct": True},
                                {"text": "fscanf fp, \"format\", &var;", "is_correct": False},
                                {"text": "fscanf(fp, \"format\", &var);", "is_correct": False},
                                {"text": "fscanf(fp, \"format\", &var);", "is_correct": False}
                            ],
                            "explanation": "The correct syntax for 'fscanf' is 'fscanf(fp, \"format\", &var);'.",
                            "resources": [
                                {"title": "C File Operations", "url": "https://www.tutorialspoint.com/cprogramming/c_file_handling.htm"}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
} 