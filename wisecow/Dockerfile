FROM ubuntu:latest

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    cowsay \
    fortune-mod \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Fix PATH issue (IMPORTANT)
ENV PATH="/usr/games:$PATH"

# Create app directory
WORKDIR /app

# Copy script into container
COPY wisecow.sh .

# Give execute permission
RUN chmod +x wisecow.sh

# Expose port
EXPOSE 4499

# Run the app
CMD ["./wisecow.sh"]