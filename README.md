# ai-streamlit-application
This web application was created with streamlit. While the web app is running, you are able to upload a csv-file and ask questions about the uploaded csv-file with the help of PandasAI and OpenAI. You need a valid OpenAI-Key.

# Installation 
Please install the following Python Packages:
- os
- dotenv
- streamlit
- pandas
- pandasai
- matplotlib

You also need to create a file named ".env" and open it with text editor. Then you write the following variable inside and save it:
OPENAI_API_KEY="OPENAI-API_KEY" (for OPENAI-API-KEY you need to type in your valid API-Key)

# Starting the application
For the application to run you need to type in the following command inside the folder of the Python script:

"streamlit run main.py"

This will open the streamlit application in your standard browser.
