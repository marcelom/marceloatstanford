# Marcelo @ Stanford

This is the data for my personal blog at work.

It is automatically transformed by [Pelican](http://getpelican.com) into a static site whenever I push code to this git repository.

It uses GitHub's webhook for teh automatic deployment, which call a cgi script in python that refreshes the code and runs Pelican on demand to re-publish the site.

Like many others, I dont like the idea of my blog posts ending up somewhere in a database... I want to be able to author the posts locally in Markdown (and possibly Textile), and have full control of the theme. It should also take care of the feed for me. And above all, it needs version control (GitHub) !

# How to use it

You need first to setup a Python virtual environment:

  virtualenv website

Then open the virtualenv:

  cd website ; source bin/activate

Install all the dependencies, pelican and Markdown:

  pip install Markdown pelican

Clone the git repo:

  git clone https://github.com/marcelom/marceloatstanford.git

Now you are ready to start... Make sure to visit the Pelican docs at http://docs.getpelican.com/ for more info on how to use it.

# License

All original content is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/)