'use client';

import { useState, useEffect, ChangeEvent } from 'react';
import axios from 'axios';

interface Product {
  id: number;
  name: string;
  category: string;
  price: number;
}

const API_URL = 'http://localhost:8000/api';

export default function Home() {
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<string[]>([]);

  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await axios.get(`${API_URL}/categories`);
        setCategories(['All', ...response.data]);
      } catch (error) {
        console.error('Ошибка загрузки категорий:', error);
      }
    };
    fetchCategories();
  }, []);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const params = new URLSearchParams();
        if (searchTerm) params.append('search', searchTerm);
        if (selectedCategory !== 'All') params.append('category', selectedCategory);

        const response = await axios.get(`${API_URL}/products?${params.toString()}`);
        setProducts(response.data);
      } catch (error) {
        console.error('Ошибка загрузки товаров:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, [searchTerm, selectedCategory]);

  return (
    <div className="bg-gray-50 min-h-screen">
      <header className="bg-indigo-600 p-4">
        <div className="container mx-auto">
          <h1 className="text-3xl font-bold text-white">🌟 Каталог товаров</h1>
        </div>
      </header>

      <main className="container mx-auto p-4">
        {/* Фильтры */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8 bg-black p-4 rounded-lg shadow">
          <input
            type="text"
            placeholder="🔎 Поиск по названию..."
            value={searchTerm}
            onChange={(e: ChangeEvent<HTMLInputElement>) => setSearchTerm(e.target.value)}
            className="p-2 border border-blue-400 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <select
            value={selectedCategory}
            onChange={(e: ChangeEvent<HTMLSelectElement>) => setSelectedCategory(e.target.value)}
            className="p-2 border border-purple-400 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-purple-500"
          >
            {categories.map(cat => (
              <option key={cat} value={cat}>
                {cat}
              </option>
            ))}
          </select>
        </div>

        {/* Товары */}
        {loading ? (
          <p className="text-center text-blue-600 text-lg font-semibold">⏳ Загрузка товаров...</p>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {products.length > 0 ? (
              products.map(product => (
                <div
                  key={product.id}
                  className="bg-yellow-100 rounded-lg shadow-md overflow-hidden transform hover:-translate-y-1 transition-transform duration-300 border border-yellow-300"
                >
                  <div className="p-6">
                    <span className="text-xs font-bold text-purple-700 bg-purple-100 px-2 py-1 rounded-full">
                      {product.category}
                    </span>
                    <h2 className="text-xl font-bold text-blue-800 mt-2 min-h-12">{product.name}</h2>
                    <p className="text-2xl font-extrabold text-green-600 mt-4">${product.price}</p>
                  </div>
                </div>
              ))
            ) : (
              <p className="col-span-full text-center text-red-600 font-semibold">🚫 Товары не найдены.</p>
            )}
          </div>
        )}
      </main>
    </div>
  );
}
