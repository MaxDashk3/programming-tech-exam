FROM alpine
RUN apk add --update python3 py-pip
COPY arithmetic_progression_sum.py main.py /app/
WORKDIR /app
CMD ["python", "main.py"]