FROM python:3.11-slim

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Porta da aplicação
EXPOSE 8008

# Produção
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8008"]
