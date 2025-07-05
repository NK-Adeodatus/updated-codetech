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
import { getMe, getDashboardData, getUserSubjects, getUserActivity, getUserStats } from "@/lib/api"

const iconMap: Record<string, React.ElementType> = {
  BookOpen,
  Target,
  TrendingUp,
  Trophy,
}

export default function DashboardPage() {
  const [user, setUser] = useState<any>(null)
  const router = useRouter()
  const [subjects, setSubjects] = useState<any[]>([])
  const [stats, setStats] = useState<any[]>([])
  const [recentActivity, setRecentActivity] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")
  const [userStats, setUserStats] = useState<any>({ totalCompleted: 0, avgScore: 0, streak: 0, rank: '-' })

  useEffect(() => {
    const token = localStorage.getItem("authToken")
    if (!token) {
      router.push("/login")
      return
    }
    Promise.all([
      getDashboardData(),
      getUserSubjects(token),
      getUserActivity(token),
      getUserStats(token),
    ])
      .then(([dashboard, userSubjects, activity, stats]) => {
        setStats(dashboard.stats)
        setRecentActivity(activity)
        setSubjects(userSubjects)
        setUserStats(stats)
      })
      .catch(() => setError("Failed to load dashboard data"))
      .finally(() => setLoading(false))
  }, [router])

  useEffect(() => {
    const token = localStorage.getItem("authToken")
    if (!token) {
      router.push("/login")
      return
    }
    getMe(token)
      .then(setUser)
      .catch(() => {
        localStorage.removeItem("authToken")
        router.push("/login")
      })
  }, [router])

  const handleLogout = () => {
    localStorage.removeItem("authToken")
    router.push("/")
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">Loading...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">{error}</div>
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
              {user?.role === "admin" && (
                <Link href="/admin">
                  <Button variant="ghost">Admin Panel</Button>
                </Link>
              )}
              <div className="flex items-center space-x-3">
                <Avatar>
                  <AvatarFallback className="bg-gradient-to-r from-blue-600 to-purple-600 text-white">
                    {user?.name
                      ? user.name.split(" ").map((n: string) => n[0]).join("")
                      : ""}
                  </AvatarFallback>
                </Avatar>
                <div className="hidden md:block">
                  <p className="font-medium text-slate-900">{user?.name || ""}</p>
                  <p className="text-sm text-slate-600">{user?.email || ""}</p>
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
          <h1 className="text-3xl font-bold text-slate-900 mb-2">Welcome back, {user?.name ? user.name.split(" ")[0] : ""}! 👋</h1>
          <p className="text-slate-600">Ready to continue your learning journey?</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-4">
              <div className="flex items-center space-x-3">
                <BookOpen className="w-8 h-8 text-blue-600" />
                <div>
                  <div className="text-2xl font-bold text-slate-900">{userStats.totalCompleted}</div>
                  <div className="text-xs text-slate-600">Total Quizzes Completed</div>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-4">
              <div className="flex items-center space-x-3">
                <TrendingUp className="w-8 h-8 text-green-600" />
                <div>
                  <div className="text-2xl font-bold text-slate-900">{userStats.avgScore}%</div>
                  <div className="text-xs text-slate-600">Average Score</div>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-4">
              <div className="flex items-center space-x-3">
                <Clock className="w-8 h-8 text-purple-600" />
                <div>
                  <div className="text-2xl font-bold text-slate-900">{userStats.streak} days</div>
                  <div className="text-xs text-slate-600">Current Streak</div>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
            <CardContent className="p-4">
              <div className="flex items-center space-x-3">
                <Trophy className="w-8 h-8 text-yellow-500" />
                <div>
                  <div className="text-2xl font-bold text-slate-900">#{userStats.rank}</div>
                  <div className="text-xs text-slate-600">Rank Position</div>
                </div>
              </div>
            </CardContent>
          </Card>
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
                        {subject.levels.map((level: any) => (
                          <div key={level.id} className="flex items-center space-x-3 text-sm">
                            {level.completed ? (
                              <CheckCircle className="w-4 h-4 text-green-500" />
                            ) : level.unlocked ? (
                              <div className="w-4 h-4 border-2 border-blue-500 rounded-full bg-blue-100" />
                            ) : (
                              <Lock className="w-4 h-4 text-slate-400" />
                            )}
                            <span
                              className={
                                level.completed
                                  ? "text-green-700"
                                  : level.unlocked
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

                      {/* Start/Continue/Review Button */}
                      {(() => {
                        const firstUnlocked = subject.levels.find((level: any) => level.unlocked && !level.completed);
                        if (firstUnlocked) {
                          return (
                            <Link href={`/quiz/${subject.id}/${firstUnlocked.id}`}>
                              <Button className="w-full">
                                {subject.progress === 0 ? "Start Learning" : "Continue"}
                                <ArrowRight className="ml-2 w-4 h-4" />
                              </Button>
                            </Link>
                          );
                        } else {
                          // All levels completed
                          return (
                            <Button className="w-full" variant="outline" disabled>
                              <CheckCircle className="w-4 h-4 mr-2" />
                              All Complete
                            </Button>
                          );
                        }
                      })()}
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
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}
