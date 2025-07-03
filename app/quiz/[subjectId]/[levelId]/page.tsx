"use client"

import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { ArrowLeft, Clock, CheckCircle, XCircle, ArrowRight, BookOpen, ExternalLink, RotateCcw } from "lucide-react"
import Link from "next/link"
import { useRouter, useParams } from "next/navigation"
import { updateUserProgress, completeQuizLevel, getUserSubjects, getUserActivity, submitQuiz } from "@/lib/api"

export default function QuizPage() {
  const params = useParams()
  const router = useRouter()
  const subjectId = Number.parseInt(params.subjectId as string)
  const levelId = Number.parseInt(params.levelId as string)

  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null)
  const [showResult, setShowResult] = useState(false)
  const [answers, setAnswers] = useState<{ [key: number]: string }>({})
  const [timeLeft, setTimeLeft] = useState(300) // 5 minutes
  const [quizCompleted, setQuizCompleted] = useState(false)
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)

  // Sample quiz data
  const quizData = {
    1: {
      // Python Programming
      1: {
        // Variables & Data Types
        title: "Python Variables & Data Types",
        description: "Test your understanding of Python variables and basic data types",
        timeLimit: 300,
        questions: [
          {
            id: 1,
            question: "Which of the following is NOT a valid Python variable name?",
            options: ["my_var", "2variable", "_private", "Variable"],
            correct: "2variable",
            explanation:
              "Variable names in Python cannot start with a number. They must start with a letter or underscore.",
            resources: [
              {
                title: "Python Variable Naming Rules",
                url: "https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator",
              },
              { title: "PEP 8 Style Guide", url: "https://pep8.org/" },
            ],
          },
          {
            id: 2,
            question: "What is the data type of the value 3.14 in Python?",
            options: ["int", "float", "double", "decimal"],
            correct: "float",
            explanation: "In Python, decimal numbers are represented as float data type.",
            resources: [
              {
                title: "Python Numeric Types",
                url: "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex",
              },
            ],
          },
          {
            id: 3,
            question: "Which function is used to determine the type of a variable in Python?",
            options: ["typeof()", "type()", "gettype()", "datatype()"],
            correct: "type()",
            explanation: "The type() function returns the type of an object in Python.",
            resources: [
              { title: "Built-in Functions - type()", url: "https://docs.python.org/3/library/functions.html#type" },
            ],
          },
          {
            id: 4,
            question: 'What will be the output of: print(type("Hello"))?',
            options: ["<class 'string'>", "<class 'str'>", "<type 'str'>", "string"],
            correct: "<class 'str'>",
            explanation: "In Python 3, strings are of type 'str' and type() returns <class 'str'>.",
            resources: [
              {
                title: "Python String Type",
                url: "https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str",
              },
            ],
          },
          {
            id: 5,
            question: "Which of the following creates a string in Python?",
            options: [
              "Both single and double quotes",
              "Only double quotes",
              "Only single quotes",
              "Only triple quotes",
            ],
            correct: "Both single and double quotes",
            explanation: "Python allows strings to be created using both single quotes (') and double quotes (\").",
            resources: [
              {
                title: "Python String Literals",
                url: "https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals",
              },
            ],
          },
        ],
      },
      3: {
        // Functions & Modules
        title: "Python Functions & Modules",
        description: "Test your knowledge of Python functions and module system",
        timeLimit: 300,
        questions: [
          {
            id: 1,
            question: "What keyword is used to define a function in Python?",
            options: ["function", "def", "define", "func"],
            correct: "def",
            explanation: "The 'def' keyword is used to define functions in Python.",
            resources: [
              {
                title: "Python Functions",
                url: "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
              },
            ],
          },
          {
            id: 2,
            question: "What does the return statement do in a Python function?",
            options: [
              "Ends the function",
              "Returns a value",
              "Both ends the function and returns a value",
              "Prints a value",
            ],
            correct: "Both ends the function and returns a value",
            explanation: "The return statement exits the function and optionally returns a value to the caller.",
            resources: [
              {
                title: "Return Statement",
                url: "https://docs.python.org/3/reference/simple_stmts.html#the-return-statement",
              },
            ],
          },
          {
            id: 3,
            question: "How do you import a specific function from a module?",
            options: [
              "import function from module",
              "from module import function",
              "import module.function",
              "get function from module",
            ],
            correct: "from module import function",
            explanation: "Use 'from module import function' to import specific functions from a module.",
            resources: [
              {
                title: "Import Statement",
                url: "https://docs.python.org/3/reference/simple_stmts.html#the-import-statement",
              },
            ],
          },
        ],
      },
    },
    2: {
      // Machine Learning
      1: {
        // ML Fundamentals
        title: "Machine Learning Fundamentals",
        description: "Test your understanding of basic ML concepts",
        timeLimit: 300,
        questions: [
          {
            id: 1,
            question: "What is the main goal of supervised learning?",
            options: [
              "Find hidden patterns",
              "Learn from labeled data",
              "Reduce dimensionality",
              "Cluster similar data",
            ],
            correct: "Learn from labeled data",
            explanation: "Supervised learning uses labeled training data to learn a mapping from inputs to outputs.",
            resources: [
              {
                title: "Supervised Learning Overview",
                url: "https://scikit-learn.org/stable/supervised_learning.html",
              },
            ],
          },
          {
            id: 2,
            question: "What is overfitting in machine learning?",
            options: [
              "Model is too simple",
              "Model performs well on training but poorly on test data",
              "Model has too few parameters",
              "Model trains too slowly",
            ],
            correct: "Model performs well on training but poorly on test data",
            explanation:
              "Overfitting occurs when a model learns the training data too well, including noise, leading to poor generalization.",
            resources: [
              {
                title: "Overfitting and Underfitting",
                url: "https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html",
              },
            ],
          },
        ],
      },
    },
  }

  const currentQuiz = (quizData[subjectId as keyof typeof quizData]?.[levelId as keyof (typeof quizData)[1]]) as any;
  const currentQuestion = currentQuiz?.questions[currentQuestionIndex]

  // Timer effect
  useEffect(() => {
    if (timeLeft > 0 && !quizCompleted) {
      const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000)
      return () => clearTimeout(timer)
    } else if (timeLeft === 0) {
      handleQuizComplete()
    }
  }, [timeLeft, quizCompleted])

  const handleAnswerSelect = (answer: string) => {
    setSelectedAnswer(answer)
  }

  const handleNextQuestion = () => {
    if (selectedAnswer) {
      setAnswers((prev) => ({
        ...prev,
        [currentQuestionIndex]: selectedAnswer,
      }))

      if (currentQuestionIndex < currentQuiz.questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1)
        setSelectedAnswer(null)
        setShowResult(false)
      } else {
        handleQuizComplete()
      }
    }
  }

  const handleShowResult = () => {
    setShowResult(true)
  }

  const handleQuizComplete = async () => {
    const finalAnswers = { ...answers, [currentQuestionIndex]: selectedAnswer }
    let correctCount = 0

    currentQuiz.questions.forEach((question: any, index: number) => {
      if (finalAnswers[index] === question.correct) {
        correctCount++
      }
    })

    setScore(Math.round((correctCount / currentQuiz.questions.length) * 100))
    setQuizCompleted(true)

    // --- SUBMIT QUIZ TO BACKEND ---
    try {
      const token = localStorage.getItem("authToken");
      await submitQuiz(subjectId, levelId, finalAnswers, token);
      // After successful submission, redirect to subject page to refresh progress
      setTimeout(() => {
        window.location.href = `/subject/${subjectId}`;
      }, 1200); // Give user a moment to see their score
    } catch {
      setError("Failed to submit quiz");
    }
  }

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, "0")}`
  }

  const handleSubmit = async () => {
    try {
      const token = localStorage.getItem("authToken");
      const res = await submitQuiz(subjectId, levelId, answers, token);
      setResult(res);
      setQuiz(null);
      // Optionally, refetch user subjects/activity or refresh dashboard/subject page
      // router.refresh(); // Uncomment if using Next.js 13+ for route refresh
    } catch {
      setError("Failed to submit quiz");
    }
  };

  if (!currentQuiz) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-slate-900 mb-4">Quiz Not Found</h1>
          <Link href="/dashboard">
            <Button>Back to Dashboard</Button>
          </Link>
        </div>
      </div>
    )
  }

  if (quizCompleted) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
        <div className="container mx-auto px-4 py-8">
          <Card className="max-w-2xl mx-auto border-0 shadow-xl bg-white/80 backdrop-blur-sm">
            <CardHeader className="text-center">
              <div
                className={`w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center ${score >= 70 ? "bg-green-100" : "bg-red-100"
                  }`}
              >
                {score >= 70 ? (
                  <CheckCircle className="w-8 h-8 text-green-600" />
                ) : (
                  <XCircle className="w-8 h-8 text-red-600" />
                )}
              </div>
              <CardTitle className="text-2xl">Quiz Completed!</CardTitle>
              <CardDescription>Here are your results</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="text-center">
                <div className={`text-4xl font-bold mb-2 ${score >= 70 ? "text-green-600" : "text-red-600"}`}>
                  {score}%
                </div>
                <p className="text-slate-600">
                  You got{" "}
                  {
                    Object.values(answers).filter((answer: string, index: number) => answer === currentQuiz.questions[index]?.correct)
                      .length
                  }{" "}
                  out of {currentQuiz.questions.length} questions correct
                </p>
              </div>

              <div className="space-y-4">
                <h3 className="font-semibold text-slate-900">Question Review:</h3>
                {currentQuiz.questions.map((question: any, index: number) => {
                  const userAnswer = answers[index]
                  const isCorrect = userAnswer === question.correct

                  return (
                    <div
                      key={question.id}
                      className={`p-4 rounded-lg border-2 ${isCorrect ? "border-green-200 bg-green-50" : "border-red-200 bg-red-50"
                        }`}
                    >
                      <div className="flex items-start space-x-3">
                        {isCorrect ? (
                          <CheckCircle className="w-5 h-5 text-green-600 mt-0.5" />
                        ) : (
                          <XCircle className="w-5 h-5 text-red-600 mt-0.5" />
                        )}
                        <div className="flex-1">
                          <p className="font-medium text-slate-900 mb-2">{question.question}</p>
                          <div className="space-y-1 text-sm">
                            <p className={isCorrect ? "text-green-700" : "text-red-700"}>
                              Your answer: {userAnswer || "No answer"}
                            </p>
                            {!isCorrect && <p className="text-green-700">Correct answer: {question.correct}</p>}
                            <p className="text-slate-600 mt-2">{question.explanation}</p>
                            {!isCorrect && question.resources && (
                              <div className="mt-3">
                                <p className="font-medium text-slate-700 mb-2">Additional Resources:</p>
                                <div className="space-y-1">
                                  {question.resources.map((resource: any, resourceIndex: number) => (
                                    <a
                                      key={resourceIndex}
                                      href={resource.url}
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      className="flex items-center text-blue-600 hover:text-blue-700 text-sm"
                                    >
                                      <ExternalLink className="w-3 h-3 mr-1" />
                                      {resource.title}
                                    </a>
                                  ))}
                                </div>
                              </div>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  )
                })}
              </div>

              <div className="flex flex-col sm:flex-row gap-4 pt-4">
                <Button
                  variant="outline"
                  className="w-full bg-transparent flex-1"
                  onClick={() => window.location.href = `/subject/${subjectId}`}
                >
                  <ArrowLeft className="w-4 h-4 mr-2" />
                  Back to Subject
                </Button>
                <Button onClick={() => window.location.reload()} className="flex-1">
                  <RotateCcw className="w-4 h-4 mr-2" />
                  Retake Quiz
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Link href={`/subject/${subjectId}`}>
                <Button variant="ghost" size="sm">
                  <ArrowLeft className="w-4 h-4 mr-2" />
                  Back
                </Button>
              </Link>
              <div>
                <h1 className="text-lg font-bold text-slate-900">{currentQuiz.title}</h1>
                <p className="text-sm text-slate-600">{currentQuiz.description}</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Badge variant="outline" className="flex items-center space-x-1">
                <Clock className="w-3 h-3" />
                <span>{formatTime(timeLeft)}</span>
              </Badge>
              <Badge variant="secondary">
                {currentQuestionIndex + 1} / {currentQuiz.questions.length}
              </Badge>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        <div className="max-w-3xl mx-auto">
          {/* Progress */}
          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm mb-6">
            <CardContent className="p-6">
              <div className="flex justify-between text-sm mb-2">
                <span className="text-slate-600">Progress</span>
                <span className="font-medium">
                  {currentQuestionIndex + 1} of {currentQuiz.questions.length} questions
                </span>
              </div>
              <Progress value={((currentQuestionIndex + 1) / currentQuiz.questions.length) * 100} className="h-2" />
            </CardContent>
          </Card>

          {/* Question */}
          <Card className="border-0 shadow-xl bg-white/80 backdrop-blur-sm">
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="text-xl">Question {currentQuestionIndex + 1}</CardTitle>
                <Badge variant="outline">
                  <BookOpen className="w-3 h-3 mr-1" />
                  Multiple Choice
                </Badge>
              </div>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="text-lg text-slate-900 leading-relaxed">{currentQuestion.question}</div>

              <div className="space-y-3">
                {currentQuestion.options.map((option: string, index: number) => (
                  <button
                    key={index}
                    onClick={() => handleAnswerSelect(option)}
                    className={`w-full p-4 text-left rounded-lg border-2 transition-all ${selectedAnswer === option
                      ? "border-blue-500 bg-blue-50"
                      : "border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50"
                      }`}
                  >
                    <div className="flex items-center space-x-3">
                      <div
                        className={`w-4 h-4 rounded-full border-2 ${selectedAnswer === option ? "border-blue-500 bg-blue-500" : "border-slate-300"
                          }`}
                      >
                        {selectedAnswer === option && <div className="w-full h-full rounded-full bg-white scale-50" />}
                      </div>
                      <span className="text-slate-900">{option}</span>
                    </div>
                  </button>
                ))}
              </div>

              {showResult && (
                <Alert
                  className={`${selectedAnswer === currentQuestion.correct
                    ? "border-green-200 bg-green-50"
                    : "border-red-200 bg-red-50"
                    }`}
                >
                  <div className="flex items-start space-x-3">
                    {selectedAnswer === currentQuestion.correct ? (
                      <CheckCircle className="w-5 h-5 text-green-600 mt-0.5" />
                    ) : (
                      <XCircle className="w-5 h-5 text-red-600 mt-0.5" />
                    )}
                    <div className="flex-1">
                      <AlertDescription
                        className={selectedAnswer === currentQuestion.correct ? "text-green-700" : "text-red-700"}
                      >
                        <div className="font-medium mb-2">
                          {selectedAnswer === currentQuestion.correct ? "Correct!" : "Incorrect"}
                        </div>
                        <div className="text-slate-700 mb-3">{currentQuestion.explanation}</div>
                        {selectedAnswer !== currentQuestion.correct && currentQuestion.resources && (
                          <div>
                            <div className="font-medium text-slate-700 mb-2">Additional Resources:</div>
                            <div className="space-y-1">
                              {currentQuestion.resources.map((resource: any, resourceIndex: number) => (
                                <a
                                  key={resourceIndex}
                                  href={resource.url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="flex items-center text-blue-600 hover:text-blue-700 text-sm"
                                >
                                  <ExternalLink className="w-3 h-3 mr-1" />
                                  {resource.title}
                                </a>
                              ))}
                            </div>
                          </div>
                        )}
                      </AlertDescription>
                    </div>
                  </div>
                </Alert>
              )}

              <div className="flex justify-between pt-4">
                <Button variant="outline" onClick={handleShowResult} disabled={!selectedAnswer || showResult}>
                  Check Answer
                </Button>
                <Button onClick={handleNextQuestion} disabled={!showResult} className="bg-blue-600 hover:bg-blue-700">
                  {currentQuestionIndex < currentQuiz.questions.length - 1 ? (
                    <>
                      Next Question
                      <ArrowRight className="w-4 h-4 ml-2" />
                    </>
                  ) : (
                    "Complete Quiz"
                  )}
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
