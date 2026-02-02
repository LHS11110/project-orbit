const API_BASE_URL = '/api';

export async function getMovies() {
    const response = await fetch(`${API_BASE_URL}/movies`);
    if (!response.ok) throw new Error('Failed to fetch movies');
    return response.json();
}

export async function getMovie(id) {
    const response = await fetch(`${API_BASE_URL}/movies/${id}`);
    if (!response.ok) throw new Error('Failed to fetch movie');
    return response.json();
}

export async function getFeaturedMovie() {
    const response = await fetch(`${API_BASE_URL}/movies/featured`);
    if (!response.ok) throw new Error('Failed to fetch featured movie');
    return response.json();
}

export async function getCategories() {
    const response = await fetch(`${API_BASE_URL}/categories`);
    if (!response.ok) throw new Error('Failed to fetch categories');
    return response.json();
}

export async function searchMovies(query) {
    const response = await fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error('Failed to search movies');
    return response.json();
}
