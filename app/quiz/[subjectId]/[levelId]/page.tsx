// =============================================================================
// QUIZ PAGE COMPONENT
// =============================================================================
// This page displays individual quiz questions for a specific subject and level.
// Handles quiz progression, answer submission, scoring, and completion tracking.
// Includes timer functionality and immediate feedback for each question.

"use client"

// Import React hooks for state management and side effects
import { useState, useEffect } from "react"
// Import UI components from the design system
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { Alert, AlertDescription } from "@/components/ui/alert"
// Import icons from Lucide React
import { ArrowLeft, Clock, CheckCircle, XCircle, ArrowRight, BookOpen, ExternalLink, RotateCcw, Loader2 } from "lucide-react"
// Import Next.js routing components
import Link from "next/link"
import { useRouter, useParams } from "next/navigation"
// Import API functions for quiz interaction
import { updateUserProgress, completeQuizLevel, getUserSubjects, getUserActivity, submitQuiz, getQuiz } from "@/lib/api"

export default function QuizPage() {
  // Get route parameters for subject and level IDs
  const params = useParams()
  const router = useRouter()
  const subjectId = Number.parseInt(params.subjectId as string) // Convert string to number
  const levelId = Number.parseInt(params.levelId as string) // Convert string to number

  // Quiz state management
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0) // Track current question
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null) // User's selected answer
  const [showResult, setShowResult] = useState(false) // Show feedback for current question
  const [answers, setAnswers] = useState<{ [key: number]: string }>({}) // Store all user answers
  const [timeLeft, setTimeLeft] = useState(300) // Timer: 5 minutes (300 seconds)
  const [quizCompleted, setQuizCompleted] = useState(false) // Quiz completion status
  const [score, setScore] = useState(0) // Final quiz score percentage
  const [result, setResult] = useState<any>(null) // Quiz submission result
  const [error, setError] = useState<string | null>(null) // Error message state
  const [currentQuiz, setCurrentQuiz] = useState<any>(null) // Current quiz data
  const [loading, setLoading] = useState(true) // Loading state for data fetching

  // Effect hook to fetch quiz data when component mounts or parameters change
  useEffect(() => {
    const fetchQuiz = async () => {
      try {
        setLoading(true) // Show loading state
        const quizData = await getQuiz(subjectId, levelId) // Fetch quiz from API
        setCurrentQuiz(quizData) // Store quiz data in state
        setTimeLeft(300) // Reset timer to 5 minutes
      } catch (err) {
        setError("Failed to load quiz") // Set error message
        console.error("Error fetching quiz:", err) // Log error for debugging
      } finally {
        setLoading(false) // Hide loading state
      }
    }

    // Only fetch if we have valid subject and level IDs
    if (subjectId && levelId) {
      fetchQuiz()
    }
  }, [subjectId, levelId]) // Re-run when subject or level changes

  // Effect hook to handle quiz timer countdown
  useEffect(() => {
    if (!currentQuiz || quizCompleted) return // Don't run timer if no quiz or already completed

    const timer = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          handleShowResult() // Auto-submit when time runs out
          return 0
        }
        return prev - 1 // Decrease timer by 1 second
      })
    }, 1000) // Update every second

    return () => clearInterval(timer) // Cleanup timer on unmount
  }, [currentQuiz, quizCompleted]) // Re-run when quiz data or completion status changes

  // Get the current question from the quiz data
  const currentQuestion = currentQuiz?.questions?.[currentQuestionIndex]

  // Handle user selecting an answer for the current question
  const handleAnswerSelect = (answer: string) => {
    setSelectedAnswer(answer) // Update selected answer for current question
    setAnswers((prev) => ({ ...prev, [currentQuestionIndex]: answer })) // Store answer in answers object
  }

  // Handle progression to next question or quiz completion
  const handleNextQuestion = () => {
    if (selectedAnswer) {
      if (currentQuestionIndex < currentQuiz.questions.length - 1) {
        // Move to next question
        setCurrentQuestionIndex(currentQuestionIndex + 1)
        setSelectedAnswer(null) // Reset selected answer for new question
        setShowResult(false) // Hide result feedback
      } else {
        // This is the last question, complete the quiz
        setQuizCompleted(true)
        // Calculate final score
        let correctCount = 0
        currentQuiz.questions.forEach((question: any, index: number) => {
          if (answers[index] === question.correct) {
            correctCount++
          }
        })
        setScore(Math.round((correctCount / currentQuiz.questions.length) * 100)) // Calculate percentage
        // Call handleQuizComplete to save progress in backend
        handleQuizComplete();
      }
    }
  }

  // Show feedback for current question without completing quiz
  const handleShowResult = () => {
    setShowResult(true) // Show immediate feedback for current question
    // Don't complete the quiz yet, just show feedback for current question
  }

  const handleQuizComplete = async () => {
    try {
      const token = localStorage.getItem("authToken")
      if (token) {
        await submitQuiz(subjectId, levelId, answers, token)
        // Redirect to subject page to refresh progress
        router.push(`/subject/${subjectId}`)
      }
    } catch (err) {
      console.error("Error completing quiz:", err)
      // Still redirect even if submission fails
      router.push(`/subject/${subjectId}`)
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
      const res = await submitQuiz(subjectId, levelId, answers, token as string | undefined);
      setResult(res);
      setCurrentQuiz(null);
      // Optionally, refetch user subjects/activity or refresh dashboard/subject page
      // router.refresh(); // Uncomment if using Next.js 13+ for route refresh
    } catch {
      setError("Failed to submit quiz");
    }
  };

  // Loading state
  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <Loader2 className="w-8 h-8 animate-spin mx-auto mb-4 text-blue-600" />
          <h1 className="text-xl font-semibold text-slate-900 mb-2">Loading Quiz...</h1>
          <p className="text-slate-600">Please wait while we prepare your quiz</p>
        </div>
      </div>
    )
  }

  // Error state
  if (error || !currentQuiz) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-slate-900 mb-4">Quiz Not Found</h1>
          <p className="text-slate-600 mb-6">The quiz you're looking for doesn't exist or is not available.</p>
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
                <Button
                  variant="outline"
                  onClick={handleShowResult}
                  disabled={!selectedAnswer || showResult}
                >
                  {showResult ? "Answer Checked" : "Check Answer"}
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
