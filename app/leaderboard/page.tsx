// =============================================================================
// LEADERBOARD PAGE COMPONENT
// =============================================================================
// This page displays user rankings and performance statistics.
// Shows top performers, user stats, and provides goal-setting features.
// Includes different time period filters and social features.

"use client"

// Import React hooks for state management and side effects
import { useState, useEffect } from "react"
// Import UI components from the design system
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
// Import icons from Lucide React
import { Trophy, Medal, Award, TrendingUp, Users, Target, ArrowLeft, Code, Crown, Star, BookOpen, Send, Plus } from "lucide-react"
// Import Next.js routing components
import Link from "next/link"
// Import API functions for leaderboard data
import { getLeaderboard, getUserStats, getTotalStudents, saveUserGoal, getUserGoals, sendChallenge, getUserChallenges } from "@/lib/api"

export default function LeaderboardPage() {
  // State management for leaderboard data
  const [selectedPeriod, setSelectedPeriod] = useState("all-time") // Selected time period filter
  const [leaderboard, setLeaderboard] = useState<any[]>([]) // Leaderboard rankings data
  const [userStats, setUserStats] = useState<any>(null) // Current user's statistics
  const [totalStudents, setTotalStudents] = useState(0) // Total number of students
  const [loading, setLoading] = useState(true) // Loading state for data fetching
  const [error, setError] = useState("") // Error message state

  // Modal states for interactive features
  const [showGoalsModal, setShowGoalsModal] = useState(false) // Toggle goal setting modal
  const [showChallengeModal, setShowChallengeModal] = useState(false) // Toggle challenge modal
  const [goalData, setGoalData] = useState({
    type: "",
    target: "",
    deadline: "",
    description: ""
  }) // Form data for goal setting
  const [challengeData, setChallengeData] = useState({
    friendEmail: "",
    message: "",
    quizType: ""
  }) // Form data for friend challenges

  const [goals, setGoals] = useState<any[]>([])
  const [challenges, setChallenges] = useState<any[]>([])

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true)
      try {
        // Get leaderboard data
        const leaderboardRes = await getLeaderboard(selectedPeriod)
        setLeaderboard(leaderboardRes.data)

        // Get user stats (if user is logged in)
        const token = localStorage.getItem("authToken")
        if (token) {
          try {
            const statsRes = await getUserStats(token)
            setUserStats(statsRes)
            // Fetch user goals
            const goalsRes = await getUserGoals(token)
            setGoals(goalsRes)
            // Fetch received challenges
            const challengesRes = await getUserChallenges(token)
            setChallenges(challengesRes)
          } catch (err) {
            console.log("User not logged in or stats not available")
          }
        }

        // Get total students count
        const totalRes = await getTotalStudents()
        setTotalStudents(totalRes.totalStudents)
      } catch (err) {
        setError("Failed to load leaderboard data")
      } finally {
        setLoading(false)
      }
    }

    fetchData()
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

  const handleSetGoal = async () => {
    if (!goalData.type || !goalData.target || !goalData.deadline) {
      alert("Please fill in all required fields")
      return
    }
    try {
      const token = localStorage.getItem("authToken")
      if (!token) throw new Error("Not authenticated")
      await saveUserGoal(goalData, token)
      // Refetch goals
      const goalsRes = await getUserGoals(token)
      setGoals(goalsRes)
      alert("Goal set successfully!")
      setShowGoalsModal(false)
      setGoalData({ type: "", target: "", deadline: "", description: "" })
    } catch (err: any) {
      alert(err.message || "Failed to save goal")
    }
  }

  const handleChallengeFriend = async () => {
    if (!challengeData.friendEmail || !challengeData.quizType) {
      alert("Please fill in all required fields")
      return
    }
    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(challengeData.friendEmail)) {
      alert("Please enter a valid email address")
      return
    }
    try {
      const token = localStorage.getItem("authToken")
      if (!token) throw new Error("Not authenticated")
      await sendChallenge(challengeData, token)
      alert(`Challenge sent to ${challengeData.friendEmail}!`)
      setShowChallengeModal(false)
      setChallengeData({ friendEmail: "", message: "", quizType: "" })
    } catch (err: any) {
      alert(err.message || "Failed to send challenge")
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
                    {loading ? (
                      <div className="text-center py-8">
                        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
                        <p className="text-slate-600 mt-2">Loading leaderboard...</p>
                      </div>
                    ) : error ? (
                      <div className="text-center py-8">
                        <p className="text-red-600">{error}</p>
                      </div>
                    ) : (
                      leaderboard.map((user, index) => (
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
                      ))
                    )}
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
                  {loading ? (
                    <div className="text-slate-200 animate-pulse h-32 flex flex-col items-center justify-center">
                      <div className="w-16 h-8 bg-slate-200 rounded mb-2" />
                      <div className="w-32 h-4 bg-slate-200 rounded mb-2" />
                      <div className="w-40 h-4 bg-slate-200 rounded mb-1" />
                      <div className="w-40 h-4 bg-slate-200 rounded mb-1" />
                      <div className="w-40 h-4 bg-slate-200 rounded mb-1" />
                      <div className="w-40 h-4 bg-slate-200 rounded mb-1" />
                    </div>
                  ) : userStats ? (
                    <>
                      <div className="text-3xl font-bold mb-2">#{userStats.rank}</div>
                      <p className="text-blue-100 mb-4">out of {totalStudents.toLocaleString()} students</p>
                      <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                          <span className="text-blue-100">Total Points:</span>
                          <span className="font-medium">{userStats.totalPoints?.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-blue-100">Quizzes Completed:</span>
                          <span className="font-medium">{userStats.totalCompleted}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-blue-100">Average Score:</span>
                          <span className="font-medium">{userStats.avgScore}%</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-blue-100">Current Streak:</span>
                          <span className="font-medium">{userStats.streak} days</span>
                        </div>
                      </div>
                    </>
                  ) : (
                    <>
                      <div className="text-3xl font-bold mb-2">#-</div>
                      <p className="text-blue-100 mb-4">out of {totalStudents.toLocaleString()} students</p>
                      <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                          <span className="text-blue-100">Total Points:</span>
                          <span className="font-medium">-</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-blue-100">Quizzes Completed:</span>
                          <span className="font-medium">-</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-blue-100">Average Score:</span>
                          <span className="font-medium">-</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-blue-100">Current Streak:</span>
                          <span className="font-medium">-</span>
                        </div>
                      </div>
                    </>
                  )}
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

                {/* Set Goals Modal */}
                <Dialog open={showGoalsModal} onOpenChange={setShowGoalsModal}>
                  <DialogTrigger asChild>
                    <Button variant="outline" className="w-full justify-start bg-transparent">
                      <Target className="w-4 h-4 mr-2" />
                      Set Goals
                    </Button>
                  </DialogTrigger>
                  <DialogContent className="sm:max-w-[425px]">
                    <DialogHeader>
                      <DialogTitle>Set Your Learning Goals</DialogTitle>
                      <DialogDescription>
                        Set specific goals to track your progress and stay motivated.
                      </DialogDescription>
                    </DialogHeader>
                    <div className="grid gap-4 py-4">
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="goal-type" className="text-right">
                          Goal Type
                        </Label>
                        <Select value={goalData.type} onValueChange={(value) => setGoalData({ ...goalData, type: value })}>
                          <SelectTrigger className="col-span-3">
                            <SelectValue placeholder="Select goal type" />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="complete">Complete Quizzes</SelectItem>
                            <SelectItem value="score">Achieve Score</SelectItem>
                            <SelectItem value="streak">Maintain Streak</SelectItem>
                            <SelectItem value="rank">Reach Rank</SelectItem>
                          </SelectContent>
                        </Select>
                      </div>
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="target" className="text-right">
                          Target
                        </Label>
                        <Input
                          id="target"
                          value={goalData.target}
                          onChange={(e) => setGoalData({ ...goalData, target: e.target.value })}
                          placeholder="e.g., 50 quizzes, 90% score"
                          className="col-span-3"
                        />
                      </div>
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="deadline" className="text-right">
                          Deadline
                        </Label>
                        <Input
                          id="deadline"
                          type="date"
                          value={goalData.deadline}
                          onChange={(e) => setGoalData({ ...goalData, deadline: e.target.value })}
                          className="col-span-3"
                        />
                      </div>
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="description" className="text-right">
                          Description
                        </Label>
                        <Textarea
                          id="description"
                          value={goalData.description}
                          onChange={(e) => setGoalData({ ...goalData, description: e.target.value })}
                          placeholder="Why is this goal important to you?"
                          className="col-span-3"
                        />
                      </div>
                    </div>
                    <DialogFooter>
                      <Button variant="outline" onClick={() => setShowGoalsModal(false)}>
                        Cancel
                      </Button>
                      <Button onClick={handleSetGoal}>
                        <Plus className="w-4 h-4 mr-2" />
                        Set Goal
                      </Button>
                    </DialogFooter>
                  </DialogContent>
                </Dialog>

                {/* Challenge Friends Modal */}
                <Dialog open={showChallengeModal} onOpenChange={setShowChallengeModal}>
                  <DialogTrigger asChild>
                    <Button variant="outline" className="w-full justify-start bg-transparent">
                      <Users className="w-4 h-4 mr-2" />
                      Challenge Friends
                    </Button>
                  </DialogTrigger>
                  <DialogContent className="sm:max-w-[425px]">
                    <DialogHeader>
                      <DialogTitle>Challenge a Friend</DialogTitle>
                      <DialogDescription>
                        Send a friendly challenge to compete with your friends on the leaderboard.
                      </DialogDescription>
                    </DialogHeader>
                    <div className="grid gap-4 py-4">
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="friend-email" className="text-right">
                          Friend's Email
                        </Label>
                        <Input
                          id="friend-email"
                          type="email"
                          value={challengeData.friendEmail}
                          onChange={(e) => setChallengeData({ ...challengeData, friendEmail: e.target.value })}
                          placeholder="friend@example.com"
                          className="col-span-3"
                        />
                      </div>
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="quiz-type" className="text-right">
                          Quiz Type
                        </Label>
                        <Select value={challengeData.quizType} onValueChange={(value) => setChallengeData({ ...challengeData, quizType: value })}>
                          <SelectTrigger className="col-span-3">
                            <SelectValue placeholder="Select quiz type" />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="python">Python Programming</SelectItem>
                            <SelectItem value="javascript">JavaScript</SelectItem>
                            <SelectItem value="machine-learning">Machine Learning</SelectItem>
                            <SelectItem value="any">Any Subject</SelectItem>
                          </SelectContent>
                        </Select>
                      </div>
                      <div className="grid grid-cols-4 items-center gap-4">
                        <Label htmlFor="message" className="text-right">
                          Message
                        </Label>
                        <Textarea
                          id="message"
                          value={challengeData.message}
                          onChange={(e) => setChallengeData({ ...challengeData, message: e.target.value })}
                          placeholder="Add a personal message to your challenge..."
                          className="col-span-3"
                        />
                      </div>
                    </div>
                    <DialogFooter>
                      <Button variant="outline" onClick={() => setShowChallengeModal(false)}>
                        Cancel
                      </Button>
                      <Button onClick={handleChallengeFriend}>
                        <Send className="w-4 h-4 mr-2" />
                        Send Challenge
                      </Button>
                    </DialogFooter>
                  </DialogContent>
                </Dialog>
              </CardContent>
            </Card>

            {/* Display saved goals */}
            {goals.length > 0 && (
              <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle>Your Goals</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2">
                    {goals.map((goal) => (
                      <li key={goal.id} className="p-2 rounded bg-blue-50">
                        <div className="font-medium">{goal.type} {goal.target} by {goal.deadline}</div>
                        <div className="text-xs text-slate-600">{goal.description}</div>
                        <div className="text-xs text-slate-400">Set on {goal.created_at?.slice(0, 10)}</div>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            )}

            {/* Display received challenges */}
            {challenges.length > 0 && (
              <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle>Challenges Received</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2">
                    {challenges.map((challenge) => (
                      <li key={challenge.id} className="p-2 rounded bg-purple-50">
                        <div className="font-medium">From: {challenge.sender_id} | Quiz: {challenge.quiz_type}</div>
                        <div className="text-xs text-slate-600">{challenge.message}</div>
                        <div className="text-xs text-slate-400">Received: {challenge.created_at?.slice(0, 10)}</div>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
