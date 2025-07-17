subject_data = {
    "name": "JavaScript",
    "description": "Learn JavaScript concepts and modern ES6+ features",
    "icon": "⚡",
    "color": "bg-yellow-500",
    "levels": [
        {
            "name": "JavaScript Basics",
            "description": "Variables, types, and operators",
            "quizzes": [
                {
                    "title": "JavaScript Basics Quiz",
                    "description": "Test your understanding of JavaScript variables, types, and operators.",
                    "questions": [
                        {
                            "text": "Which of the following is NOT a valid way to declare a variable in JavaScript?",
                            "choices": [
                                {"text": "var", "is_correct": False},
                                {"text": "let", "is_correct": False},
                                {"text": "const", "is_correct": False},
                                {"text": "int", "is_correct": True}
                            ],
                            "explanation": "'int' is not a keyword in JavaScript for variable declaration.",
                            "resources": [
                                {"title": "MDN var", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var"}
                            ]
                        },
                        {
                            "text": "What is the output of: console.log(typeof null);",
                            "choices": [
                                {"text": "'object'", "is_correct": True},
                                {"text": "'null'", "is_correct": False},
                                {"text": "'undefined'", "is_correct": False},
                                {"text": "'number'", "is_correct": False}
                            ],
                            "explanation": "In JavaScript, typeof null returns 'object' due to legacy reasons.",
                            "resources": [
                                {"title": "MDN typeof", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof"}
                            ]
                        },
                        {
                            "text": "Which operator is used for strict equality comparison in JavaScript?",
                            "choices": [
                                {"text": "==", "is_correct": False},
                                {"text": "===", "is_correct": True},
                                {"text": "=", "is_correct": False},
                                {"text": "!=", "is_correct": False}
                            ],
                            "explanation": "The === operator checks both value and type equality.",
                            "resources": [
                                {"title": "MDN Equality", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness"}
                            ]
                        },
                        {
                            "text": "What is the result of: 5 + '5' in JavaScript?",
                            "choices": [
                                {"text": "10", "is_correct": False},
                                {"text": "55", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "JavaScript converts the number to string and concatenates them.",
                            "resources": [
                                {"title": "MDN Type Coercion", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition"}
                            ]
                        },
                        {
                            "text": "Which of these is a falsy value in JavaScript?",
                            "choices": [
                                {"text": "'hello'", "is_correct": False},
                                {"text": "1", "is_correct": False},
                                {"text": "0", "is_correct": True},
                                {"text": "true", "is_correct": False}
                            ],
                            "explanation": "0 is one of the falsy values in JavaScript.",
                            "resources": [
                                {"title": "MDN Falsy", "url": "https://developer.mozilla.org/en-US/docs/Glossary/Falsy"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Variables and Data Types Mastery",
                    "description": "Assess your knowledge of JavaScript variable declarations, scope, and data types.",
                    "questions": [
                        {
                            "text": "Which of the following is a primitive data type in JavaScript?",
                            "choices": [
                                {"text": "Object", "is_correct": False},
                                {"text": "Array", "is_correct": False},
                                {"text": "String", "is_correct": True},
                                {"text": "Function", "is_correct": False}
                            ],
                            "explanation": "String is a primitive data type in JavaScript.",
                            "resources": [
                                {"title": "MDN Data Types", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures"}
                            ]
                        },
                        {
                            "text": "What is the result of typeof undefined?",
                            "choices": [
                                {"text": "'object'", "is_correct": False},
                                {"text": "'undefined'", "is_correct": True},
                                {"text": "'null'", "is_correct": False},
                                {"text": "'number'", "is_correct": False}
                            ],
                            "explanation": "typeof undefined returns 'undefined'.",
                            "resources": [
                                {"title": "MDN typeof", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof"}
                            ]
                        },
                        {
                            "text": "Which keyword is used to declare a block-scoped variable?",
                            "choices": [
                                {"text": "var", "is_correct": False},
                                {"text": "let", "is_correct": True},
                                {"text": "const", "is_correct": False},
                                {"text": "static", "is_correct": False}
                            ],
                            "explanation": "'let' declares a block-scoped variable.",
                            "resources": [
                                {"title": "MDN let", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let"}
                            ]
                        },
                        {
                            "text": "What will be logged by: let x; console.log(x); ?",
                            "choices": [
                                {"text": "null", "is_correct": False},
                                {"text": "undefined", "is_correct": True},
                                {"text": "0", "is_correct": False},
                                {"text": "Error", "is_correct": False}
                            ],
                            "explanation": "A declared but uninitialized variable is undefined.",
                            "resources": [
                                {"title": "MDN Variables", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Declarations"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a valid JavaScript variable name?",
                            "choices": [
                                {"text": "_myVar", "is_correct": False},
                                {"text": "$value", "is_correct": False},
                                {"text": "2ndValue", "is_correct": True},
                                {"text": "myVar2", "is_correct": False}
                            ],
                            "explanation": "Variable names cannot start with a number.",
                            "resources": [
                                {"title": "MDN Variable Names", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Variable_names"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Operators and Expressions Challenge",
                    "description": "Test your understanding of JavaScript operators and how expressions are evaluated.",
                    "questions": [
                        {
                            "text": "What is the result of: '10' - 2 in JavaScript?",
                            "choices": [
                                {"text": "8", "is_correct": True},
                                {"text": "'8'", "is_correct": False},
                                {"text": "'102'", "is_correct": False},
                                {"text": "NaN", "is_correct": False}
                            ],
                            "explanation": "The minus operator converts strings to numbers if possible.",
                            "resources": [
                                {"title": "MDN Operators", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators"}
                            ]
                        },
                        {
                            "text": "Which operator is used to assign a value to a variable?",
                            "choices": [
                                {"text": "=", "is_correct": True},
                                {"text": "==", "is_correct": False},
                                {"text": "===", "is_correct": False},
                                {"text": "+=", "is_correct": False}
                            ],
                            "explanation": "= is the assignment operator.",
                            "resources": [
                                {"title": "MDN Assignment", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment_Operators"}
                            ]
                        },
                        {
                            "text": "What is the result of: true + false?",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "truefalse", "is_correct": False},
                                {"text": "NaN", "is_correct": False},
                                {"text": "0", "is_correct": False}
                            ],
                            "explanation": "true is 1, false is 0, so 1 + 0 = 1.",
                            "resources": [
                                {"title": "MDN Type Conversion", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#Type_Conversion"}
                            ]
                        },
                        {
                            "text": "Which operator returns true if the two compared values are not equal in value or type?",
                            "choices": [
                                {"text": "!==", "is_correct": True},
                                {"text": "!=", "is_correct": False},
                                {"text": "==", "is_correct": False},
                                {"text": "=", "is_correct": False}
                            ],
                            "explanation": "!== checks both value and type.",
                            "resources": [
                                {"title": "MDN Strict Inequality", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality"}
                            ]
                        },
                        {
                            "text": "What is the output of: typeof NaN?",
                            "choices": [
                                {"text": "'number'", "is_correct": True},
                                {"text": "'NaN'", "is_correct": False},
                                {"text": "'undefined'", "is_correct": False},
                                {"text": "'object'", "is_correct": False}
                            ],
                            "explanation": "typeof NaN returns 'number'.",
                            "resources": [
                                {"title": "MDN NaN", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Control Flow",
            "description": "If, else, switch, and loops",
            "quizzes": [
                {
                    "title": "Control Flow Quiz",
                    "description": "Test your understanding of control flow in JavaScript.",
                    "questions": [
                        {
                            "text": "Which statement is used to skip the current iteration of a loop in JavaScript?",
                            "choices": [
                                {"text": "break", "is_correct": False},
                                {"text": "continue", "is_correct": True},
                                {"text": "skip", "is_correct": False},
                                {"text": "exit", "is_correct": False}
                            ],
                            "explanation": "'continue' skips the current iteration of a loop.",
                            "resources": [
                                {"title": "MDN continue", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue"}
                            ]
                        },
                        {
                            "text": "Which loop will always execute at least once?",
                            "choices": [
                                {"text": "for", "is_correct": False},
                                {"text": "while", "is_correct": False},
                                {"text": "do...while", "is_correct": True},
                                {"text": "foreach", "is_correct": False}
                            ],
                            "explanation": "'do...while' executes the block at least once before checking the condition.",
                            "resources": [
                                {"title": "MDN do...while", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while"}
                            ]
                        },
                        {
                            "text": "What is the output of: for(let i = 0; i < 3; i++) { console.log(i); }",
                            "choices": [
                                {"text": "0,1,2", "is_correct": True},
                                {"text": "1,2,3", "is_correct": False},
                                {"text": "0,1,2,3", "is_correct": False},
                                {"text": "1,2", "is_correct": False}
                            ],
                            "explanation": "The loop runs from 0 to 2 (less than 3).",
                            "resources": [
                                {"title": "MDN for", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for"}
                            ]
                        },
                        {
                            "text": "Which statement is used to exit a switch case in JavaScript?",
                            "choices": [
                                {"text": "break", "is_correct": True},
                                {"text": "continue", "is_correct": False},
                                {"text": "return", "is_correct": False},
                                {"text": "exit", "is_correct": False}
                            ],
                            "explanation": "break is used to exit a switch case.",
                            "resources": [
                                {"title": "MDN switch", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch"}
                            ]
                        },
                        {
                            "text": "What is the result of: if (0) { console.log('true'); } else { console.log('false'); }",
                            "choices": [
                                {"text": "true", "is_correct": False},
                                {"text": "false", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "0 is falsy, so the else block executes.",
                            "resources": [
                                {"title": "MDN if...else", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Looping and Branching Scenarios",
                    "description": "Apply your knowledge of JavaScript loops and branching statements to real-world scenarios.",
                    "questions": [
                        {
                            "text": "Which loop is best suited for iterating over an array when you need the index?",
                            "choices": [
                                {"text": "for", "is_correct": True},
                                {"text": "for...of", "is_correct": False},
                                {"text": "for...in", "is_correct": False},
                                {"text": "while", "is_correct": False}
                            ],
                            "explanation": "The classic for loop gives you access to the index.",
                            "resources": [
                                {"title": "MDN for loop", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for"}
                            ]
                        },
                        {
                            "text": "What is the output of: let sum = 0; for(let i = 1; i <= 3; i++) { sum += i; } console.log(sum);",
                            "choices": [
                                {"text": "6", "is_correct": True},
                                {"text": "3", "is_correct": False},
                                {"text": "7", "is_correct": False},
                                {"text": "0", "is_correct": False}
                            ],
                            "explanation": "1+2+3=6.",
                            "resources": [
                                {"title": "MDN for loop", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for"}
                            ]
                        },
                        {
                            "text": "Which statement immediately exits a loop, regardless of the condition?",
                            "choices": [
                                {"text": "break", "is_correct": True},
                                {"text": "continue", "is_correct": False},
                                {"text": "return", "is_correct": False},
                                {"text": "exit", "is_correct": False}
                            ],
                            "explanation": "break exits the loop immediately.",
                            "resources": [
                                {"title": "MDN break", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break"}
                            ]
                        },
                        {
                            "text": "What is the output of: let x = 0; while(x < 2) { x++; } console.log(x);",
                            "choices": [
                                {"text": "2", "is_correct": True},
                                {"text": "1", "is_correct": False},
                                {"text": "0", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "x is incremented twice, ending at 2.",
                            "resources": [
                                {"title": "MDN while loop", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while"}
                            ]
                        },
                        {
                            "text": "Which control flow structure is best for handling multiple discrete values of a variable?",
                            "choices": [
                                {"text": "switch", "is_correct": True},
                                {"text": "if...else", "is_correct": False},
                                {"text": "for", "is_correct": False},
                                {"text": "while", "is_correct": False}
                            ],
                            "explanation": "switch is ideal for multiple discrete cases.",
                            "resources": [
                                {"title": "MDN switch", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Real-World Control Flow Applications",
                    "description": "Apply your knowledge of JavaScript control flow to practical coding scenarios.",
                    "questions": [
                        {
                            "text": "Which control flow structure is best for validating user input against multiple possible values?",
                            "choices": [
                                {"text": "switch", "is_correct": True},
                                {"text": "for", "is_correct": False},
                                {"text": "while", "is_correct": False},
                                {"text": "do...while", "is_correct": False}
                            ],
                            "explanation": "The switch statement is ideal for handling multiple discrete values.",
                            "resources": [
                                {"title": "MDN switch", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch"}
                            ]
                        },
                        {
                            "text": "What is the output of: let x = 5; if (x > 3) { x += 2; } else { x -= 2; } console.log(x);",
                            "choices": [
                                {"text": "7", "is_correct": True},
                                {"text": "3", "is_correct": False},
                                {"text": "5", "is_correct": False},
                                {"text": "2", "is_correct": False}
                            ],
                            "explanation": "Since x > 3, x is incremented by 2, resulting in 7.",
                            "resources": [
                                {"title": "MDN if...else", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else"}
                            ]
                        },
                        {
                            "text": "Which loop is best for iterating until a condition is no longer true, but the number of iterations is unknown?",
                            "choices": [
                                {"text": "while", "is_correct": True},
                                {"text": "for", "is_correct": False},
                                {"text": "do...while", "is_correct": False},
                                {"text": "switch", "is_correct": False}
                            ],
                            "explanation": "A while loop is ideal when the number of iterations is not predetermined.",
                            "resources": [
                                {"title": "MDN while loop", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while"}
                            ]
                        },
                        {
                            "text": "What is the result of: let arr = [1,2,3]; for (let i of arr) { if (i === 2) break; console.log(i); }",
                            "choices": [
                                {"text": "1", "is_correct": True},
                                {"text": "1 2", "is_correct": False},
                                {"text": "1 2 3", "is_correct": False},
                                {"text": "2", "is_correct": False}
                            ],
                            "explanation": "The loop logs 1, then breaks when i === 2.",
                            "resources": [
                                {"title": "MDN break", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break"}
                            ]
                        },
                        {
                            "text": "Which statement is used to skip the rest of the code inside a loop for the current iteration?",
                            "choices": [
                                {"text": "continue", "is_correct": True},
                                {"text": "break", "is_correct": False},
                                {"text": "return", "is_correct": False},
                                {"text": "exit", "is_correct": False}
                            ],
                            "explanation": "The continue statement skips to the next iteration of the loop.",
                            "resources": [
                                {"title": "MDN continue", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Functions & ES6",
            "description": "Functions, arrow functions, and ES6 features",
            "quizzes": [
                {
                    "title": "Functions & ES6 Quiz",
                    "description": "Test your understanding of functions and ES6 features in JavaScript.",
                    "questions": [
                        {
                            "text": "How do you define an arrow function in JavaScript?",
                            "choices": [
                                {"text": "function() => {}", "is_correct": False},
                                {"text": "() => {}", "is_correct": True},
                                {"text": "=> function() {}", "is_correct": False},
                                {"text": "function => {}", "is_correct": False}
                            ],
                            "explanation": "Arrow functions use the syntax: () => {}",
                            "resources": [
                                {"title": "MDN Arrow Functions", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"}
                            ]
                        },
                        {
                            "text": "Which ES6 feature allows you to declare a block-scoped variable?",
                            "choices": [
                                {"text": "var", "is_correct": False},
                                {"text": "let", "is_correct": False},
                                {"text": "const", "is_correct": False},
                                {"text": "both let and const", "is_correct": True}
                            ],
                            "explanation": "'let' and 'const' are block-scoped in ES6.",
                            "resources": [
                                {"title": "MDN let", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let"}
                            ]
                        },
                        {
                            "text": "What is the output of: const add = (a, b) => a + b; console.log(add(2, 3));",
                            "choices": [
                                {"text": "5", "is_correct": True},
                                {"text": "23", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "Arrow functions can have implicit return for single expressions.",
                            "resources": [
                                {"title": "MDN Arrow Functions", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"}
                            ]
                        },
                        {
                            "text": "Which ES6 feature allows you to extract values from objects?",
                            "choices": [
                                {"text": "Destructuring", "is_correct": True},
                                {"text": "Spread", "is_correct": False},
                                {"text": "Rest", "is_correct": False},
                                {"text": "Template literals", "is_correct": False}
                            ],
                            "explanation": "Destructuring allows you to extract values from objects and arrays.",
                            "resources": [
                                {"title": "MDN Destructuring", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment"}
                            ]
                        },
                        {
                            "text": "What is the result of: const name = 'John'; console.log(`Hello ${name}!`);",
                            "choices": [
                                {"text": "Hello John!", "is_correct": True},
                                {"text": "Hello ${name}!", "is_correct": False},
                                {"text": "Error", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "Template literals use backticks and ${} for variable interpolation.",
                            "resources": [
                                {"title": "MDN Template Literals", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals"}
                            ]
                        }
                    ]
                },
                {
                    "title": "ES6 Features in Practice",
                    "description": "Demonstrate your understanding of ES6 features and modern JavaScript function patterns.",
                    "questions": [
                        {
                            "text": "Which ES6 feature allows you to combine multiple arrays into one?",
                            "choices": [
                                {"text": "Spread operator", "is_correct": True},
                                {"text": "Rest operator", "is_correct": False},
                                {"text": "Destructuring", "is_correct": False},
                                {"text": "Template literals", "is_correct": False}
                            ],
                            "explanation": "The spread operator (...) combines arrays.",
                            "resources": [
                                {"title": "MDN Spread syntax", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax"}
                            ]
                        },
                        {
                            "text": "What is the output of: const nums = [1,2,3]; const [a,,c] = nums; console.log(a, c);",
                            "choices": [
                                {"text": "1 3", "is_correct": True},
                                {"text": "1 2", "is_correct": False},
                                {"text": "2 3", "is_correct": False},
                                {"text": "undefined undefined", "is_correct": False}
                            ],
                            "explanation": "Destructuring skips the second element.",
                            "resources": [
                                {"title": "MDN Destructuring", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment"}
                            ]
                        },
                        {
                            "text": "Which function syntax preserves the value of 'this' from the enclosing context?",
                            "choices": [
                                {"text": "Arrow function", "is_correct": True},
                                {"text": "Function declaration", "is_correct": False},
                                {"text": "Function expression", "is_correct": False},
                                {"text": "IIFE", "is_correct": False}
                            ],
                            "explanation": "Arrow functions do not have their own 'this'.",
                            "resources": [
                                {"title": "MDN Arrow Functions", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"}
                            ]
                        },
                        {
                            "text": "Which ES6 feature allows you to assign default values to function parameters?",
                            "choices": [
                                {"text": "Default parameters", "is_correct": True},
                                {"text": "Rest parameters", "is_correct": False},
                                {"text": "Spread operator", "is_correct": False},
                                {"text": "Destructuring", "is_correct": False}
                            ],
                            "explanation": "Default parameters let you set default values.",
                            "resources": [
                                {"title": "MDN Default parameters", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters"}
                            ]
                        },
                        {
                            "text": "What is the output of: const f = (...args) => args.length; console.log(f(1,2,3));",
                            "choices": [
                                {"text": "3", "is_correct": True},
                                {"text": "1", "is_correct": False},
                                {"text": "undefined", "is_correct": False},
                                {"text": "0", "is_correct": False}
                            ],
                            "explanation": "The rest parameter collects all arguments into an array.",
                            "resources": [
                                {"title": "MDN Rest parameters", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "DOM & Events",
            "description": "Document Object Model and event handling",
            "quizzes": [
                {
                    "title": "DOM & Events Quiz",
                    "description": "Test your understanding of the DOM and event handling in JavaScript.",
                    "questions": [
                        {
                            "text": "Which method is used to select an element by its ID in JavaScript?",
                            "choices": [
                                {"text": "getElementById", "is_correct": True},
                                {"text": "querySelector", "is_correct": False},
                                {"text": "getElementsByClassName", "is_correct": False},
                                {"text": "getElementByTag", "is_correct": False}
                            ],
                            "explanation": "getElementById is used to select an element by its ID.",
                            "resources": [
                                {"title": "MDN getElementById", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById"}
                            ]
                        },
                        {
                            "text": "Which event is triggered when a user clicks on an HTML element?",
                            "choices": [
                                {"text": "onchange", "is_correct": False},
                                {"text": "onmouseover", "is_correct": False},
                                {"text": "onclick", "is_correct": True},
                                {"text": "onload", "is_correct": False}
                            ],
                            "explanation": "The 'onclick' event is triggered when an element is clicked.",
                            "resources": [
                                {"title": "MDN onclick", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event"}
                            ]
                        },
                        {
                            "text": "How do you add an event listener in JavaScript?",
                            "choices": [
                                {"text": "addEventListener", "is_correct": True},
                                {"text": "onEvent", "is_correct": False},
                                {"text": "attachEvent", "is_correct": False},
                                {"text": "bindEvent", "is_correct": False}
                            ],
                            "explanation": "addEventListener is the modern way to add event handlers.",
                            "resources": [
                                {"title": "MDN addEventListener", "url": "https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener"}
                            ]
                        },
                        {
                            "text": "Which method is used to create a new HTML element?",
                            "choices": [
                                {"text": "createElement", "is_correct": True},
                                {"text": "newElement", "is_correct": False},
                                {"text": "makeElement", "is_correct": False},
                                {"text": "buildElement", "is_correct": False}
                            ],
                            "explanation": "createElement creates a new HTML element.",
                            "resources": [
                                {"title": "MDN createElement", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement"}
                            ]
                        },
                        {
                            "text": "How do you change the text content of an element?",
                            "choices": [
                                {"text": "textContent", "is_correct": True},
                                {"text": "innerHTML", "is_correct": False},
                                {"text": "value", "is_correct": False},
                                {"text": "content", "is_correct": False}
                            ],
                            "explanation": "textContent sets or returns the text content of an element.",
                            "resources": [
                                {"title": "MDN textContent", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Event Handling in Depth",
                    "description": "Assess your knowledge of advanced event handling and DOM manipulation techniques.",
                    "questions": [
                        {
                            "text": "Which event is triggered when a form is submitted?",
                            "choices": [
                                {"text": "submit", "is_correct": True},
                                {"text": "change", "is_correct": False},
                                {"text": "click", "is_correct": False},
                                {"text": "input", "is_correct": False}
                            ],
                            "explanation": "The 'submit' event is fired when a form is submitted.",
                            "resources": [
                                {"title": "MDN submit event", "url": "https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event"}
                            ]
                        },
                        {
                            "text": "How do you prevent the default action of an event?",
                            "choices": [
                                {"text": "event.preventDefault()", "is_correct": True},
                                {"text": "event.stopPropagation()", "is_correct": False},
                                {"text": "return false", "is_correct": False},
                                {"text": "event.cancel()", "is_correct": False}
                            ],
                            "explanation": "event.preventDefault() prevents the default browser action.",
                            "resources": [
                                {"title": "MDN preventDefault", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault"}
                            ]
                        },
                        {
                            "text": "Which method is used to stop an event from bubbling up the DOM?",
                            "choices": [
                                {"text": "event.stopPropagation()", "is_correct": True},
                                {"text": "event.preventDefault()", "is_correct": False},
                                {"text": "event.stopImmediatePropagation()", "is_correct": False},
                                {"text": "event.cancelBubble()", "is_correct": False}
                            ],
                            "explanation": "event.stopPropagation() stops the event from bubbling.",
                            "resources": [
                                {"title": "MDN stopPropagation", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation"}
                            ]
                        },
                        {
                            "text": "What is the output of: document.getElementById('demo').textContent = 'Hello'; ?",
                            "choices": [
                                {"text": "The text content of the element with id 'demo' is set to 'Hello'", "is_correct": True},
                                {"text": "An error is thrown", "is_correct": False},
                                {"text": "Nothing happens", "is_correct": False},
                                {"text": "The HTML is changed to 'Hello'", "is_correct": False}
                            ],
                            "explanation": "textContent sets the text of the element.",
                            "resources": [
                                {"title": "MDN textContent", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent"}
                            ]
                        },
                        {
                            "text": "Which event is triggered when an input field loses focus?",
                            "choices": [
                                {"text": "blur", "is_correct": True},
                                {"text": "focus", "is_correct": False},
                                {"text": "change", "is_correct": False},
                                {"text": "input", "is_correct": False}
                            ],
                            "explanation": "The 'blur' event is fired when an element loses focus.",
                            "resources": [
                                {"title": "MDN blur event", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Arrays & Objects",
            "description": "Working with arrays, objects, and methods",
            "quizzes": [
                {
                    "title": "Arrays & Objects Quiz",
                    "description": "Test your understanding of arrays and objects in JavaScript.",
                    "questions": [
                        {
                            "text": "Which method adds an element to the end of an array?",
                            "choices": [
                                {"text": "push", "is_correct": True},
                                {"text": "pop", "is_correct": False},
                                {"text": "shift", "is_correct": False},
                                {"text": "unshift", "is_correct": False}
                            ],
                            "explanation": "push adds one or more elements to the end of an array.",
                            "resources": [
                                {"title": "MDN push", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push"}
                            ]
                        },
                        {
                            "text": "How do you access an object property in JavaScript?",
                            "choices": [
                                {"text": "object.property", "is_correct": False},
                                {"text": "object['property']", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "object->property", "is_correct": False}
                            ],
                            "explanation": "You can use dot notation or bracket notation to access object properties.",
                            "resources": [
                                {"title": "MDN Objects", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"}
                            ]
                        },
                        {
                            "text": "Which method creates a new array with the results of calling a function for every array element?",
                            "choices": [
                                {"text": "map", "is_correct": True},
                                {"text": "filter", "is_correct": False},
                                {"text": "reduce", "is_correct": False},
                                {"text": "forEach", "is_correct": False}
                            ],
                            "explanation": "map creates a new array with the results of calling a function for every array element.",
                            "resources": [
                                {"title": "MDN map", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map"}
                            ]
                        },
                        {
                            "text": "What is the output of: const arr = [1, 2, 3]; console.log(arr.length);",
                            "choices": [
                                {"text": "3", "is_correct": True},
                                {"text": "2", "is_correct": False},
                                {"text": "4", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "The length property returns the number of elements in an array.",
                            "resources": [
                                {"title": "MDN Array length", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length"}
                            ]
                        },
                        {
                            "text": "Which method removes the last element from an array?",
                            "choices": [
                                {"text": "pop", "is_correct": True},
                                {"text": "push", "is_correct": False},
                                {"text": "shift", "is_correct": False},
                                {"text": "unshift", "is_correct": False}
                            ],
                            "explanation": "pop removes the last element from an array and returns it.",
                            "resources": [
                                {"title": "MDN pop", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Array Methods in Action",
                    "description": "Test your knowledge of advanced array methods and object manipulation.",
                    "questions": [
                        {
                            "text": "Which method returns the first element that satisfies a provided testing function?",
                            "choices": [
                                {"text": "find", "is_correct": True},
                                {"text": "filter", "is_correct": False},
                                {"text": "map", "is_correct": False},
                                {"text": "reduce", "is_correct": False}
                            ],
                            "explanation": "find returns the first matching element.",
                            "resources": [
                                {"title": "MDN find", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find"}
                            ]
                        },
                        {
                            "text": "What is the output of: [1,2,3].filter(x => x > 1); ?",
                            "choices": [
                                {"text": "[2,3]", "is_correct": True},
                                {"text": "[1,2,3]", "is_correct": False},
                                {"text": "[1]", "is_correct": False},
                                {"text": "[3]", "is_correct": False}
                            ],
                            "explanation": "filter returns elements greater than 1.",
                            "resources": [
                                {"title": "MDN filter", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter"}
                            ]
                        },
                        {
                            "text": "Which method merges two or more arrays?",
                            "choices": [
                                {"text": "concat", "is_correct": True},
                                {"text": "join", "is_correct": False},
                                {"text": "push", "is_correct": False},
                                {"text": "splice", "is_correct": False}
                            ],
                            "explanation": "concat merges arrays.",
                            "resources": [
                                {"title": "MDN concat", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat"}
                            ]
                        },
                        {
                            "text": "How do you check if a property exists in an object?",
                            "choices": [
                                {"text": "'property' in object", "is_correct": True},
                                {"text": "object.hasProperty('property')", "is_correct": False},
                                {"text": "object.exists('property')", "is_correct": False},
                                {"text": "object.check('property')", "is_correct": False}
                            ],
                            "explanation": "'property' in object checks for existence.",
                            "resources": [
                                {"title": "MDN in operator", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in"}
                            ]
                        },
                        {
                            "text": "Which method returns a shallow copy of a portion of an array?",
                            "choices": [
                                {"text": "slice", "is_correct": True},
                                {"text": "splice", "is_correct": False},
                                {"text": "copy", "is_correct": False},
                                {"text": "map", "is_correct": False}
                            ],
                            "explanation": "slice returns a shallow copy of a portion of an array.",
                            "resources": [
                                {"title": "MDN slice", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Advanced JavaScript",
            "description": "Closures, promises, and modern patterns",
            "quizzes": [
                {
                    "title": "Advanced JavaScript Quiz",
                    "description": "Test your understanding of advanced JavaScript concepts.",
                    "questions": [
                        {
                            "text": "What is a closure in JavaScript?",
                            "choices": [
                                {"text": "A function that has access to variables in its outer scope", "is_correct": True},
                                {"text": "A way to close a function", "is_correct": False},
                                {"text": "A type of loop", "is_correct": False},
                                {"text": "A method to end execution", "is_correct": False}
                            ],
                            "explanation": "A closure is a function that has access to variables in its outer scope.",
                            "resources": [
                                {"title": "MDN Closures", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures"}
                            ]
                        },
                        {
                            "text": "Which method is used to handle asynchronous operations in modern JavaScript?",
                            "choices": [
                                {"text": "async/await", "is_correct": False},
                                {"text": "callbacks", "is_correct": False},
                                {"text": "promises", "is_correct": False},
                                {"text": "All of the above", "is_correct": True}
                            ],
                            "explanation": "JavaScript supports callbacks, promises, and async/await for asynchronous operations.",
                            "resources": [
                                {"title": "MDN async/await", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function"}
                            ]
                        },
                        {
                            "text": "What is the output of: Promise.resolve(5).then(x => x * 2).then(console.log);",
                            "choices": [
                                {"text": "5", "is_correct": False},
                                {"text": "10", "is_correct": True},
                                {"text": "Error", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "The promise resolves to 5, then multiplies by 2, resulting in 10.",
                            "resources": [
                                {"title": "MDN Promise", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise"}
                            ]
                        },
                        {
                            "text": "Which keyword is used to declare an async function?",
                            "choices": [
                                {"text": "async", "is_correct": True},
                                {"text": "await", "is_correct": False},
                                {"text": "function", "is_correct": False},
                                {"text": "async function", "is_correct": False}
                            ],
                            "explanation": "The async keyword is used to declare an async function.",
                            "resources": [
                                {"title": "MDN async function", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function"}
                            ]
                        },
                        {
                            "text": "What is the purpose of the 'this' keyword in JavaScript?",
                            "choices": [
                                {"text": "Refers to the current object", "is_correct": True},
                                {"text": "Creates a new object", "is_correct": False},
                                {"text": "Ends a function", "is_correct": False},
                                {"text": "Starts a loop", "is_correct": False}
                            ],
                            "explanation": "The 'this' keyword refers to the current object context.",
                            "resources": [
                                {"title": "MDN this", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Modern Patterns and Best Practices",
                    "description": "Demonstrate your understanding of modern JavaScript patterns and best practices.",
                    "questions": [
                        {
                            "text": "Which pattern is used to create a single instance of an object?",
                            "choices": [
                                {"text": "Singleton", "is_correct": True},
                                {"text": "Factory", "is_correct": False},
                                {"text": "Observer", "is_correct": False},
                                {"text": "Module", "is_correct": False}
                            ],
                            "explanation": "The Singleton pattern restricts instantiation to one object.",
                            "resources": [
                                {"title": "MDN Singleton", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"}
                            ]
                        },
                        {
                            "text": "Which method is used to copy all enumerable properties from one or more source objects to a target object?",
                            "choices": [
                                {"text": "Object.assign", "is_correct": True},
                                {"text": "Object.copy", "is_correct": False},
                                {"text": "Object.merge", "is_correct": False},
                                {"text": "Object.clone", "is_correct": False}
                            ],
                            "explanation": "Object.assign copies properties to a target object.",
                            "resources": [
                                {"title": "MDN Object.assign", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign"}
                            ]
                        },
                        {
                            "text": "What is the output of: const obj = {a:1}; const copy = {...obj}; console.log(copy);",
                            "choices": [
                                {"text": "{a:1}", "is_correct": True},
                                {"text": "[1]", "is_correct": False},
                                {"text": "1", "is_correct": False},
                                {"text": "undefined", "is_correct": False}
                            ],
                            "explanation": "The spread operator creates a shallow copy of the object.",
                            "resources": [
                                {"title": "MDN Spread syntax", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax"}
                            ]
                        },
                        {
                            "text": "Which pattern is used to observe changes to an object and react to them?",
                            "choices": [
                                {"text": "Observer", "is_correct": True},
                                {"text": "Factory", "is_correct": False},
                                {"text": "Singleton", "is_correct": False},
                                {"text": "Module", "is_correct": False}
                            ],
                            "explanation": "The Observer pattern allows objects to subscribe to events.",
                            "resources": [
                                {"title": "MDN Observer", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Details_of_the_Object_Model"}
                            ]
                        },
                        {
                            "text": "Which ES6 feature allows you to define constants?",
                            "choices": [
                                {"text": "const", "is_correct": True},
                                {"text": "let", "is_correct": False},
                                {"text": "var", "is_correct": False},
                                {"text": "static", "is_correct": False}
                            ],
                            "explanation": "const declares a block-scoped constant.",
                            "resources": [
                                {"title": "MDN const", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const"}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
} 