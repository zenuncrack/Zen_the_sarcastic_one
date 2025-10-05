

  <h1>🤖 Zen_the_sarcastic_one</h1>

  <p>A sarcastic yet friendly AI chatbot built using <a href="https://www.langchain.com/">LangChain</a>, <a href="https://streamlit.io/">Streamlit</a>, and <a href="https://ollama.com/">Ollama</a> running the <strong>Gemma3 1B</strong> model locally.</p>

  <p>Zen doesn’t sugarcoat. Zen doesn’t flatter. Zen responds with wit, sarcasm, and just enough charm to keep you coming back.</p>

  <hr>

  <h2>✨ Features</h2>
  <ul>
    <li>🧠 Powered by <strong>Google's Gemma 3B</strong> via Ollama</li>
    <li>🧩 Integrated with <strong>LangChain</strong> for modular prompting and chaining</li>
    <li>🖼️ Built with <strong>Streamlit</strong> for a fast, interactive web UI</li>
    <li>🎭 Zen responds in a <strong>sarcastic, but non-offensive tone</strong></li>
    <li>🛠️ Runs <strong>100% locally</strong> – no OpenAI key or cloud API required</li>
  </ul>

  <hr>

  <h2>🚀 Getting Started</h2>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/yourusername/Zen_the_sarcastic_one.git
cd Zen_the_sarcastic_one
</code></pre>

  <h3>2. Install Requirements</h3>
  <p>We recommend using a virtual environment.</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. Install & Run Ollama</h3>
  <p>Make sure you have <a href="https://ollama.com/">Ollama</a> installed and running.</p>
  <p>Pull the Gemma model:</p>
  <pre><code>ollama pull gemma:1b</code></pre>
  <p><strong>🔁 You can change the model in the script to <code>gemma:7b</code> or another if you prefer.</strong></p>

  <hr>

  <h2>🧪 Run the App</h2>
  <pre><code>streamlit run app.py</code></pre>

  <p>Open your browser and go to:</p>
  <pre><code>http://localhost:8501</code></pre>

  <hr>

  <h2>💬 Example Prompt</h2>
  <blockquote>
    <p><strong>You</strong>: What's the capital of France?</p>
    <p><strong>Zen</strong>: Oh, just the tiny little city you've probably never heard of — <em>Paris</em>. You know, the place with the tower everyone posts on Instagram?</p>
  </blockquote>

  <hr>

  <h2>📁 Project Structure</h2>
  <pre><code>Zen_the_sarcastic_one/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── .env (optional)       # Environment variables if needed
</code></pre>

  <hr>

  <h2>📦 Dependencies</h2>
  <ul>
    <li>langchain</li>
    <li>streamlit</li>
    <li>langchain-community</li>
    <li>langchain-core</li>
    <li>python-dotenv</li>
    <li>ollama</li>
  </ul>

  <p>Install them with:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <hr>

  <h2>🙃 Zen's Philosophy</h2>
  <blockquote>
    <p>"I'm not saying you're wrong. I'm just saying you're creatively misinformed."</p>
  </blockquote>

  <hr>

  <h2>📄 License</h2>
  <p>MIT License. Do whatever, but don’t blame Zen if he roasts your users.</p>

  <hr>

  <h2>✍️ Author</h2>
  <p>Built by <a href="https://github.com/zenuncrack">Zenun Chowdhury</a> with too much sarcasm and too little sleep.</p>

</body>
</html>
