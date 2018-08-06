FROM python:3-alpine

WORKDIR /opt/application
RUN apk --no-cache add alpine-sdk freetype-dev libpng-dev pkgconfig
RUN pip install matplotlib

COPY . .
CMD ["python", "./chicago_bikeshare.py"]