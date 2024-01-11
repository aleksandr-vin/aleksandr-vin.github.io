# Notes on development

Run locally with drafts:

    docker run --rm -it -v $(pwd):/code -w /code -p 4000:4000 ruby:2 \
      sh -c 'bundle install && exec jekyll serve --host 0.0.0.0 --drafts'

or

    JEKYLL_ENV=production bundle exec jekyll serve --drafts