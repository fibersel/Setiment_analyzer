FROM python:3.5
ADD main.py /
ADD sentiment_analyser.h5 /
ADD tokenizer.pickle /
RUN pip install Flask
RUN pip install gunicorn
CMD gunicorn main:app --bind 0.0.0.0:$PORT --reload
