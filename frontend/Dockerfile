FROM node:18

WORKDIR /app

# Print what's being copied
COPY package*.json ./
COPY .env .env

RUN echo "📦 Installing dependencies..." \
    && npm install \
    && echo "✅ Done installing dependencies."

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev"]