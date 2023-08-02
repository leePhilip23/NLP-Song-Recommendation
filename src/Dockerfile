FROM python:3.11
COPY . /streamlit-UI
WORKDIR /streamlit-UI
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "--server.port", "8501", "streamlit-UI.py"]