# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy only package files first to leverage Docker cache.
# If package files haven't changed, npm install will be skipped on rebuild.
COPY package*.json ./
# Install dependencies
RUN npm install

# Copy the rest of the app
COPY . .

# Build Next.js app
RUN npm run build

# Expose port
EXPOSE 3000

# Start the server
CMD ["npm", "run", "dev"]
# CMD ["npm", "run", "start"]