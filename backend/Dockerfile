# Multi stage build for developent container.
# Use full size Python image as builder. This is a temp build image which is disgarded in the final build.
# This ensures that we can build the base image with minimal layers to make the final image as small as possible.
FROM python:3.9 as builder

# Copy the requirements from the project files to the builder image. This creates a new Docker Layer.
COPY requirements.txt .

# Build wheels for the python packages in the requirements.txt.
# This lets us create wheels ready for install for the final image, reducing build time.
RUN pip wheel \
	--no-cache-dir \
	--no-deps \
	--wheel-dir /wheels \
	-r requirements.txt

# Use the alpine version of the Python image for the smallest final image possible.
FROM python:3.9-alpine

# Copy the wheels created from the builder image and install them with pip.
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Set the working directory to the /app folder and copy the rest of the project over.
WORKDIR /app
COPY . .