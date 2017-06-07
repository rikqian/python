From python:3.6
WORKDIR /usr/src/app
COPY requirements ./
RUN pip install --no-cache-dir -r requirements
COPY . .
CMD ["python","./test.py"]