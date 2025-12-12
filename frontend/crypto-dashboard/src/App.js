import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const cryptos = ["BTC", "ETH", "SOL", "DOGE"];

  const [prices, setPrices] = useState({});
  const [loading, setLoading] = useState(true);
  const [timer, setTimer] = useState(10);

  // Timer countdown for auto-refresh
  useEffect(() => {
    const interval = setInterval(() => {
      setTimer((t) => (t > 1 ? t - 1 : 10));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  // Fetch all prices every time timer resets to 10
  useEffect(() => {
    if (timer === 10) fetchAll();
  }, [timer]);

  async function fetchAll() {
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/crypto-prices");
      const data = await res.json();
      setPrices(data);
    } catch (err) {
      console.error("Error fetching prices:", err);
      // set all to N/A on error
      let empty = {};
      cryptos.forEach((c) => (empty[c] = "N/A"));
      setPrices(empty);
    }
    setLoading(false);
  }

  // Initial load
  useEffect(() => {
    fetchAll();
  }, []);

  return (
    <div className="App">
      <h1>Crypto Live Prices</h1>
      <p className="timer">Refreshing in {timer} sec…</p>

      <div className="grid">
        {cryptos.map((symbol) => (
          <div key={symbol} className="card">
            <h2>{symbol}</h2>
            {loading ? <p>Loading...</p> : <h3>${prices[symbol]}</h3>}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
