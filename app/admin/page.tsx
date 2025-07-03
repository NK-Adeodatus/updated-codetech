"use client"
import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { getSubjects } from "@/lib/api"

export default function AdminPage() {
    const [subjects, setSubjects] = useState<any[]>([])
    const [subjectName, setSubjectName] = useState("")
    const [subjectDesc, setSubjectDesc] = useState("")
    const [addSubjectMsg, setAddSubjectMsg] = useState("")
    const [levelSubjectId, setLevelSubjectId] = useState("")
    const [levelName, setLevelName] = useState("")
    const [levelDesc, setLevelDesc] = useState("")
    const [addLevelMsg, setAddLevelMsg] = useState("")

    useEffect(() => {
        getSubjects().then(setSubjects)
    }, [addSubjectMsg, addLevelMsg])

    const handleAddSubject = async (e: any) => {
        e.preventDefault()
        setAddSubjectMsg("")
        const res = await fetch("/admin/add-subject", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: subjectName,
                description: subjectDesc,
                icon: "📚",
                color: "bg-gray-500",
                levels: [],
                totalQuizzes: 0,
            }),
        })
        if (res.ok) {
            setAddSubjectMsg("Subject added!")
            setSubjectName("")
            setSubjectDesc("")
        } else {
            setAddSubjectMsg("Failed to add subject.")
        }
    }

    const handleAddLevel = async (e: any) => {
        e.preventDefault()
        setAddLevelMsg("")
        const res = await fetch("/admin/add-level", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                subject_id: Number(levelSubjectId),
                level: {
                    name: levelName,
                    description: levelDesc,
                    quizzes: 0,
                    completedQuizzes: 0,
                    estimatedTime: "1 hour",
                    topics: [],
                },
            }),
        })
        if (res.ok) {
            setAddLevelMsg("Level added!")
            setLevelName("")
            setLevelDesc("")
        } else {
            setAddLevelMsg("Failed to add level.")
        }
    }

    return (
        <div className="container mx-auto py-12">
            <h1 className="text-3xl font-bold mb-8">Admin Tools</h1>
            <div className="grid md:grid-cols-2 gap-8">
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
        </div>
    )
} 