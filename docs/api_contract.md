# Crypto Momentum Dashboard — API Contract

This document defines the backend API endpoints for the Crypto Momentum Dashboard project.

The backend will expose simple JSON endpoints that the frontend dashboard can consume.

---

# 1. Health Check

Endpoint

GET /health

Purpose

Verify that the backend server is running.

Response

{
  "status": "ok"
}

---

# 2. List Coins

Endpoint

GET /api/coins

Purpose

Return all tracked cryptocurrencies along with their latest price and momentum score.

Response

{
  "coins": [
    {
      "symbol": "BTC",
      "name": "Bitcoin",
      "price_usd": 92000.12,
      "momentum_score": 4.82
    },
    {
      "symbol": "ETH",
      "name": "Ethereum",
      "price_usd": 4800.55,
      "momentum_score": 3.11
    }
  ]
}

Fields

symbol — short ticker symbol  
name — full cryptocurrency name  
price_usd — latest price in USD  
momentum_score — calculated short-term momentum score

---

# 3. Top Momentum Coins

Endpoint

GET /api/top

Purpose

Return the highest momentum cryptocurrencies ranked from strongest to weakest.

Response

{
  "top_coins": [
    {
      "symbol": "BTC",
      "name": "Bitcoin",
      "momentum_score": 4.82
    },
    {
      "symbol": "SOL",
      "name": "Solana",
      "momentum_score": 4.01
    },
    {
      "symbol": "ETH",
      "name": "Ethereum",
      "momentum_score": 3.11
    }
  ]
}
