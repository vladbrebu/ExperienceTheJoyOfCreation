function fetchJoke() {
    return new Promise((resolve, reject) => {
      const apiUrl = 'https://v2.jokeapi.dev/joke/Any';
  
      fetch(apiUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          resolve(data);
        })
        .catch(error => {
          reject(error);
        });
    });
  }
  
  // Example usage
  fetchJoke()
    .then(jokeData => {
      console.log(`Joke: ${jokeData.joke || `${jokeData.setup} ${jokeData.delivery}`}`);
    })
    .catch(error => {
      console.error("Error fetching joke:", error);
    });