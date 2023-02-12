# build stage
FROM node:lts-alpine as build-stage

# prepare sources
COPY ./*.json ./*.ts ./*.html ./*.md /app/
COPY ./nginx/ /app/nginx/
COPY ./src/ /app/src/
COPY ./public/ /app/public/
WORKDIR /app
RUN npm install

# build with api url argument
ARG VITE_API_URL
RUN npm run build

# production stage
FROM nginx:alpine as production-stage
COPY --from=build-stage /app/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
