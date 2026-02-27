# =========================
# 1️⃣ Build stage
# =========================
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Install dependencies first (better caching)
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./

# Choose ONE package manager (npm assumed here)
RUN npm install

# Copy source code
COPY . .

# Build Next.js app
RUN npm run build


# =========================
# 2️⃣ Production stage
# =========================
FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

# Copy only required files from builder
COPY --from=builder /app/package.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/next.config.js ./next.config.js

# Expose Next.js port
EXPOSE 3000

# Start Next.js
CMD ["npm", "run", "start"]