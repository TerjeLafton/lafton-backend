# Multi stage build for developent container.
# Use full size Python image as builder. This is a temp build image which is disgarded in the final build.
# This ensures that we can build the base image with minimal layers to make the final image as small as possible.
FROM python:3.9 as builder

# Install required packages. Use --no-cache to minimize image size.
# Netcat is used to check if the database is up and running while postgresql is used to communicate with the database.
RUN apt-get update \
  && apt-get -y install postgresql \
  && apt-get clean

# Build wheels for the python packages in the requirements.txt.
# This lets us create wheels ready for install for the final image, reducing build time.
COPY requirements.txt requirements-dev.txt ./
RUN pip wheel \
	--no-cache-dir \
	--no-deps \
	--wheel-dir /wheels \
	-r requirements-dev.txt

# Use the slim version of the Python image for the smallest final image possible.
# Wanted to use Alpine, but struggled to install asyncpg using wheel. When it finally worked, I took forever installing.
FROM python:3.9-slim

# Stops python from creating __pycache__ file, which is not neccesary files.
ENV PYTHONDONTWRITEBYTECODE 1
# This ensures that the python out is sent straight to the container log without buffering.
ENV PYTHONUNBUFFERED 1

# Copy the wheels created from the builder image and install them with pip.
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Set the working directory to the /app folder and copy the rest of the project over.
WORKDIR /app