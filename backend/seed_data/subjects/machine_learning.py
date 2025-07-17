subject_data = {
    "name": "Machine Learning",
    "description": "Understand ML algorithms and theoretical foundations",
    "icon": "🤖",
    "color": "bg-purple-500",
    "levels": [
        {
            "name": "ML Fundamentals",
            "description": "Introduction to machine learning concepts and terminology",
            "quizzes": [
                {
                    "title": "ML Fundamentals Quiz",
                    "description": "Test your understanding of basic ML concepts",
                    "questions": [
                        {
                            "text": "What is the main goal of supervised learning?",
                            "choices": [
                                {"text": "Find hidden patterns", "is_correct": False},
                                {"text": "Learn from labeled data", "is_correct": True},
                                {"text": "Reduce dimensionality", "is_correct": False},
                                {"text": "Cluster similar data", "is_correct": False}
                            ],
                            "explanation": "Supervised learning uses labeled training data to learn a mapping from inputs to outputs.",
                            "resources": [
                                {"title": "Supervised Learning Overview", "url": "https://scikit-learn.org/stable/supervised_learning.html"}
                            ]
                        },
                        {
                            "text": "What is overfitting in machine learning?",
                            "choices": [
                                {"text": "Model is too simple", "is_correct": False},
                                {"text": "Model performs well on training but poorly on test data", "is_correct": True},
                                {"text": "Model has too few parameters", "is_correct": False},
                                {"text": "Model trains too slowly", "is_correct": False}
                            ],
                            "explanation": "Overfitting occurs when a model learns the training data too well, including noise, leading to poor generalization.",
                            "resources": [
                                {"title": "Overfitting and Underfitting", "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a type of machine learning?",
                            "choices": [
                                {"text": "Supervised Learning", "is_correct": False},
                                {"text": "Unsupervised Learning", "is_correct": False},
                                {"text": "Reinforcement Learning", "is_correct": False},
                                {"text": "Descriptive Learning", "is_correct": True}
                            ],
                            "explanation": "Descriptive Learning is not a standard type of machine learning.",
                            "resources": [
                                {"title": "Types of Machine Learning", "url": "https://en.wikipedia.org/wiki/Machine_learning#Types_of_problems_and_tasks"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Types of Machine Learning Quiz",
                    "description": "Assess your understanding of supervised, unsupervised, and reinforcement learning.",
                    "questions": [
                        {
                            "text": "Which type of machine learning uses labeled data?",
                            "choices": [
                                {"text": "Supervised Learning", "is_correct": True},
                                {"text": "Unsupervised Learning", "is_correct": False},
                                {"text": "Reinforcement Learning", "is_correct": False},
                                {"text": "Semi-supervised Learning", "is_correct": False}
                            ],
                            "explanation": "Supervised learning uses labeled data.",
                            "resources": [
                                {"title": "Types of Machine Learning", "url": "https://en.wikipedia.org/wiki/Machine_learning#Types_of_problems_and_tasks"}
                            ]
                        },
                        {
                            "text": "Which of the following is an example of reinforcement learning?",
                            "choices": [
                                {"text": "A robot learning to walk by trial and error", "is_correct": True},
                                {"text": "Clustering customer data", "is_correct": False},
                                {"text": "Predicting house prices", "is_correct": False},
                                {"text": "Image classification", "is_correct": False}
                            ],
                            "explanation": "Reinforcement learning involves learning by interacting with an environment and receiving feedback.",
                            "resources": [
                                {"title": "Reinforcement Learning", "url": "https://en.wikipedia.org/wiki/Reinforcement_learning"}
                            ]
                        },
                        {
                            "text": "What is the main difference between supervised and unsupervised learning?",
                            "choices": [
                                {"text": "Supervised uses labeled data, unsupervised does not", "is_correct": True},
                                {"text": "Unsupervised is always more accurate", "is_correct": False},
                                {"text": "Supervised is faster", "is_correct": False},
                                {"text": "Unsupervised uses reinforcement", "is_correct": False}
                            ],
                            "explanation": "Supervised learning uses labeled data, unsupervised does not.",
                            "resources": [
                                {"title": "Supervised vs Unsupervised", "url": "https://scikit-learn.org/stable/supervised_learning.html"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a common ML task?",
                            "choices": [
                                {"text": "Classification", "is_correct": False},
                                {"text": "Regression", "is_correct": False},
                                {"text": "Clustering", "is_correct": False},
                                {"text": "Transpilation", "is_correct": True}
                            ],
                            "explanation": "Transpilation is not a machine learning task.",
                            "resources": [
                                {"title": "ML Tasks", "url": "https://en.wikipedia.org/wiki/Machine_learning#Types_of_problems_and_tasks"}
                            ]
                        },
                        {
                            "text": "What is the purpose of cross-validation?",
                            "choices": [
                                {"text": "To assess model performance on unseen data", "is_correct": True},
                                {"text": "To increase training data", "is_correct": False},
                                {"text": "To reduce dimensionality", "is_correct": False},
                                {"text": "To cluster data", "is_correct": False}
                            ],
                            "explanation": "Cross-validation helps estimate how well a model will generalize to unseen data.",
                            "resources": [
                                {"title": "Cross-Validation", "url": "https://scikit-learn.org/stable/modules/cross_validation.html"}
                            ]
                        }
                    ]
                },
                {
                    "title": "ML Concepts & Terminology Challenge",
                    "description": "Test your knowledge of key machine learning concepts and terminology.",
                    "questions": [
                        {
                            "text": "What is a feature in machine learning?",
                            "choices": [
                                {"text": "An input variable used for prediction", "is_correct": True},
                                {"text": "The output of a model", "is_correct": False},
                                {"text": "A type of algorithm", "is_correct": False},
                                {"text": "A data label", "is_correct": False}
                            ],
                            "explanation": "A feature is an input variable used by a model to make predictions.",
                            "resources": [
                                {"title": "Features in ML", "url": "https://en.wikipedia.org/wiki/Feature_(machine_learning)"}
                            ]
                        },
                        {
                            "text": "What is the output of a regression model?",
                            "choices": [
                                {"text": "A continuous value", "is_correct": True},
                                {"text": "A category label", "is_correct": False},
                                {"text": "A cluster assignment", "is_correct": False},
                                {"text": "A probability", "is_correct": False}
                            ],
                            "explanation": "Regression models predict continuous values.",
                            "resources": [
                                {"title": "Regression", "url": "https://scikit-learn.org/stable/supervised_learning.html#regression"}
                            ]
                        },
                        {
                            "text": "Which metric is commonly used to evaluate classification models?",
                            "choices": [
                                {"text": "Accuracy", "is_correct": True},
                                {"text": "Mean Squared Error", "is_correct": False},
                                {"text": "R-squared", "is_correct": False},
                                {"text": "Silhouette Score", "is_correct": False}
                            ],
                            "explanation": "Accuracy is a common metric for classification models.",
                            "resources": [
                                {"title": "Classification Metrics", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics"}
                            ]
                        },
                        {
                            "text": "What is the purpose of a loss function?",
                            "choices": [
                                {"text": "To measure how well a model predicts the target", "is_correct": True},
                                {"text": "To increase model complexity", "is_correct": False},
                                {"text": "To reduce training time", "is_correct": False},
                                {"text": "To cluster data", "is_correct": False}
                            ],
                            "explanation": "A loss function measures the difference between predicted and actual values.",
                            "resources": [
                                {"title": "Loss Functions", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#loss-functions"}
                            ]
                        },
                        {
                            "text": "Which of the following is NOT a benefit of using machine learning?",
                            "choices": [
                                {"text": "Automating repetitive tasks", "is_correct": False},
                                {"text": "Making predictions from data", "is_correct": False},
                                {"text": "Replacing all human jobs", "is_correct": True},
                                {"text": "Finding patterns in large datasets", "is_correct": False}
                            ],
                            "explanation": "Machine learning is powerful, but it does not replace all human jobs.",
                            "resources": [
                                {"title": "Benefits of ML", "url": "https://en.wikipedia.org/wiki/Machine_learning#Applications"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Supervised Learning",
            "description": "Learn about classification and regression algorithms",
            "quizzes": [
                {
                    "title": "Supervised Learning Quiz",
                    "description": "Test your understanding of classification and regression algorithms",
                    "questions": [
                        {
                            "text": "What is the main difference between Linear Regression and Logistic Regression?",
                            "choices": [
                                {"text": "Linear Regression is faster", "is_correct": False},
                                {"text": "Linear Regression predicts continuous values, Logistic Regression predicts probabilities", "is_correct": True},
                                {"text": "Logistic Regression is more accurate", "is_correct": False},
                                {"text": "There is no difference", "is_correct": False}
                            ],
                            "explanation": "Linear Regression predicts continuous numerical values, while Logistic Regression predicts probabilities and is used for classification.",
                            "resources": [
                                {"title": "Linear vs Logistic Regression", "url": "https://scikit-learn.org/stable/modules/linear_model.html"}
                            ]
                        },
                        {
                            "text": "What is the purpose of the sigmoid function in logistic regression?",
                            "choices": [
                                {"text": "To make the model faster", "is_correct": False},
                                {"text": "To convert any real number to a probability between 0 and 1", "is_correct": True},
                                {"text": "To reduce overfitting", "is_correct": False},
                                {"text": "To increase accuracy", "is_correct": False}
                            ],
                            "explanation": "The sigmoid function maps any real number to a value between 0 and 1, making it suitable for probability prediction.",
                            "resources": [
                                {"title": "Sigmoid Function", "url": "https://en.wikipedia.org/wiki/Sigmoid_function"}
                            ]
                        },
                        {
                            "text": "What is a decision tree in machine learning?",
                            "choices": [
                                {"text": "A tree-like model for making decisions", "is_correct": False},
                                {"text": "A model that splits data based on feature values", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "A type of neural network", "is_correct": False}
                            ],
                            "explanation": "A decision tree is a tree-like model that makes decisions by splitting data based on feature values at each node.",
                            "resources": [
                                {"title": "Decision Trees", "url": "https://scikit-learn.org/stable/modules/tree.html"}
                            ]
                        },
                        {
                            "text": "What is the purpose of the Support Vector Machine (SVM) algorithm?",
                            "choices": [
                                {"text": "To find the best hyperplane that separates classes", "is_correct": True},
                                {"text": "To reduce dimensionality", "is_correct": False},
                                {"text": "To cluster data", "is_correct": False},
                                {"text": "To make predictions faster", "is_correct": False}
                            ],
                            "explanation": "SVM finds the optimal hyperplane that best separates different classes in the data with maximum margin.",
                            "resources": [
                                {"title": "Support Vector Machines", "url": "https://scikit-learn.org/stable/modules/svm.html"}
                            ]
                        },
                        {
                            "text": "What is the difference between precision and recall?",
                            "choices": [
                                {"text": "Precision measures accuracy, recall measures completeness", "is_correct": False},
                                {"text": "Precision = TP/(TP+FP), Recall = TP/(TP+FN)", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "There is no difference", "is_correct": False}
                            ],
                            "explanation": "Precision measures how many of the predicted positives are actually positive, while recall measures how many of the actual positives were correctly predicted.",
                            "resources": [
                                {"title": "Precision and Recall", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Supervised Learning Quiz 2",
                    "description": "Test your understanding of classification and regression algorithms",
                    "questions": [
                        {
                            "text": "What is the main difference between Linear Regression and Logistic Regression?",
                            "choices": [
                                {"text": "Linear Regression is faster", "is_correct": False},
                                {"text": "Linear Regression predicts continuous values, Logistic Regression predicts probabilities", "is_correct": True},
                                {"text": "Logistic Regression is more accurate", "is_correct": False},
                                {"text": "There is no difference", "is_correct": False}
                            ],
                            "explanation": "Linear Regression predicts continuous numerical values, while Logistic Regression predicts probabilities and is used for classification.",
                            "resources": [
                                {"title": "Linear vs Logistic Regression", "url": "https://scikit-learn.org/stable/modules/linear_model.html"}
                            ]
                        },
                        {
                            "text": "What is the purpose of the sigmoid function in logistic regression?",
                            "choices": [
                                {"text": "To make the model faster", "is_correct": False},
                                {"text": "To convert any real number to a probability between 0 and 1", "is_correct": True},
                                {"text": "To reduce overfitting", "is_correct": False},
                                {"text": "To increase accuracy", "is_correct": False}
                            ],
                            "explanation": "The sigmoid function maps any real number to a value between 0 and 1, making it suitable for probability prediction.",
                            "resources": [
                                {"title": "Sigmoid Function", "url": "https://en.wikipedia.org/wiki/Sigmoid_function"}
                            ]
                        },
                        {
                            "text": "What is a decision tree in machine learning?",
                            "choices": [
                                {"text": "A tree-like model for making decisions", "is_correct": False},
                                {"text": "A model that splits data based on feature values", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "A type of neural network", "is_correct": False}
                            ],
                            "explanation": "A decision tree is a tree-like model that makes decisions by splitting data based on feature values at each node.",
                            "resources": [
                                {"title": "Decision Trees", "url": "https://scikit-learn.org/stable/modules/tree.html"}
                            ]
                        },
                        {
                            "text": "What is the purpose of the Support Vector Machine (SVM) algorithm?",
                            "choices": [
                                {"text": "To find the best hyperplane that separates classes", "is_correct": True},
                                {"text": "To reduce dimensionality", "is_correct": False},
                                {"text": "To cluster data", "is_correct": False},
                                {"text": "To make predictions faster", "is_correct": False}
                            ],
                            "explanation": "SVM finds the optimal hyperplane that best separates different classes in the data with maximum margin.",
                            "resources": [
                                {"title": "Support Vector Machines", "url": "https://scikit-learn.org/stable/modules/svm.html"}
                            ]
                        },
                        {
                            "text": "What is the difference between precision and recall?",
                            "choices": [
                                {"text": "Precision measures accuracy, recall measures completeness", "is_correct": False},
                                {"text": "Precision = TP/(TP+FP), Recall = TP/(TP+FN)", "is_correct": False},
                                {"text": "Both A and B", "is_correct": True},
                                {"text": "There is no difference", "is_correct": False}
                            ],
                            "explanation": "Precision measures how many of the predicted positives are actually positive, while recall measures how many of the actual positives were correctly predicted.",
                            "resources": [
                                {"title": "Precision and Recall", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Unsupervised Learning",
            "description": "Explore clustering and dimensionality reduction",
            "quizzes": [
                {
                    "title": "Unsupervised Learning Quiz",
                    "description": "Test your understanding of clustering and dimensionality reduction",
                    "questions": [
                        {
                            "text": "What is the main goal of K-Means clustering?",
                            "choices": [
                                {"text": "To classify data into predefined categories", "is_correct": False},
                                {"text": "To group similar data points together", "is_correct": True},
                                {"text": "To predict continuous values", "is_correct": False},
                                {"text": "To reduce model complexity", "is_correct": False}
                            ],
                            "explanation": "K-Means clustering groups data points into clusters based on their similarity, without predefined categories.",
                            "resources": [
                                {"title": "K-Means Clustering", "url": "https://scikit-learn.org/stable/modules/clustering.html#k-means"}
                            ]
                        },
                        {
                            "text": "What is Principal Component Analysis (PCA) used for?",
                            "choices": [
                                {"text": "To increase the number of features", "is_correct": False},
                                {"text": "To reduce dimensionality while preserving variance", "is_correct": True},
                                {"text": "To improve model accuracy", "is_correct": False},
                                {"text": "To cluster data", "is_correct": False}
                            ],
                            "explanation": "PCA reduces the number of features while preserving as much variance as possible in the data.",
                            "resources": [
                                {"title": "Principal Component Analysis", "url": "https://scikit-learn.org/stable/modules/decomposition.html#pca"}
                            ]
                        },
                        {
                            "text": "What is hierarchical clustering?",
                            "choices": [
                                {"text": "A clustering method that builds a tree of clusters", "is_correct": True},
                                {"text": "A method that requires knowing the number of clusters beforehand", "is_correct": False},
                                {"text": "Both A and B", "is_correct": False},
                                {"text": "A type of supervised learning", "is_correct": False}
                            ],
                            "explanation": "Hierarchical clustering builds a tree-like structure of clusters, showing relationships between different levels of clustering.",
                            "resources": [
                                {"title": "Hierarchical Clustering", "url": "https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering"}
                            ]
                        },
                        {
                            "text": "What is t-SNE used for?",
                            "choices": [
                                {"text": "To visualize high-dimensional data in 2D or 3D", "is_correct": True},
                                {"text": "To improve model performance", "is_correct": False},
                                {"text": "To classify data", "is_correct": False},
                                {"text": "To predict values", "is_correct": False}
                            ],
                            "explanation": "t-SNE (t-Distributed Stochastic Neighbor Embedding) is used for dimensionality reduction and visualization of high-dimensional data.",
                            "resources": [
                                {"title": "t-SNE", "url": "https://scikit-learn.org/stable/modules/manifold.html#t-sne"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Unsupervised Learning Quiz 2",
                    "description": "Test your understanding of clustering and dimensionality reduction",
                    "questions": [
                        {
                            "text": "What is the main goal of K-Means clustering?",
                            "choices": [
                                {"text": "To classify data into predefined categories", "is_correct": False},
                                {"text": "To group similar data points together", "is_correct": True},
                                {"text": "To predict continuous values", "is_correct": False},
                                {"text": "To reduce model complexity", "is_correct": False}
                            ],
                            "explanation": "K-Means clustering groups data points into clusters based on their similarity, without predefined categories.",
                            "resources": [
                                {"title": "K-Means Clustering", "url": "https://scikit-learn.org/stable/modules/clustering.html#k-means"}
                            ]
                        },
                        {
                            "text": "What is Principal Component Analysis (PCA) used for?",
                            "choices": [
                                {"text": "To increase the number of features", "is_correct": False},
                                {"text": "To reduce dimensionality while preserving variance", "is_correct": True},
                                {"text": "To improve model accuracy", "is_correct": False},
                                {"text": "To cluster data", "is_correct": False}
                            ],
                            "explanation": "PCA reduces the number of features while preserving as much variance as possible in the data.",
                            "resources": [
                                {"title": "Principal Component Analysis", "url": "https://scikit-learn.org/stable/modules/decomposition.html#pca"}
                            ]
                        },
                        {
                            "text": "What is hierarchical clustering?",
                            "choices": [
                                {"text": "A clustering method that builds a tree of clusters", "is_correct": True},
                                {"text": "A method that requires knowing the number of clusters beforehand", "is_correct": False},
                                {"text": "Both A and B", "is_correct": False},
                                {"text": "A type of supervised learning", "is_correct": False}
                            ],
                            "explanation": "Hierarchical clustering builds a tree-like structure of clusters, showing relationships between different levels of clustering.",
                            "resources": [
                                {"title": "Hierarchical Clustering", "url": "https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering"}
                            ]
                        },
                        {
                            "text": "What is t-SNE used for?",
                            "choices": [
                                {"text": "To visualize high-dimensional data in 2D or 3D", "is_correct": True},
                                {"text": "To improve model performance", "is_correct": False},
                                {"text": "To classify data", "is_correct": False},
                                {"text": "To predict values", "is_correct": False}
                            ],
                            "explanation": "t-SNE (t-Distributed Stochastic Neighbor Embedding) is used for dimensionality reduction and visualization of high-dimensional data.",
                            "resources": [
                                {"title": "t-SNE", "url": "https://scikit-learn.org/stable/modules/manifold.html#t-sne"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Deep Learning Basics",
            "description": "Introduction to neural networks and deep learning",
            "quizzes": [
                {
                    "title": "Deep Learning Basics Quiz",
                    "description": "Test your understanding of neural networks and deep learning concepts",
                    "questions": [
                        {
                            "text": "What is a neural network?",
                            "choices": [
                                {"text": "A network of interconnected nodes that process information", "is_correct": True},
                                {"text": "A type of decision tree", "is_correct": False},
                                {"text": "A clustering algorithm", "is_correct": False},
                                {"text": "A regression model", "is_correct": False}
                            ],
                            "explanation": "A neural network consists of interconnected nodes (neurons) that process and transmit information to learn patterns.",
                            "resources": [
                                {"title": "Neural Networks", "url": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html"}
                            ]
                        },
                        {
                            "text": "What is backpropagation?",
                            "choices": [
                                {"text": "A method to update neural network weights", "is_correct": True},
                                {"text": "A type of clustering", "is_correct": False},
                                {"text": "A dimensionality reduction technique", "is_correct": False},
                                {"text": "A classification algorithm", "is_correct": False}
                            ],
                            "explanation": "Backpropagation is an algorithm that calculates gradients and updates weights in neural networks to minimize error.",
                            "resources": [
                                {"title": "Backpropagation", "url": "https://en.wikipedia.org/wiki/Backpropagation"}
                            ]
                        },
                        {
                            "text": "What is a Convolutional Neural Network (CNN) primarily used for?",
                            "choices": [
                                {"text": "Image processing and computer vision", "is_correct": True},
                                {"text": "Text processing", "is_correct": False},
                                {"text": "Time series analysis", "is_correct": False},
                                {"text": "Clustering", "is_correct": False}
                            ],
                            "explanation": "CNNs are specifically designed for processing grid-like data such as images, using convolutional layers to detect features.",
                            "resources": [
                                {"title": "Convolutional Neural Networks", "url": "https://en.wikipedia.org/wiki/Convolutional_neural_network"}
                            ]
                        },
                        {
                            "text": "What is a Recurrent Neural Network (RNN) used for?",
                            "choices": [
                                {"text": "Processing sequential data", "is_correct": True},
                                {"text": "Image classification", "is_correct": False},
                                {"text": "Clustering", "is_correct": False},
                                {"text": "Dimensionality reduction", "is_correct": False}
                            ],
                            "explanation": "RNNs are designed to process sequential data by maintaining internal memory of previous inputs.",
                            "resources": [
                                {"title": "Recurrent Neural Networks", "url": "https://en.wikipedia.org/wiki/Recurrent_neural_network"}
                            ]
                        },
                        {
                            "text": "What is transfer learning?",
                            "choices": [
                                {"text": "Using a pre-trained model for a new task", "is_correct": True},
                                {"text": "Transferring data between models", "is_correct": False},
                                {"text": "A type of clustering", "is_correct": False},
                                {"text": "A dimensionality reduction technique", "is_correct": False}
                            ],
                            "explanation": "Transfer learning involves using a model trained on one task and adapting it for a different but related task.",
                            "resources": [
                                {"title": "Transfer Learning", "url": "https://en.wikipedia.org/wiki/Transfer_learning"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Deep Learning Basics Quiz 2",
                    "description": "Test your understanding of neural networks and deep learning concepts",
                    "questions": [
                        {
                            "text": "What is a neural network?",
                            "choices": [
                                {"text": "A network of interconnected nodes that process information", "is_correct": True},
                                {"text": "A type of decision tree", "is_correct": False},
                                {"text": "A clustering algorithm", "is_correct": False},
                                {"text": "A regression model", "is_correct": False}
                            ],
                            "explanation": "A neural network consists of interconnected nodes (neurons) that process and transmit information to learn patterns.",
                            "resources": [
                                {"title": "Neural Networks", "url": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html"}
                            ]
                        },
                        {
                            "text": "What is backpropagation?",
                            "choices": [
                                {"text": "A method to update neural network weights", "is_correct": True},
                                {"text": "A type of clustering", "is_correct": False},
                                {"text": "A dimensionality reduction technique", "is_correct": False},
                                {"text": "A classification algorithm", "is_correct": False}
                            ],
                            "explanation": "Backpropagation is an algorithm that calculates gradients and updates weights in neural networks to minimize error.",
                            "resources": [
                                {"title": "Backpropagation", "url": "https://en.wikipedia.org/wiki/Backpropagation"}
                            ]
                        },
                        {
                            "text": "What is a Convolutional Neural Network (CNN) primarily used for?",
                            "choices": [
                                {"text": "Image processing and computer vision", "is_correct": True},
                                {"text": "Text processing", "is_correct": False},
                                {"text": "Time series analysis", "is_correct": False},
                                {"text": "Clustering", "is_correct": False}
                            ],
                            "explanation": "CNNs are specifically designed for processing grid-like data such as images, using convolutional layers to detect features.",
                            "resources": [
                                {"title": "Convolutional Neural Networks", "url": "https://en.wikipedia.org/wiki/Convolutional_neural_network"}
                            ]
                        },
                        {
                            "text": "What is a Recurrent Neural Network (RNN) used for?",
                            "choices": [
                                {"text": "Processing sequential data", "is_correct": True},
                                {"text": "Image classification", "is_correct": False},
                                {"text": "Clustering", "is_correct": False},
                                {"text": "Dimensionality reduction", "is_correct": False}
                            ],
                            "explanation": "RNNs are designed to process sequential data by maintaining internal memory of previous inputs.",
                            "resources": [
                                {"title": "Recurrent Neural Networks", "url": "https://en.wikipedia.org/wiki/Recurrent_neural_network"}
                            ]
                        },
                        {
                            "text": "What is transfer learning?",
                            "choices": [
                                {"text": "Using a pre-trained model for a new task", "is_correct": True},
                                {"text": "Transferring data between models", "is_correct": False},
                                {"text": "A type of clustering", "is_correct": False},
                                {"text": "A dimensionality reduction technique", "is_correct": False}
                            ],
                            "explanation": "Transfer learning involves using a model trained on one task and adapting it for a different but related task.",
                            "resources": [
                                {"title": "Transfer Learning", "url": "https://en.wikipedia.org/wiki/Transfer_learning"}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
} 