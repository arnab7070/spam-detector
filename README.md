# Spam Predictor API

A minimal Flask web application for spam detection, hosted on **Render** or **Vercel**. This API uses a pre-trained machine learning model to classify comments as "Spam" or "Not Spam."

---

## Features

- **Flask-based API** for spam prediction.
- **Endpoints**:
  - `GET /`: Status check.
  - `POST /predict`: Predicts whether a comment is spam.
- Deployable on **Render** or **Vercel**.

---

## Getting Started

Follow these instructions to set up and run the API locally or deploy it on a hosting service.

---

### Prerequisites

#### For Local Development:
- Python 3.8+
- Required Python dependencies (`requirements.txt`).

#### For Vercel:
- Node.js installed.
- npm (Node Package Manager) installed.
- axios library installed (`npm install axios`).

---

## Folder Structure

```
.
├── app.py             # Main Flask application
├── index.py           # (Optional) Additional application entry point
├── model.pkl          # Pre-trained ML model
├── vocabulary.pkl     # Vocabulary for the vectorizer
├── requirements.txt   # Python dependencies
├── vercel.json        # (Optional) Vercel-specific configuration
├── wsgi.py            # WSGI entry point for production
└── README.md          # Project documentation
```

---

## Local Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arnab7070/spam-detector.git spam-detector
   cd spam-detector
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Locally**:
   ```bash
   python wsgi.py
   ```
   Access the app at `http://127.0.0.1:5000`.

---

## Deployment Instructions

### Hosting on Render

1. **Push Code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/arnab7070/spam-detector.git
   git push -u origin main
   ```

2. **Create a Render Web Service**:
   - Go to [Render](https://render.com).
   - Create a **New Web Service**.
   - Connect your GitHub repository.
   - Use the following configuration:
     - **Start Command**: `gunicorn wsgi:app`
     - **Runtime**: Python 3.

3. **Deploy and Test**:
   - Once deployed, Render will provide a public URL.
   - Use Postman or cURL to test the `/predict` API.

---

### Hosting on Vercel

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy the App**:
   ```bash
   vercel deploy
   ```

3. **Optimize for Vercel**:
   - Convert `model.pkl` and `vocabulary.pkl` to JSON format if their size exceeds 250 MB.
   - Update the app to load JSON files instead.

---

## Example Usage with Axios

Here's an example of how to interact with the API using **axios** in a Node.js application:

```javascript
const axios = require('axios');

async function makePrediction(commentText) {
  try {
    const response = await axios.post('https://spam-detector-2v99.onrender.com/predict', { comment: commentText });
    const responseData = response.data;
    console.log('Prediction:', responseData);
  } catch (error) {
    console.error('Error making prediction:', error.message);
  }
}

// Example usage
const commentText = 'This is a sample comment.';
makePrediction(commentText);
```

---

## API Documentation

### **1. Home Route**
- **Endpoint**: `GET /`
- **Response**:
  ```json
  {
    "message": "Spam Detection Server is Running!"
  }
  ```

### **2. Spam Prediction**
- **Endpoint**: `POST /predict`
- **Request Body**:
  - `comment` (string): The text comment for prediction.
- **Response**:
  ```json
  {
    "result": 0 or 1
  }
  ```

---

## Notes

- If using **Vercel**, ensure that your `model.pkl` and `vocabulary.pkl` are in a format and size compatible with serverless function limits.
- For larger deployments, use external storage (e.g., AWS S3) or a platform like Render.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


This `README.md` combines instructions for both **Vercel** and **Render** deployment, includes examples, and API documentation in a clear structure. Let me know if you need further adjustments!