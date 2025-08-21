"use client";
import { useState } from "react";
import { apiRequest } from "@/lib/api";

export default function LoginPage() {
  const [form, setForm] = useState({ username: "", password: "" });
  const [msg, setMsg] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const data = await apiRequest("/api/login/", {
        method: "POST",
        body: JSON.stringify(form),
      });
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      setMsg("Logged in successfully!");
    } catch (err: any) {
      setMsg("Error: " + err.message);
    }
  };

  return (
    <div className="max-w-sm mx-auto mt-10">
      <h1 className="text-xl font-bold mb-4">Login</h1>
      <form onSubmit={handleSubmit} className="space-y-3">
        <input
          className="w-full border p-2 rounded"
          placeholder="Username"
          value={form.username}
          onChange={(e) => setForm({ ...form, username: e.target.value })}
        />
        <input
          className="w-full border p-2 rounded"
          placeholder="Password"
          type="password"
          value={form.password}
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />
        <button className="w-full bg-blue-500 text-white p-2 rounded">
          Login
        </button>
      </form>
      {msg && <p className="mt-3 text-sm">{msg}</p>}
    </div>
  );
}
