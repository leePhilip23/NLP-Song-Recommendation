import React, { useState } from 'react';
import Loader from './loader';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [summary, setSummary] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };
  

  const handleSummarizeClick = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/post_text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      const data = await response.json();
      setSummary(data.summary);
      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className={`App ${isDarkMode ? 'dark-mode' : ''}`}>
      <header className="App-header">
      <div className="App-title">NLP News Summarizer</div>
        <div className="header-buttons">
          <a className="App-link" href="https://github.com/leePhilip23/NLP_News_Summarization" target="_blank" rel="noopener noreferrer">
            Visit GitHub
          </a>
        </div>
       
      </header>
      <main className="App-main">
        <h2 className="text-title">
          Summarize any news article with AI
        </h2>
        <textarea
          className="Input-textbox"
          placeholder="Copy and paste any link to a news article to summarize..."
          value={inputText}
          onChange={handleInputChange}
        />
        
        <button className="Summarize-button" onClick={handleSummarizeClick}>
          <div classname="Summarize-button-text">
            Summarize
          </div>
        </button>
        {(summary )? (
          <div>
            <h3 className="result-holder">Summary</h3>
            <div className="Summary-result">
            {summary}
          </div>
        </div>
        ) : ( isLoading &&
          <Loader />
        )}

      </main>
    </div>
  );
}

export default App;

