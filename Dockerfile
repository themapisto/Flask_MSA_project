FROM python:3.9
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

### 파이썬 모듈을 실행시키는 방식으로 flask를 실행시켜주었다.
### flask를 외부에 노출시키기 위해 --host=0.0.0.0태그를 넣어주었다.