// =============================================================================
// HOMEPAGE COMPONENT - MAIN LANDING PAGE
// =============================================================================
// This is the main landing page that users see when they visit the application.
// It displays different content for logged-in users vs guests.

"use client"

// Import React hooks for state management and side effects
import { useState, useEffect } from "react"
// Import UI components from the design system
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
// Import icons from Lucide React
import { BookOpen, Trophy, Users, TrendingUp, ArrowRight, Star, Code, Brain, Zap } from "lucide-react"
// Import Next.js routing component
import Link from "next/link"
// Import API function to get user's subjects
import { getUserSubjects } from "@/lib/api"

export default function HomePage() {
  // State management for user authentication status
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  // State for storing user's subjects and progress data
  const [subjects, setSubjects] = useState<any[]>([])
  // Loading state for API calls
  const [loading, setLoading] = useState(true)

  // Effect hook that runs on component mount to check authentication and load data
  useEffect(() => {
    // Check if user is logged in by looking for auth token in localStorage
    const token = localStorage.getItem("authToken")
    setIsLoggedIn(!!token)

    if (token) {
      // If logged in, fetch user's subjects with progress from API
      getUserSubjects(token)
        .then((userSubjects) => setSubjects(userSubjects))
        .catch(() => setSubjects([]))
        .finally(() => setLoading(false))
    } else {
      // If not logged in (guest), show all subjects with 0% progress for preview
      setSubjects([
        {
          id: 1,
          name: "Python Programming",
          description: "Master Python fundamentals and advanced concepts",
          levels: 5,
          totalQuizzes: 50,
          icon: "🐍",
          color: "bg-blue-500",
          progress: 0,
        },
        {
          id: 2,
          name: "Machine Learning",
          description: "Understand ML algorithms and theoretical foundations",
          levels: 4,
          totalQuizzes: 40,
          icon: "🤖",
          color: "bg-purple-500",
          progress: 0,
        },
        {
          id: 3,
          name: "JavaScript",
          description: "Learn JavaScript concepts and modern ES6+ features",
          levels: 4,
          totalQuizzes: 45,
          icon: "⚡",
          color: "bg-yellow-500",
          progress: 0,
        },
        {
          id: 4,
          name: "C Programming",
          description: "Build strong foundations in C programming language",
          levels: 3,
          totalQuizzes: 35,
          icon: "⚙️",
          color: "bg-green-500",
          progress: 0,
        },
      ])
      setLoading(false)
    }
  }, [])

  // Static statistics data for the homepage stats section
  const stats = [
    { label: "Active Students", value: "1,247", icon: Users, color: "text-blue-600" },
    { label: "Quizzes Completed", value: "15,432", icon: BookOpen, color: "text-green-600" },
    { label: "Average Score", value: "78%", icon: TrendingUp, color: "text-purple-600" },
    { label: "Top Performers", value: "156", icon: Trophy, color: "text-yellow-600" },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Code className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                  CodeTech
                </h1>
                <p className="text-sm text-slate-600">Interactive Learning Platform</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              {isLoggedIn ? (
                <>
                  <Link href="/dashboard">
                    <Button variant="ghost">Dashboard</Button>
                  </Link>
                  <Link href="/leaderboard">
                    <Button variant="ghost">Leaderboard</Button>
                  </Link>
                  <Link href="/profile">
                    <Button>Profile</Button>
                  </Link>
                </>
              ) : (
                <>
                  <Link href="/login">
                    <Button variant="ghost">Login</Button>
                  </Link>
                  <Link href="/signup">
                    <Button>Sign Up</Button>
                  </Link>
                </>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 px-4">
        <div className="container mx-auto text-center">
          <div className="max-w-4xl mx-auto">
            <Badge className="mb-6 bg-blue-100 text-blue-700 hover:bg-blue-200">
              <Star className="w-4 h-4 mr-2" />
              Enhance Your Theoretical Knowledge
            </Badge>
            <h1 className="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-slate-900 via-blue-800 to-purple-800 bg-clip-text text-transparent">
              Master Technical Concepts Through
              <span className="block text-blue-600">Interactive Quizzes</span>
            </h1>
            <p className="text-xl text-slate-600 mb-8 leading-relaxed">
              Bridge the gap between theory and practice with our comprehensive quiz platform. Build strong theoretical
              foundations in Python, Machine Learning, JavaScript, and more.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              {isLoggedIn ? (
                <Link href="/dashboard">
                  <Button
                    size="lg"
                    className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
                  >
                    Continue Learning
                    <ArrowRight className="ml-2 w-5 h-5" />
                  </Button>
                </Link>
              ) : (
                <Link href="/signup">
                  <Button
                    size="lg"
                    className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
                  >
                    Start Learning Today
                    <ArrowRight className="ml-2 w-5 h-5" />
                  </Button>
                </Link>
              )}
              <Link href="/about">
                <Button size="lg" variant="outline">
                  Learn More
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 px-4 bg-white/50">
        <div className="container mx-auto">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {stats.map((stat, index) => (
              <Card key={index} className="text-center border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                <CardContent className="pt-6">
                  <stat.icon className={`w-8 h-8 mx-auto mb-3 ${stat.color}`} />
                  <div className="text-2xl font-bold text-slate-900 mb-1">{stat.value}</div>
                  <div className="text-sm text-slate-600">{stat.label}</div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Subjects Preview */}
      <section className="py-20 px-4">
        <div className="container mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4 text-slate-900">Available Subjects</h2>
            <p className="text-xl text-slate-600 max-w-2xl mx-auto">
              Choose from our comprehensive collection of technical subjects, each with structured learning paths
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {subjects.map((subject) => (
              <Card
                key={subject.id}
                className="group hover:shadow-xl transition-all duration-300 border-0 bg-white/80 backdrop-blur-sm"
              >
                <CardHeader className="pb-4">
                  <div
                    className={`w-12 h-12 ${subject.color} rounded-lg flex items-center justify-center text-2xl mb-3 group-hover:scale-110 transition-transform`}
                  >
                    {subject.icon}
                  </div>
                  <CardTitle className="text-lg">{subject.name}</CardTitle>
                  <CardDescription className="text-sm">{subject.description}</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div className="flex justify-between text-sm">
                      <span className="text-slate-600">Progress</span>
                      <span className="font-medium">{subject.progress}%</span>
                    </div>
                    <Progress value={subject.progress} className="h-2" />
                    <div className="flex justify-between text-sm text-slate-600">
                      <span>{Array.isArray(subject.levels) ? subject.levels.length : subject.levels} Levels</span>
                      <span>{subject.totalQuizzes} Quizzes</span>
                    </div>
                  </div>
                  <Link href={isLoggedIn ? `/subject/${subject.id}` : "/login"}>
                    <Button className="w-full mt-4 group-hover:bg-slate-900 transition-colors">
                      {isLoggedIn ? "Continue" : "Start Learning"}
                      <ArrowRight className="ml-2 w-4 h-4" />
                    </Button>
                  </Link>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="container mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4">Why Choose CodeTech?</h2>
            <p className="text-xl opacity-90 max-w-2xl mx-auto">
              Our platform is designed to enhance your theoretical understanding through interactive learning
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <Brain className="w-12 h-12 mx-auto mb-4 opacity-90" />
              <h3 className="text-xl font-semibold mb-3">Structured Learning</h3>
              <p className="opacity-80">
                Progress through carefully designed levels that build upon each other for comprehensive understanding
              </p>
            </div>
            <div className="text-center">
              <Zap className="w-12 h-12 mx-auto mb-4 opacity-90" />
              <h3 className="text-xl font-semibold mb-3">Instant Feedback</h3>
              <p className="opacity-80">
                Get immediate results with detailed explanations and additional resources for failed questions
              </p>
            </div>
            <div className="text-center">
              <Trophy className="w-12 h-12 mx-auto mb-4 opacity-90" />
              <h3 className="text-xl font-semibold mb-3">Competitive Learning</h3>
              <p className="opacity-80">Track your progress on leaderboards and compete with peers to stay motivated</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-white py-12 px-4">
        <div className="container mx-auto">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-3 mb-4">
                <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                  <Code className="w-5 h-5 text-white" />
                </div>
                <h3 className="text-xl font-bold">CodeTech</h3>
              </div>
              <p className="text-slate-400">
                Enhancing theoretical knowledge acquisition for technical students at ALU.
              </p>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Subjects</h4>
              <ul className="space-y-2 text-slate-400">
                <li>Python Programming</li>
                <li>Machine Learning</li>
                <li>JavaScript</li>
                <li>C Programming</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Features</h4>
              <ul className="space-y-2 text-slate-400">
                <li>Interactive Quizzes</li>
                <li>Progress Tracking</li>
                <li>Leaderboards</li>
                <li>Additional Resources</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Team</h4>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li>Gaddiel Irakoze - Product Owner</li>
                <li>Adeodatus Nkundimana - Developer</li>
                <li>Mohammed Ahmed Khalid - DevOps</li>
                <li>Iradukunda Ibrahim - Scrum Master</li>
                <li>Elvin Cyubahiro - QA Tester</li>
                <li>Effiong Uyo - UX Designer</li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-800 mt-8 pt-8 text-center text-slate-400">
            <p>&copy; 2024 CodeTech. Built by ALU Software Engineering Students.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
