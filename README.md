<h1>Deploy</h1>
<p>python -m venv venv</p>
<p>pip install -r requirements.txt</p>
<p>source venv/bin/activate</p>
<p>touch .env</p>
<p>Enter on the https://platform.openai.com/account/api-keys</p>
<p>Create new OPENAI API KEY and COPY</p>
<p>PASTE into .env</p>
<b>must be look as OPENAI_API_KEY={your_api_key}</b>
<hr>
<p>uvicorn main:app --host 0.0.0.0 --port 8000</p>
