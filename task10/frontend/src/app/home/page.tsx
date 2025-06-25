'use client';
import { useState, useEffect, FormEvent } from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation';

interface Post {
  id: string;
  text: string;
  timestamp: string;
  owner_id: string;
  owner_username: string;
  likes: string[];
}
interface User { id: string; username: string; }

export default function HomePage() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [newText, setNewText] = useState('');
  const [user, setUser] = useState<User | null>(null);
  const router = useRouter();

  const API_URL = 'http://localhost:8000/api';

  const fetchPosts = async () => {
    const res = await axios.get(`${API_URL}/posts`);
    setPosts(res.data);
  };

  useEffect(() => {
    const stored = localStorage.getItem('user');
    if (!stored) return router.push('/login');
    setUser(JSON.parse(stored));
    fetchPosts();
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('user');
    router.push('/login');
  };

  const handleCreate = async (e: FormEvent) => {
    e.preventDefault();
    const token = localStorage.getItem('auth_token');
    await axios.post(`${API_URL}/posts`, { text: newText }, { headers: { Authorization: `Bearer ${token}` } });
    setNewText('');
    fetchPosts();
  };

  const handleDelete = async (id: string) => {
    const token = localStorage.getItem('auth_token');
    await axios.delete(`${API_URL}/posts/${id}`, { headers: { Authorization: `Bearer ${token}` } });
    fetchPosts();
  };

  const toggleLike = async (id: string, liked: boolean) => {
    const token = localStorage.getItem('auth_token');
    if (liked) await axios.delete(`${API_URL}/posts/${id}/like`, { headers: { Authorization: `Bearer ${token}` } });
    else await axios.post(`${API_URL}/posts/${id}/like`, {}, { headers: { Authorization: `Bearer ${token}` } });
    fetchPosts();
  };

  if (!user) return <p>Загрузка...</p>;

  return (
    <div className="max-w-2xl mx-auto p-4">
      <header className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Лента</h1>
        <div>
          <span>Привет, <strong>{user.username}</strong>!</span>
          <button onClick={handleLogout} className="ml-4 bg-red-500 text-white px-2 py-1 rounded">Выйти</button>
        </div>
      </header>

      <form onSubmit={handleCreate} className="mb-6">
        <textarea value={newText} onChange={(e) => setNewText(e.target.value)} placeholder="Новый пост..." className="w-full p-2 border rounded mb-2" rows={3} />
        <button type="submit" className="w-full bg-green-500 text-white p-2 rounded">Опубликовать</button>
      </form>

      {posts.map(post => {
        const liked = post.likes.includes(user.id);
        return (
          <div key={post.id} className="bg-black p-4 mb-4 rounded shadow relative">
            <p>{post.text}</p>
            <div className="text-xs text-gray-500 mt-2">
              <a href={`/users/${post.owner_username}`} className="text-blue-600 hover:underline">{post.owner_username}</a> — {new Date(post.timestamp).toLocaleString()}
            </div>
            <button
              onClick={() => toggleLike(post.id, liked)}
              className={`mt-2 text-sm ${liked ? 'text-pink-500' : 'text-gray-500'}`}>
              {liked ? '❤️ Unlike' : '🤍 Like'} ({post.likes.length})
            </button>
            {user.id === post.owner_id && (
              <button onClick={() => handleDelete(post.id)} className="absolute top-2 right-2 text-red-500 hover:text-red-700">✕</button>
            )}
          </div>
        );
      })}
    </div>
  );
}
