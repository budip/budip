# Use Node.js LTS as the base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project to the container
COPY . .

# Expose the application port
EXPOSE 3000

# Start the server
CMD ["node", "server.js"]