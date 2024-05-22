import React, { useState, useEffect } from 'react';
import './style/MovieList.css'; // Import CSS file for styling

const MovieList = () => {
  const [filter, setFilter] = useState('');
  const [search, setSearch] = useState('');

const [movies, setMovies] = useState([]);

useEffect(() => {
    const fetchData = async () => {
      try {
        // Make API call
        const response = await fetch('http://localhost:8000/movies/');
        
        // Parse JSON response
        const jsonData = await response.json();
        
        // Update state with fetched data
        setMovies(jsonData);
        console.log(jsonData)
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    
    fetchData(); // Call the async function to fetch data
  }, []); // Empty dependency array means this effect runs only once, when the component mounts

  const filteredMoviesList = movies.filter(movie_data => {
    return movie_data.movies.map((movie) => {
      return (movie.title.toLowerCase().includes(search.toLowerCase()))
    })
  });

  return (
    <div className="movie-list-container">
      <input
        type="text"
        placeholder="Search by title..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="search-input"
      />
      <select
        value={filter}
        onChange={e => setFilter(e.target.value)}
        className="filter-select"
      >
        <option value="">All Genres</option>
        <option value="action">Action</option>
        <option value="comedy">Comedy</option>
        <option value="drama">Drama</option>
        {/* Add more genres as needed */}
      </select>

      <table className="movie-table">
        <thead>
          <tr>
            <th>MONTH</th>
            <th>DAY</th>
            <th>FILM</th>
            <th>RELEASED</th>
            <th>RATING</th>
            <th>LIKE</th>
            <th>REWATCH</th>
            <th>REVIEW</th>
          </tr>
        </thead>
        <tbody>
          {movies.length > 0 && filteredMoviesList.map((movie_list, key) => (
            movie_list.movies.map((movie, k) => (
              <tr key={k}>
              <td>{movie.released.split(' ')[1]}</td>
              <td>{movie.released.split(' ')[0]}</td>
              <td>{movie.title}</td>
              <td>{movie.year}</td>
              <td>{movie.imdb_rating}</td>
              <td>{movie.meta_score > 80 ? '&hearts;' : '&#x2661;' }</td>
              <td>{''}</td>
              <td>{''}</td>
            </tr>
            ))
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MovieList;
