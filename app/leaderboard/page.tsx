"use client"

import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Trophy, Medal, Award, TrendingUp, Users, Target, ArrowLeft, Code, Crown, Star, BookOpen } from "lucide-react"
import Link from "next/link"
import { getLeaderboard } from "@/lib/api"

export default function LeaderboardPage() {
  const [selectedPeriod, setSelectedPeriod] = useState("all-time")
  const [leaderboard, setLeaderboard] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    setLoading(true)
    getLeaderboard(selectedPeriod)
      .then(res => setLeaderboard(res.data))
      .catch(() => setError("Leaderboard not found"))
      .finally(() => setLoading(false))
  }, [selectedPeriod])

  const getRankIcon = (rank: number) => {
    switch (rank) {
      case 1:
        return <Crown className="w-5 h-5 text-yellow-500" />
      case 2:
        return <Medal className="w-5 h-5 text-gray-400" />
      case 3:
        return <Award className="w-5 h-5 text-amber-600" />
      default:
        return <span className="text-slate-600 font-bold">#{rank}</span>
    }
  }

  const getRankBadge = (rank: number) => {
    switch (rank) {
      case 1:
        return "bg-gradient-to-r from-yellow-400 to-yellow-600 text-white"
      case 2:
        return "bg-gradient-to-r from-gray-300 to-gray-500 text-white"
      case 3:
        return "bg-gradient-to-r from-amber-400 to-amber-600 text-white"
      default:
        return "bg-slate-100 text-slate-700"
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
                <div className="w-10 h-10 bg-gradient-to-r from-yellow-500 to-orange-500 rounded-lg flex items-center justify-center">
                  <Trophy className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h1 className="text-2xl font-bold text-slate-900">Leaderboard</h1>
                  <p className="text-sm text-slate-600">See how you rank among your peers</p>
                </div>
              </div>
            </div>
            <Link href="/">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Code className="w-5 h-5 text-white" />
              </div>
            </Link>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        {/* Stats Overview */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {/* Remove subjectLeaders and achievements arrays */}
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Main Leaderboard */}
          <div className="lg:col-span-2">
            <Card className="border-0 shadow-xl bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <div>
                    <CardTitle className="flex items-center space-x-2">
                      <Trophy className="w-5 h-5 text-yellow-600" />
                      <span>Global Rankings</span>
                    </CardTitle>
                    <CardDescription>Top performers across all subjects</CardDescription>
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <Tabs value={selectedPeriod} onValueChange={setSelectedPeriod}>
                  <TabsList className="grid w-full grid-cols-3 mb-6">
                    <TabsTrigger value="all-time">All Time</TabsTrigger>
                    <TabsTrigger value="monthly">This Month</TabsTrigger>
                    <TabsTrigger value="weekly">This Week</TabsTrigger>
                  </TabsList>

                  <TabsContent value={selectedPeriod} className="space-y-4">
                    {leaderboard.map((user, index) => (
                      <div
                        key={user.rank}
                        className={`flex items-center space-x-4 p-4 rounded-lg border-2 transition-all ${user.rank <= 3
                          ? "border-yellow-200 bg-gradient-to-r from-yellow-50 to-orange-50"
                          : "border-slate-200 bg-white hover:border-slate-300"
                          }`}
                      >
                        {/* Rank */}
                        <div
                          className={`w-12 h-12 rounded-full flex items-center justify-center ${getRankBadge(user.rank)}`}
                        >
                          {getRankIcon(user.rank)}
                        </div>

                        {/* User Info */}
                        <div className="flex-1">
                          <div className="flex items-center space-x-3 mb-2">
                            <Avatar className="w-10 h-10">
                              <AvatarFallback className="bg-gradient-to-r from-blue-600 to-purple-600 text-white text-sm">
                                {user.name
                                  .split(" ")
                                  .map((n: string) => n[0])
                                  .join("")}
                              </AvatarFallback>
                            </Avatar>
                            <div>
                              <h3 className="font-semibold text-slate-900">{user.name}</h3>
                              <p className="text-sm text-slate-600">{user.email}</p>
                            </div>
                          </div>

                          <div className="flex flex-wrap gap-2">
                            {user.subjects.map((subject: string, subjectIndex: number) => (
                              <Badge key={subjectIndex} variant="secondary" className="text-xs">
                                {subject}
                              </Badge>
                            ))}
                          </div>
                        </div>

                        {/* Stats */}
                        <div className="text-right space-y-1">
                          <div className="text-2xl font-bold text-slate-900">{user.score.toLocaleString()}</div>
                          <div className="text-xs text-slate-600">Total Points</div>
                          <div className="flex items-center space-x-4 text-xs text-slate-500">
                            <span>{user.quizzes} quizzes</span>
                            <span>{user.avgScore}% avg</span>
                            <span className="flex items-center">
                              <TrendingUp className="w-3 h-3 mr-1" />
                              {user.streak}
                            </span>
                          </div>
                        </div>
                      </div>
                    ))}
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Subject Leaders */}
            {/* Remove all references to subjectLeaders */}

            {/* Your Rank */}
            <Card className="border-0 shadow-lg bg-gradient-to-r from-blue-600 to-purple-600 text-white">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Users className="w-5 h-5" />
                  <span>Your Rank</span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-center">
                  <div className="text-3xl font-bold mb-2">#23</div>
                  <p className="text-blue-100 mb-4">out of 1,247 students</p>
                  <div className="space-y-2 text-sm">
                    <div className="flex justify-between">
                      <span className="text-blue-100">Total Points:</span>
                      <span className="font-medium">1,847</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-blue-100">Quizzes Completed:</span>
                      <span className="font-medium">87</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-blue-100">Average Score:</span>
                      <span className="font-medium">82%</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-blue-100">Current Streak:</span>
                      <span className="font-medium">5 days</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Quick Actions */}
            <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle>Climb the Ranks</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <Link href="/dashboard">
                  <Button className="w-full justify-start">
                    <BookOpen className="w-4 h-4 mr-2" />
                    Take More Quizzes
                  </Button>
                </Link>
                <Button variant="outline" className="w-full justify-start bg-transparent">
                  <Target className="w-4 h-4 mr-2" />
                  Set Goals
                </Button>
                <Button variant="outline" className="w-full justify-start bg-transparent">
                  <Users className="w-4 h-4 mr-2" />
                  Challenge Friends
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}
