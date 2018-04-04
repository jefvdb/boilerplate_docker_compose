FROM node:carbon

WORKDIR /src

# install the deps first, creates a nice snapshot
COPY src/package.json /src
RUN npm install

COPY src /src

EXPOSE 8080

CMD [ "npm", "start" ]
