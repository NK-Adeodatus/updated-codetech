"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Trophy, Medal, Award, TrendingUp, Users, Target, ArrowLeft, Code, Crown, Star, BookOpen } from "lucide-react"
import Link from "next/link"

export default function LeaderboardPage() {
  const [selectedPeriod, setSelectedPeriod] = useState("all-time")

  const leaderboardData = {
    "all-time": [
      {
        rank: 1,
        name: "Sarah Johnson",
        email: "sarah.j@alu.edu",
        score: 2847,
        quizzes: 156,
        avgScore: 94,
        streak: 23,
        subjects: ["Python", "ML", "JavaScript"],
      },
      {
        rank: 2,
        name: "Michael Chen",
        email: "michael.c@alu.edu",
        score: 2756,
        quizzes: 142,
        avgScore: 92,
        streak: 18,
        subjects: ["Python", "C", "JavaScript"],
      },
      {
        rank: 3,
        name: "Amara Okafor",
        email: "amara.o@alu.edu",
        score: 2698,
        quizzes: 138,
        avgScore: 91,
        streak: 15,
        subjects: ["ML", "Python", "JavaScript"],
      },
      {
        rank: 4,
        name: "David Kim",
        email: "david.k@alu.edu",
        score: 2634,
        quizzes: 134,
        avgScore: 89,
        streak: 12,
        subjects: ["JavaScript", "Python", "C"],
      },
      {
        rank: 5,
        name: "Fatima Al-Rashid",
        email: "fatima.a@alu.edu",
        score: 2587,
        quizzes: 129,
        avgScore: 88,
        streak: 20,
        subjects: ["Python", "ML"],
      },
      {
        rank: 6,
        name: "James Wilson",
        email: "james.w@alu.edu",
        score: 2543,
        quizzes: 125,
        avgScore: 87,
        streak: 9,
        subjects: ["C", "Python"],
      },
      {
        rank: 7,
        name: "Priya Sharma",
        email: "priya.s@alu.edu",
        score: 2498,
        quizzes: 121,
        avgScore: 86,
        streak: 14,
        subjects: ["ML", "JavaScript"],
      },
      {
        rank: 8,
        name: "Ahmed Hassan",
        email: "ahmed.h@alu.edu",
        score: 2456,
        quizzes: 118,
        avgScore: 85,
        streak: 7,
        subjects: ["Python", "JavaScript"],
      },
      {
        rank: 9,
        name: "Lisa Anderson",
        email: "lisa.a@alu.edu",
        score: 2412,
        quizzes: 115,
        avgScore: 84,
        streak: 11,
        subjects: ["JavaScript", "C"],
      },
      {
        rank: 10,
        name: "Carlos Rodriguez",
        email: "carlos.r@alu.edu",
        score: 2378,
        quizzes: 112,
        avgScore: 83,
        streak: 6,
        subjects: ["Python", "ML"],
      },
    ],
    monthly: [
      {
        rank: 1,
        name: "Sarah Johnson",
        email: "sarah.j@alu.edu",
        score: 487,
        quizzes: 26,
        avgScore: 95,
        streak: 23,
        subjects: ["Python", "ML"],
      },
      {
        rank: 2,
        name: "Amara Okafor",
        email: "amara.o@alu.edu",
        score: 456,
        quizzes: 24,
        avgScore: 93,
        streak: 15,
        subjects: ["ML", "JavaScript"],
      },
      {
        rank: 3,
        name: "Michael Chen",
        email: "michael.c@alu.edu",
        score: 434,
        quizzes: 22,
        avgScore: 91,
        streak: 18,
        subjects: ["Python", "C"],
      },
    ],
    weekly: [
      {
        rank: 1,
        name: "Fatima Al-Rashid",
        email: "fatima.a@alu.edu",
        score: 156,
        quizzes: 8,
        avgScore: 97,
        streak: 20,
        subjects: ["Python"],
      },
      {
        rank: 2,
        name: "Sarah Johnson",
        email: "sarah.j@alu.edu",
        score: 142,
        quizzes: 7,
        avgScore: 96,
        streak: 23,
        subjects: ["ML"],
      },
      {
        rank: 3,
        name: "David Kim",
        email: "david.k@alu.edu",
        score: 128,
        quizzes: 6,
        avgScore: 89,
        streak: 12,
        subjects: ["JavaScript"],
      },
    ],
  }

  const subjectLeaders = [
    { subject: "Python Programming", leader: "Sarah Johnson", score: 1247, icon: "🐍", color: "bg-blue-500" },
    { subject: "Machine Learning", leader: "Amara Okafor", score: 1156, icon: "🤖", color: "bg-purple-500" },
    { subject: "JavaScript", leader: "Michael Chen", score: 1089, icon: "⚡", color: "bg-yellow-500" },
    { subject: "C Programming", leader: "David Kim", score: 987, icon: "⚙️", color: "bg-green-500" },
  ]

  const achievements = [
    { title: "Quiz Master", description: "Complete 100+ quizzes", icon: Trophy, count: 12 },
    { title: "Perfect Score", description: "Get 100% on any quiz", icon: Target, count: 34 },
    { title: "Streak Champion", description: "Maintain 30-day streak", icon: TrendingUp, count: 5 },
    { title: "Subject Expert", description: "Complete all levels in a subject", icon: Award, count: 8 },
  ]

  const currentData = leaderboardData[selectedPeriod as keyof typeof leaderboardData]

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
          {achievements.map((achievement, index) => (
            <Card key={index} className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardContent className="p-4 text-center">
                <achievement.icon className="w-8 h-8 mx-auto mb-2 text-blue-600" />
                <div className="text-2xl font-bold text-slate-900 mb-1">{achievement.count}</div>
                <div className="text-xs text-slate-600">{achievement.title}</div>
              </CardContent>
            </Card>
          ))}
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
                    {currentData.map((user, index) => (
                      <div
                        key={user.rank}
                        className={`flex items-center space-x-4 p-4 rounded-lg border-2 transition-all ${
                          user.rank <= 3
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
                                  .map((n) => n[0])
                                  .join("")}
                              </AvatarFallback>
                            </Avatar>
                            <div>
                              <h3 className="font-semibold text-slate-900">{user.name}</h3>
                              <p className="text-sm text-slate-600">{user.email}</p>
                            </div>
                          </div>

                          <div className="flex flex-wrap gap-2">
                            {user.subjects.map((subject, subjectIndex) => (
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
            <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Star className="w-5 h-5 text-purple-600" />
                  <span>Subject Leaders</span>
                </CardTitle>
                <CardDescription>Top performer in each subject</CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                {subjectLeaders.map((leader, index) => (
                  <div key={index} className="flex items-center space-x-3 p-3 rounded-lg bg-slate-50">
                    <div className={`w-10 h-10 ${leader.color} rounded-lg flex items-center justify-center text-xl`}>
                      {leader.icon}
                    </div>
                    <div className="flex-1">
                      <h4 className="font-medium text-slate-900 text-sm">{leader.subject}</h4>
                      <p className="text-xs text-slate-600">{leader.leader}</p>
                    </div>
                    <div className="text-right">
                      <div className="font-bold text-slate-900">{leader.score}</div>
                      <div className="text-xs text-slate-600">points</div>
                    </div>
                  </div>
                ))}
              </CardContent>
            </Card>

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
