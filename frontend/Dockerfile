# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and lockfile
COPY package*.json ./
COPY .env .env

# Install dependencies
RUN npm install

# Copy the rest of the app
COPY . .

# Expose Vite dev server port
EXPOSE 5173

# Run Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]