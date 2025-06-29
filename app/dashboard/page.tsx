"use client"

import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  BookOpen,
  Trophy,
  Clock,
  Target,
  TrendingUp,
  Play,
  Lock,
  CheckCircle,
  Star,
  ArrowRight,
  Code,
  LogOut,
} from "lucide-react"
import Link from "next/link"
import { useRouter } from "next/navigation"

export default function DashboardPage() {
  const [user, setUser] = useState<any>(null)
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem("authToken")
    const userData = localStorage.getItem("user")

    if (!token || !userData) {
      router.push("/login")
      return
    }

    setUser(JSON.parse(userData))
  }, [router])

  const handleLogout = () => {
    localStorage.removeItem("authToken")
    localStorage.removeItem("user")
    router.push("/")
  }

  const subjects = [
    {
      id: 1,
      name: "Python Programming",
      description: "Master Python fundamentals and advanced concepts",
      icon: "🐍",
      color: "bg-blue-500",
      progress: 65,
      currentLevel: 3,
      totalLevels: 5,
      completedQuizzes: 32,
      totalQuizzes: 50,
      levels: [
        { id: 1, name: "Variables & Data Types", completed: true, quizzes: 10 },
        { id: 2, name: "Control Structures", completed: true, quizzes: 12 },
        { id: 3, name: "Functions & Modules", completed: false, quizzes: 10, current: true },
        { id: 4, name: "Object-Oriented Programming", completed: false, quizzes: 8 },
        { id: 5, name: "Advanced Topics", completed: false, quizzes: 10 },
      ],
    },
    {
      id: 2,
      name: "Machine Learning",
      description: "Understand ML algorithms and theoretical foundations",
      icon: "🤖",
      color: "bg-purple-500",
      progress: 30,
      currentLevel: 2,
      totalLevels: 4,
      completedQuizzes: 12,
      totalQuizzes: 40,
      levels: [
        { id: 1, name: "ML Fundamentals", completed: true, quizzes: 10 },
        { id: 2, name: "Supervised Learning", completed: false, quizzes: 10, current: true },
        { id: 3, name: "Unsupervised Learning", completed: false, quizzes: 10 },
        { id: 4, name: "Deep Learning Basics", completed: false, quizzes: 10 },
      ],
    },
    {
      id: 3,
      name: "JavaScript",
      description: "Learn JavaScript concepts and modern ES6+ features",
      icon: "⚡",
      color: "bg-yellow-500",
      progress: 80,
      currentLevel: 4,
      totalLevels: 4,
      completedQuizzes: 36,
      totalQuizzes: 45,
      levels: [
        { id: 1, name: "JS Fundamentals", completed: true, quizzes: 12 },
        { id: 2, name: "DOM Manipulation", completed: true, quizzes: 11 },
        { id: 3, name: "Async JavaScript", completed: true, quizzes: 13 },
        { id: 4, name: "Modern ES6+", completed: false, quizzes: 9, current: true },
      ],
    },
    {
      id: 4,
      name: "C Programming",
      description: "Build strong foundations in C programming language",
      icon: "⚙️",
      color: "bg-green-500",
      progress: 20,
      currentLevel: 1,
      totalLevels: 3,
      completedQuizzes: 7,
      totalQuizzes: 35,
      levels: [
        { id: 1, name: "C Basics & Syntax", completed: false, quizzes: 12, current: true },
        { id: 2, name: "Pointers & Memory", completed: false, quizzes: 12 },
        { id: 3, name: "Advanced C", completed: false, quizzes: 11 },
      ],
    },
  ]

  const recentActivity = [
    { subject: "Python Programming", action: "Completed Quiz: Functions Basics", time: "2 hours ago", score: 85 },
    { subject: "JavaScript", action: "Started Level: Modern ES6+", time: "1 day ago", score: null },
    { subject: "Machine Learning", action: "Completed Quiz: Linear Regression", time: "2 days ago", score: 92 },
    { subject: "Python Programming", action: "Completed Quiz: Loops & Iterations", time: "3 days ago", score: 78 },
  ]

  const stats = [
    { label: "Total Quizzes Completed", value: 87, icon: BookOpen, color: "text-blue-600" },
    { label: "Average Score", value: "82%", icon: Target, color: "text-green-600" },
    { label: "Current Streak", value: "5 days", icon: TrendingUp, color: "text-purple-600" },
    { label: "Rank Position", value: "#23", icon: Trophy, color: "text-yellow-600" },
  ]

  if (!user) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">Loading...</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <Link href="/" className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Code className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                  CodeTech
                </h1>
              </div>
            </Link>
            <div className="flex items-center space-x-4">
              <Link href="/leaderboard">
                <Button variant="ghost">Leaderboard</Button>
              </Link>
              <div className="flex items-center space-x-3">
                <Avatar>
                  <AvatarFallback className="bg-gradient-to-r from-blue-600 to-purple-600 text-white">
                    {user.name
                      .split(" ")
                      .map((n: string) => n[0])
                      .join("")}
                  </AvatarFallback>
                </Avatar>
                <div className="hidden md:block">
                  <p className="font-medium text-slate-900">{user.name}</p>
                  <p className="text-sm text-slate-600">{user.email}</p>
                </div>
                <Button variant="ghost" size="sm" onClick={handleLogout}>
                  <LogOut className="w-4 h-4" />
                </Button>
              </div>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900 mb-2">Welcome back, {user.name.split(" ")[0]}! 👋</h1>
          <p className="text-slate-600">Ready to continue your learning journey?</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {stats.map((stat, index) => (
            <Card key={index} className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardContent className="p-4">
                <div className="flex items-center space-x-3">
                  <stat.icon className={`w-8 h-8 ${stat.color}`} />
                  <div>
                    <div className="text-2xl font-bold text-slate-900">{stat.value}</div>
                    <div className="text-xs text-slate-600">{stat.label}</div>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-8">
            {/* Continue Learning */}
            <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Play className="w-5 h-5 text-blue-600" />
                  <span>Continue Learning</span>
                </CardTitle>
                <CardDescription>Pick up where you left off</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid md:grid-cols-2 gap-4">
                  {subjects
                    .filter((s) => s.progress > 0 && s.progress < 100)
                    .slice(0, 2)
                    .map((subject) => (
                      <div
                        key={subject.id}
                        className="p-4 border border-slate-200 rounded-lg hover:shadow-md transition-shadow"
                      >
                        <div className="flex items-center space-x-3 mb-3">
                          <div
                            className={`w-10 h-10 ${subject.color} rounded-lg flex items-center justify-center text-xl`}
                          >
                            {subject.icon}
                          </div>
                          <div>
                            <h3 className="font-semibold text-slate-900">{subject.name}</h3>
                            <p className="text-sm text-slate-600">
                              Level {subject.currentLevel} of {subject.totalLevels}
                            </p>
                          </div>
                        </div>
                        <Progress value={subject.progress} className="mb-3" />
                        <div className="flex justify-between items-center">
                          <span className="text-sm text-slate-600">{subject.progress}% Complete</span>
                          <Link href={`/subject/${subject.id}`}>
                            <Button size="sm">Continue</Button>
                          </Link>
                        </div>
                      </div>
                    ))}
                </div>
              </CardContent>
            </Card>

            {/* All Subjects */}
            <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle>All Subjects</CardTitle>
                <CardDescription>Explore all available learning paths</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid md:grid-cols-2 gap-6">
                  {subjects.map((subject) => (
                    <div
                      key={subject.id}
                      className="border border-slate-200 rounded-lg p-4 hover:shadow-md transition-shadow"
                    >
                      <div className="flex items-center space-x-3 mb-4">
                        <div
                          className={`w-12 h-12 ${subject.color} rounded-lg flex items-center justify-center text-2xl`}
                        >
                          {subject.icon}
                        </div>
                        <div className="flex-1">
                          <h3 className="font-semibold text-slate-900">{subject.name}</h3>
                          <p className="text-sm text-slate-600">{subject.description}</p>
                        </div>
                      </div>

                      <div className="space-y-3 mb-4">
                        <div className="flex justify-between text-sm">
                          <span className="text-slate-600">Overall Progress</span>
                          <span className="font-medium">{subject.progress}%</span>
                        </div>
                        <Progress value={subject.progress} />
                        <div className="flex justify-between text-sm text-slate-600">
                          <span>
                            {subject.completedQuizzes}/{subject.totalQuizzes} Quizzes
                          </span>
                          <span>
                            Level {subject.currentLevel}/{subject.totalLevels}
                          </span>
                        </div>
                      </div>

                      {/* Level Progress */}
                      <div className="space-y-2 mb-4">
                        {subject.levels.map((level) => (
                          <div key={level.id} className="flex items-center space-x-3 text-sm">
                            {level.completed ? (
                              <CheckCircle className="w-4 h-4 text-green-500" />
                            ) : level.current ? (
                              <div className="w-4 h-4 border-2 border-blue-500 rounded-full bg-blue-100" />
                            ) : (
                              <Lock className="w-4 h-4 text-slate-400" />
                            )}
                            <span
                              className={
                                level.completed
                                  ? "text-green-700"
                                  : level.current
                                    ? "text-blue-700 font-medium"
                                    : "text-slate-500"
                              }
                            >
                              {level.name}
                            </span>
                            <Badge variant={level.completed ? "default" : "secondary"} className="ml-auto">
                              {level.quizzes} quizzes
                            </Badge>
                          </div>
                        ))}
                      </div>

                      <Link href={`/subject/${subject.id}`}>
                        <Button className="w-full">
                          {subject.progress === 0 ? "Start Learning" : "Continue"}
                          <ArrowRight className="ml-2 w-4 h-4" />
                        </Button>
                      </Link>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Recent Activity */}
            <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Clock className="w-5 h-5 text-slate-600" />
                  <span>Recent Activity</span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {recentActivity.map((activity, index) => (
                    <div key={index} className="flex items-start space-x-3">
                      <div className="w-2 h-2 bg-blue-500 rounded-full mt-2" />
                      <div className="flex-1">
                        <p className="text-sm font-medium text-slate-900">{activity.action}</p>
                        <p className="text-xs text-slate-600">{activity.subject}</p>
                        <div className="flex items-center justify-between mt-1">
                          <p className="text-xs text-slate-500">{activity.time}</p>
                          {activity.score && (
                            <Badge variant="secondary" className="text-xs">
                              {activity.score}%
                            </Badge>
                          )}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Quick Actions */}
            <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle>Quick Actions</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <Link href="/leaderboard">
                  <Button variant="outline" className="w-full justify-start bg-transparent">
                    <Trophy className="w-4 h-4 mr-2" />
                    View Leaderboard
                  </Button>
                </Link>
                <Button variant="outline" className="w-full justify-start bg-transparent">
                  <Star className="w-4 h-4 mr-2" />
                  Review Favorites
                </Button>
                <Button variant="outline" className="w-full justify-start bg-transparent">
                  <Target className="w-4 h-4 mr-2" />
                  Set Learning Goals
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}
