"use client"
import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { getSubjects, getAllUsers, getUserProgress, addSubject, addLevel } from "@/lib/api"
import { useRouter } from "next/navigation"
import { getMe } from "@/lib/api"

export default function AdminPage() {
    const [subjects, setSubjects] = useState<any[]>([])
    const [subjectName, setSubjectName] = useState("")
    const [subjectDesc, setSubjectDesc] = useState("")
    const [addSubjectMsg, setAddSubjectMsg] = useState("")
    const [levelSubjectId, setLevelSubjectId] = useState("")
    const [levelName, setLevelName] = useState("")
    const [levelDesc, setLevelDesc] = useState("")
    const [addLevelMsg, setAddLevelMsg] = useState("")
    const [users, setUsers] = useState<any[]>([])
    const [selectedUser, setSelectedUser] = useState<any>(null)
    const [userProgress, setUserProgress] = useState<any>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")
    const router = useRouter()

    useEffect(() => {
        const token = localStorage.getItem("authToken")
        if (!token) {
            router.push("/login")
            return
        }

        // Check if user is admin
        getMe(token)
            .then((user) => {
                if (user.role !== "admin") {
                    setError("Access denied. Admin privileges required.")
                    return
                }
                loadAdminData(token)
            })
            .catch(() => {
                localStorage.removeItem("authToken")
                router.push("/login")
            })
    }, [router])

    const loadAdminData = async (token: string) => {
        try {
            const [subjectsData, usersData] = await Promise.all([
                getSubjects(),
                getAllUsers(token)
            ])
            setSubjects(subjectsData)
            setUsers(usersData)
        } catch (err: any) {
            setError(err.message || "Failed to load admin data")
        } finally {
            setLoading(false)
        }
    }

    const handleAddSubject = async (e: any) => {
        e.preventDefault()
        setAddSubjectMsg("")
        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            await addSubject({
                name: subjectName,
                description: subjectDesc,
                icon: "📚",
                color: "bg-gray-500",
                levels: [],
                totalQuizzes: 0,
            }, token)
            setAddSubjectMsg("Subject added!")
            setSubjectName("")
            setSubjectDesc("")
            // Reload subjects
            const subjectsData = await getSubjects()
            setSubjects(subjectsData)
        } catch (err: any) {
            setAddSubjectMsg(err.message || "Failed to add subject.")
        }
    }

    const handleAddLevel = async (e: any) => {
        e.preventDefault()
        setAddLevelMsg("")
        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            await addLevel({
                subject_id: Number(levelSubjectId),
                level: {
                    name: levelName,
                    description: levelDesc,
                    quizzes: 0,
                    completedQuizzes: 0,
                    estimatedTime: "1 hour",
                    topics: [],
                },
            }, token)
            setAddLevelMsg("Level added!")
            setLevelName("")
            setLevelDesc("")
            // Reload subjects
            const subjectsData = await getSubjects()
            setSubjects(subjectsData)
        } catch (err: any) {
            setAddLevelMsg(err.message || "Failed to add level.")
        }
    }

    const handleViewUserProgress = async (user: any) => {
        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            const progress = await getUserProgress(user.id, token)
            setSelectedUser(user)
            setUserProgress(progress)
        } catch (err: any) {
            console.error("Failed to load user progress:", err)
        }
    }

    if (loading) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
                <div className="text-center">Loading admin panel...</div>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
                <div className="text-center text-red-600">{error}</div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
            <div className="container mx-auto py-12 px-4">
                <h1 className="text-3xl font-bold mb-8">Admin Dashboard</h1>

                <div className="grid md:grid-cols-2 gap-8 mb-12">
                    <Card>
                        <CardHeader>
                            <CardTitle>Add New Subject</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleAddSubject} className="space-y-4">
                                <Input
                                    placeholder="Subject Name"
                                    value={subjectName}
                                    onChange={e => setSubjectName(e.target.value)}
                                    required
                                />
                                <Input
                                    placeholder="Description"
                                    value={subjectDesc}
                                    onChange={e => setSubjectDesc(e.target.value)}
                                    required
                                />
                                <Button type="submit">Add Subject</Button>
                                {addSubjectMsg && <div className="text-sm mt-2">{addSubjectMsg}</div>}
                            </form>
                        </CardContent>
                    </Card>
                    <Card>
                        <CardHeader>
                            <CardTitle>Add Level to Subject</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleAddLevel} className="space-y-4">
                                <select
                                    className="w-full border rounded p-2"
                                    value={levelSubjectId}
                                    onChange={e => setLevelSubjectId(e.target.value)}
                                    required
                                >
                                    <option value="">Select Subject</option>
                                    {subjects.map((s) => (
                                        <option key={s.id} value={s.id}>{s.name}</option>
                                    ))}
                                </select>
                                <Input
                                    placeholder="Level Name"
                                    value={levelName}
                                    onChange={e => setLevelName(e.target.value)}
                                    required
                                />
                                <Input
                                    placeholder="Level Description"
                                    value={levelDesc}
                                    onChange={e => setLevelDesc(e.target.value)}
                                    required
                                />
                                <Button type="submit">Add Level</Button>
                                {addLevelMsg && <div className="text-sm mt-2">{addLevelMsg}</div>}
                            </form>
                        </CardContent>
                    </Card>
                </div>

                {/* Users Table */}
                <div className="mt-12">
                    <h2 className="text-2xl font-bold mb-4">Registered Users</h2>
                    <div className="overflow-x-auto">
                        <table className="min-w-full bg-white border border-slate-200 rounded-lg">
                            <thead>
                                <tr>
                                    <th className="px-4 py-2 border-b">ID</th>
                                    <th className="px-4 py-2 border-b">Email</th>
                                    <th className="px-4 py-2 border-b">Name</th>
                                    <th className="px-4 py-2 border-b">Role</th>
                                    <th className="px-4 py-2 border-b">Completed Quizzes</th>
                                    <th className="px-4 py-2 border-b">Avg Score</th>
                                    <th className="px-4 py-2 border-b">Last Activity</th>
                                    <th className="px-4 py-2 border-b">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {users.map((user: any) => (
                                    <tr key={user.id}>
                                        <td className="px-4 py-2 border-b text-center">{user.id}</td>
                                        <td className="px-4 py-2 border-b">{user.email}</td>
                                        <td className="px-4 py-2 border-b">{user.name || "N/A"}</td>
                                        <td className="px-4 py-2 border-b">
                                            <Badge variant={user.role === "admin" ? "destructive" : "secondary"}>
                                                {user.role}
                                            </Badge>
                                        </td>
                                        <td className="px-4 py-2 border-b text-center">{user.total_completed}</td>
                                        <td className="px-4 py-2 border-b text-center">{user.avg_score.toFixed(1)}%</td>
                                        <td className="px-4 py-2 border-b text-sm">
                                            {user.last_activity ? new Date(user.last_activity).toLocaleDateString() : "Never"}
                                        </td>
                                        <td className="px-4 py-2 border-b">
                                            <Button
                                                size="sm"
                                                onClick={() => handleViewUserProgress(user)}
                                            >
                                                View Progress
                                            </Button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                        {users.length === 0 && <div className="text-slate-500 mt-4">No users found.</div>}
                    </div>
                </div>

                {/* User Progress Modal */}
                {selectedUser && userProgress && (
                    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
                        <div className="bg-white rounded-lg p-6 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
                            <div className="flex justify-between items-center mb-4">
                                <h3 className="text-xl font-bold">
                                    Progress for {selectedUser.email}
                                </h3>
                                <Button onClick={() => setSelectedUser(null)}>Close</Button>
                            </div>

                            <div className="grid md:grid-cols-2 gap-6">
                                <div>
                                    <h4 className="font-semibold mb-3">Subject Progress</h4>
                                    {userProgress.subjects.map((subject: any) => (
                                        <div key={subject.id} className="mb-4 p-3 border rounded">
                                            <div className="flex justify-between items-center mb-2">
                                                <span className="font-medium">{subject.name}</span>
                                                <span className="text-sm text-slate-600">
                                                    {subject.completed}/{subject.total} quizzes
                                                </span>
                                            </div>
                                            <Progress value={subject.percentage} className="mb-2" />
                                            <div className="text-sm text-slate-600">
                                                {subject.percentage}% complete
                                            </div>
                                        </div>
                                    ))}
                                </div>

                                <div>
                                    <h4 className="font-semibold mb-3">Recent Activity</h4>
                                    <div className="space-y-2">
                                        {userProgress.recent_activities.map((activity: any, index: number) => (
                                            <div key={index} className="p-2 border rounded text-sm">
                                                <div className="font-medium">{activity.action}</div>
                                                <div className="text-slate-600">
                                                    {new Date(activity.timestamp).toLocaleString()}
                                                </div>
                                                {activity.score && (
                                                    <div className="text-green-600">
                                                        Score: {activity.score}%
                                                    </div>
                                                )}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    )
} 