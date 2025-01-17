# Use Node.js as the base image for building the React app
FROM node:16-slim AS build

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and yarn.lock to install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the application
COPY . .

# Expose the development server port
EXPOSE 3000

# Run the development server
CMD ["yarn", "start"]