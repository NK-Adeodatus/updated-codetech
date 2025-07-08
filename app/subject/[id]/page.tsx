// =============================================================================
// SUBJECT PAGE COMPONENT
// =============================================================================
// This page displays detailed information about a specific subject.
// Shows progress, levels, and learning path for the selected subject.
// Includes authentication checks and progress tracking.

"use client"

// Import UI components from the design system
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
// Import icons from Lucide React
import { ArrowLeft, Play, Lock, CheckCircle, BookOpen, Clock, Target, Trophy, Code } from "lucide-react"
// Import Next.js routing components
import Link from "next/link"
import { useRouter, useParams } from "next/navigation"
// Import React hooks for state management and side effects
import { useEffect, useState } from "react"
// Import API functions for subject data
import { getUserSubjects, getSubject } from "@/lib/api"

export default function SubjectPage() {
  // Get route parameters and router instance
  const params = useParams()
  const router = useRouter()
  const subjectId = Number.parseInt(params.id as string) // Convert string ID to number

  // State management for subject data
  const [subject, setSubject] = useState<any>(null) // Current subject data
  const [loading, setLoading] = useState(true) // Loading state for data fetching
  const [error, setError] = useState("") // Error message state

  // Effect hook to load subject data when component mounts or subject ID changes
  useEffect(() => {
    setLoading(true) // Show loading state
    const token = localStorage.getItem("authToken")
    if (!token) {
      setError("Not authenticated") // Set error if no authentication token
      setLoading(false)
      return
    }
    // Fetch user's subjects and find the specific subject
    getUserSubjects(token)
      .then((subjects) => {
        const subj = subjects.find((s: any) => s.id === subjectId) // Find subject by ID
        if (!subj) throw new Error() // Throw error if subject not found
        setSubject(subj) // Set subject data in state
      })
      .catch(() => setError("Subject Not Found")) // Handle errors
      .finally(() => setLoading(false)) // Hide loading state
  }, [subjectId]) // Re-run when subject ID changes

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-slate-900 mb-4">Loading...</h1>
          {error && <p className="text-red-500">{error}</p>}
          <Link href="/dashboard">
            <Button>Back to Dashboard</Button>
          </Link>
        </div>
      </div>
    )
  }

  if (!subject) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-slate-900 mb-4">{error || "Subject Not Found"}</h1>
          <Link href="/dashboard">
            <Button>Back to Dashboard</Button>
          </Link>
        </div>
      </div>
    )
  }

  // Calculate currentLevel and totalLevels for display
  let currentLevel = 1;
  let totalLevels = subject?.levels?.length || 1;
  if (subject && Array.isArray(subject.levels)) {
    for (let i = 0; i < subject.levels.length; i++) {
      if (subject.levels[i].current) {
        currentLevel = i + 1;
        break;
      }
      // If all completed, show last as current
      if (i === subject.levels.length - 1) {
        currentLevel = subject.levels.length;
      }
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Link href="/dashboard">
                <Button variant="ghost" size="sm">
                  <ArrowLeft className="w-4 h-4 mr-2" />
                  Dashboard
                </Button>
              </Link>
              <div className="flex items-center space-x-3">
                <div className={`w-10 h-10 ${subject.color} rounded-lg flex items-center justify-center text-2xl`}>
                  {subject.icon}
                </div>
                <div>
                  <h1 className="text-xl font-bold text-slate-900">{subject.name}</h1>
                  <p className="text-sm text-slate-600">{subject.description}</p>
                </div>
              </div>
            </div>
            <Link href="/dashboard">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Code className="w-5 h-5 text-white" />
              </div>
            </Link>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        {/* Subject Overview */}
        <div className="grid lg:grid-cols-4 gap-8 mb-8">
          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-6 text-center">
              <BookOpen className="w-8 h-8 text-blue-600 mx-auto mb-3" />
              <div className="text-2xl font-bold text-slate-900 mb-1">
                {subject.completedQuizzes}/{subject.totalQuizzes}
              </div>
              <div className="text-sm text-slate-600">Quizzes Completed</div>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-6 text-center">
              <Target className="w-8 h-8 text-green-600 mx-auto mb-3" />
              <div className="text-2xl font-bold text-slate-900 mb-1">{subject.progress}%</div>
              <div className="text-sm text-slate-600">Overall Progress</div>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-6 text-center">
              <Trophy className="w-8 h-8 text-purple-600 mx-auto mb-3" />
              <div className="text-2xl font-bold text-slate-900 mb-1">
                {currentLevel}/{totalLevels}
              </div>
              <div className="text-sm text-slate-600">Current Level</div>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-6 text-center">
              <Clock className="w-8 h-8 text-yellow-600 mx-auto mb-3" />
              <div className="text-2xl font-bold text-slate-900 mb-1">
                {subject.levels.reduce((acc: number, level: any) => acc + Number.parseInt(level.estimatedTime), 0)}h
              </div>
              <div className="text-sm text-slate-600">Total Time</div>
            </CardContent>
          </Card>
        </div>

        {/* Progress Overview */}
        <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm mb-8">
          <CardHeader>
            <CardTitle>Learning Progress</CardTitle>
            <CardDescription>Track your journey through {subject.name}</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex justify-between text-sm">
                <span className="text-slate-600">Overall Progress</span>
                <span className="font-medium">{subject.progress}%</span>
              </div>
              <Progress value={subject.progress} className="h-3" />
              <div className="flex justify-between text-sm text-slate-600">
                <span>
                  Level {currentLevel} of {totalLevels}
                </span>
                <span>
                  {subject.completedQuizzes} of {subject.totalQuizzes} quizzes completed
                </span>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Learning Path */}
        <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
          <CardHeader>
            <CardTitle>Learning Path</CardTitle>
            <CardDescription>Complete levels in order to build your knowledge progressively</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-6">
              {subject.levels.map((level: any, index: number) => {
                // Determine button state
                let actionButton = null;
                if (level.completed) {
                  actionButton = (
                    <Link href={`/quiz/${subject.id}/${level.id}`}>
                      <Button variant="outline" size="sm">
                        <CheckCircle className="w-4 h-4 mr-2" />
                        Review
                      </Button>
                    </Link>
                  );
                } else if (level.unlocked) {
                  actionButton = (
                    <Link href={`/quiz/${subject.id}/${level.id}`}>
                      <Button size="sm" className="bg-blue-600 hover:bg-blue-700">
                        <Play className="w-4 h-4 mr-2" />
                        {index === 0 || subject.levels[index - 1].completed ? "Start" : "Continue"} Quiz
                      </Button>
                    </Link>
                  );
                } else {
                  actionButton = (
                    <Button variant="outline" size="sm" disabled>
                      <Lock className="w-4 h-4 mr-2" />
                      Locked
                    </Button>
                  );
                }
                return (
                  <div key={level.id} className="relative">
                    {/* Connection Line */}
                    {index < subject.levels.length - 1 && (
                      <div className="absolute left-6 top-16 w-0.5 h-16 bg-slate-200" />
                    )}

                    <div
                      className={`flex items-start space-x-4 p-6 rounded-lg border-2 transition-all ${level.completed
                        ? "border-green-200 bg-green-50"
                        : level.current
                          ? "border-blue-200 bg-blue-50"
                          : "border-slate-200 bg-slate-50"
                        }`}
                    >
                      {/* Status Icon */}
                      <div className="flex-shrink-0 mt-1">
                        {level.completed ? (
                          <CheckCircle className="w-6 h-6 text-green-500" />
                        ) : level.current ? (
                          <div className="w-6 h-6 border-2 border-blue-500 rounded-full bg-blue-100 flex items-center justify-center">
                            <div className="w-2 h-2 bg-blue-500 rounded-full" />
                          </div>
                        ) : (
                          <Lock className="w-6 h-6 text-slate-400" />
                        )}
                      </div>

                      {/* Level Content */}
                      <div className="flex-1">
                        <div className="flex items-start justify-between mb-3">
                          <div>
                            <h3
                              className={`text-lg font-semibold ${level.completed ? "text-green-700" : level.current ? "text-blue-700" : "text-slate-500"
                                }`}
                            >
                              Level {level.id}: {level.name}
                            </h3>
                            <p className="text-slate-600 mt-1">{level.description}</p>
                          </div>
                          <div className="flex items-center space-x-2">
                            <Badge variant={level.completed ? "default" : "secondary"}>
                              {level.completed ? level.quizzes : 0}/{level.quizzes} quizzes
                            </Badge>
                            <Badge variant="outline">
                              <Clock className="w-3 h-3 mr-1" />
                              {level.estimatedTime}
                            </Badge>
                          </div>
                        </div>

                        {/* Progress Bar for Current/Incomplete Levels */}
                        {!level.completed && level.completedQuizzes > 0 && (
                          <div className="mb-3">
                            <div className="flex justify-between text-sm mb-1">
                              <span className="text-slate-600">Progress</span>
                              <span className="font-medium">
                                {level.completedQuizzes > 0 ? Math.round((level.completedQuizzes / level.quizzes) * 100) : 0}%
                              </span>
                            </div>
                            <Progress value={level.completedQuizzes > 0 ? (level.completedQuizzes / level.quizzes) * 100 : 0} className="h-2" />
                          </div>
                        )}

                        {/* Topics */}
                        <div className="mb-4">
                          <h4 className="text-sm font-medium text-slate-700 mb-2">Topics Covered:</h4>
                          <div className="flex flex-wrap gap-2">
                            {level.topics.map((topic: string, topicIndex: number) => (
                              <Badge key={topicIndex} variant="outline" className="text-xs">
                                {topic}
                              </Badge>
                            ))}
                          </div>
                        </div>

                        {/* Action Button */}
                        <div className="flex justify-end">{actionButton}</div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
