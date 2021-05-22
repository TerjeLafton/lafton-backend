# Use alpine base image for minimal size.
# This is just a image to extend the original postres image to create our databases at launch.
FROM postgres:13-alpine

# Create the dev and test databases from the create.sql file on initiation.
ADD create.sql /docker-entrypoint-initdb.d