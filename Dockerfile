
FROM jekyll/jekyll:pages

COPY Gemfile* /srv/jekyll/

WORKDIR /srv/jekyll

RUN apk update && \
	apk add ruby-dev ruby-bundler nodejs gcc make curl build-base libc-dev libffi-dev zlib-dev libxml2-dev libgcrypt-dev libxslt-dev python

# RUN bundle clean
# RUN bundle config build.nokogiri --use-system-libraries	
# RUN bundle install
# RUN bundle exec jekyll liveserve
# RUN bundle exec jekyll serve

EXPOSE 4000
