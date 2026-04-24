# 1. Pegamos a imagem do Python (Nossa cozinha)
FROM python:3.12-slim

# 2. Definimos que tudo o que fizermos agora será dentro da pasta /app
WORKDIR /app

# 3. Evitamos que o Python crie arquivos temporários desnecessários
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Instalamos dependências do sistema para o banco de dados PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/apt/lists/*

# 5. Copiamos o nosso "Manual de Instruções" para dentro do Docker
COPY requirements.txt .

# 6. Mandamos o Docker ler o manual e instalar tudo
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copiamos o resto dos nossos códigos para dentro da pasta /app
COPY . .

# 8. O comando que deixa o nosso "Garçom" (API) esperando pedidos
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]